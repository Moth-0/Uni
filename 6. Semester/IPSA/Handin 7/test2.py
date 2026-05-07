import os
import sys
import importlib.util
import matplotlib.pyplot as plt
from pathlib import Path
import traceback

plt.show = lambda *args, **kwargs: None 

# Define test cases with the EXACT expected list to enforce ordering and starting point
TEST_CASES = {
    "square_with_center": {
        "points": [(0,0), (0,2), (2,0), (2,2), (1,1)],
        # Clockwise starting from (0,0)
        "expected_list": [(0,0), (0,2), (2,2), (2,0)] 
    },
    "collinear_points": {
        "points": [(0,0), (1,1), (2,2), (3,3), (0,2), (2,0)],
        # Clockwise from (0,0), strictly excluding (1,1) and (2,2)
        "expected_list": [(0,0), (0,2), (3,3), (2,0)] 
    },
    "right_triangle_on_line": {
        "points": [(0,0), (1,0), (2,0), (0,1), (0,2)],
        # Clockwise from (0,0), excluding the midpoints on the axes
        "expected_list": [(0,0), (0,2), (2,0)] 
    }
}

def load_module_from_path(filepath):
    module_name = filepath.stem
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"  [!] Failed to execute module {filepath.name}: {e}")
        return None

def diagnose_failure(student_list, expected_list):
    """Provides specific feedback based on the exercise rules."""
    student_set = set(student_list)
    expected_set = set(expected_list)
    
    if expected_set.issubset(student_set) and len(student_list) > len(expected_list):
        return f"Failed Rule 6: Included collinear/interior points. Expected {len(expected_list)} points, got {len(student_list)}."
    
    if student_set == expected_set:
        if student_list[0] != expected_list[0]:
            return "Failed Rule 4: Did not start at lexicographically smallest point."
        return "Failed Rule 3: Points are not in clockwise order."
        
    return f"Failed Rules 1/2/5: Missing points or incorrect geometry. Expected {len(expected_list)} points, got {len(student_list)}."

def main():
    base_dir = Path(__file__).parent
    test_script_name = Path(__file__).name
    
    py_files = list(base_dir.rglob("*.py"))
    print("Starting tests with strict rule compliance...\n")
    
    for py_file in py_files:
        if py_file.name == test_script_name:
            continue
            
        student_folder = py_file.parent
        print(f"Testing: {student_folder.name}/{py_file.name}")
        
        module = load_module_from_path(py_file)
        if not module:
            continue
            
        if not hasattr(module, 'convex_hull') or not hasattr(module, 'plot_hull'):
            print(f"  [!] Missing required functions in {py_file.name}")
            continue
            
        convex_hull_func = getattr(module, 'convex_hull')
        plot_hull_func = getattr(module, 'plot_hull')
        
        for test_name, test_data in TEST_CASES.items():
            try:
                test_points = test_data["points"]
                expected_list = test_data["expected_list"]
                
                hull_result = convex_hull_func(test_points.copy())
                
                # STRICT LIST COMPARISON
                if hull_result == expected_list:
                    status = "PASS"
                    print(f"  [✓] {test_name}: PASS")
                else:
                    status = "FAIL"
                    diagnosis = diagnose_failure(hull_result, expected_list)
                    print(f"  [X] {test_name}: FAIL -> {diagnosis}")

                plt.figure()
                plt.title(f"[{status}] {student_folder.name} | {test_name}")
                plot_hull_func(test_points.copy(), hull_result)
                
                output_filepath = student_folder / f"test_result_{test_name}.png"
                plt.savefig(output_filepath)
                plt.close() 
                
            except Exception as e:
                print(f"  [!] Error running test '{test_name}':")
                traceback.print_exc(limit=1, file=sys.stdout)
                plt.close()
                
        print("-" * 40)

if __name__ == "__main__":
    main()