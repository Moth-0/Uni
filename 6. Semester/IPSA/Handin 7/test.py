import os
import sys
import importlib.util
import matplotlib.pyplot as plt
from pathlib import Path
import traceback

# ---------------------------------------------------------
# MOCK PLT.SHOW(): 
# Mutes the student's plt.show() so it doesn't freeze the loop.
# ---------------------------------------------------------
plt.show = lambda *args, **kwargs: None 

# Define standard test cases with the EXPECTED correct points (as a set)
# A set is used so we only check *which* points are included, ignoring the order.
TEST_CASES = {
    "square_with_center": {
        "points": [(0,0), (0,2), (2,0), (2,2), (1,1)],
        "expected_set": {(0,0), (0,2), (2,0), (2,2)} # (1,1) is inside and should be ignored
    },
    "collinear_points": {
        "points": [(0,0), (1,1), (2,2), (3,3), (0,2), (2,0)],
        "expected_set": {(0,0), (3,3), (0,2), (2,0)} # (1,1) and (2,2) are on the line and must be excluded
    },
    "right_triangle_on_line": {
        "points": [(0,0), (1,0), (2,0), (0,1), (0,2)],
        "expected_set": {(0,0), (2,0), (0,2)} # (1,0) and (0,1) are on the edges and must be excluded
    }
}

def load_module_from_path(filepath):
    """Dynamically loads a Python file as a module."""
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

def main():
    base_dir = Path(__file__).parent
    test_script_name = Path(__file__).name
    
    py_files = list(base_dir.rglob("*.py"))
    print(f"Starting tests with automated grading...\n")
    
    for py_file in py_files:
        if py_file.name == test_script_name:
            continue
            
        student_folder = py_file.parent
        print(f"Testing: {student_folder.name}/{py_file.name}")
        
        module = load_module_from_path(py_file)
        if not module:
            continue
            
        if not hasattr(module, 'convex_hull') or not hasattr(module, 'plot_hull'):
            print(f"  [!] Missing 'convex_hull' or 'plot_hull' in {py_file.name}")
            continue
            
        convex_hull_func = getattr(module, 'convex_hull')
        plot_hull_func = getattr(module, 'plot_hull')
        
        # Run test cases
        for test_name, test_data in TEST_CASES.items():
            try:
                test_points = test_data["points"]
                expected_set = test_data["expected_set"]
                
                # 1. Calculate hull
                hull_result = convex_hull_func(test_points.copy())
                
                # 2. Automatically verify the result
                student_set = set(hull_result)
                if student_set == expected_set:
                    status = "PASS"
                    print(f"  [✓] {test_name}: PASS")
                else:
                    status = "FAIL"
                    print(f"  [X] {test_name}: FAIL (Expected {expected_set}, got {student_set})")

                # 3. Setup a new figure
                plt.figure()
                plt.title(f"[{status}] {student_folder.name} | {test_name}")
                
                # 4. Call the student's plot function
                plot_hull_func(test_points.copy(), hull_result)
                
                # 5. Save the figure
                output_filename = f"test_result_{test_name}.png"
                output_filepath = student_folder / output_filename
                plt.savefig(output_filepath)
                plt.close() 
                
            except Exception as e:
                print(f"  [!] Error running test '{test_name}' on {py_file.name}:")
                traceback.print_exc(limit=1, file=sys.stdout)
                plt.close()
                
        print("-" * 40)

if __name__ == "__main__":
    main()