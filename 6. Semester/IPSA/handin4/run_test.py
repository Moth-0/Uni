import importlib.util
import glob
import os
import sys
sys.dont_write_bytecode = True  # <--- Prevents creation of __pycache__ folders

# --- CONFIGURATION ---
# No .in files needed here. We define tests in code below.
# ---------------------

def load_module_from_path(path, module_name):
    """
    Dynamically imports a Python file as a module so we can use its functions.
    """
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    return None

def test_student_logic(student_module):
    """
    This is where you define exactly what functions to call and what to print.
    """
    logs = []
    
    # Helper to capture print output easily
    def log(message=""):
        logs.append(str(message))

    try:
        # --- TEST 1: Check generate_labels ---
        if hasattr(student_module, 'generate_tree'):
            n = 4
            log(f"--- Testing generate_tree({n}) ---")
            L = student_module.generate_tree(['A', 'B', 'C', 'D', 'E', 'F'])
            log(f"Output: {L}")
        else:
            log("[ERROR] Function 'generate_labels' is missing.")

        log() # Empty line

        # --- TEST 2: generate_triplets ---
        if hasattr(student_module, 'generate_triplets'):
            log(f"--- Testing generate_triplets(L) ---")
            trips = student_module.generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E'))))

            log(f"Trips: {trips}")
            log(f"len(trips): {len(trips[1])}")
        else:
            log("[ERROR] Function 'generate triplets' is missing.")

        log() # Empty line

        # --- TEST 3: Check triplet_distance ---
        if hasattr(student_module, 'triplet_distance'):
            log(f"--- Testing triplet_distance ---")
            dist = student_module.triplet_distance(((('A', 'F'), 'B'), ('D', ('C', 'E'))), (((('D', 'A'), 'B'), 'F'), ('C', 'E')))

            log(f"Output: {dist}")
        else:
            log("[ERROR] Function 'triplet_distance' is missing.")

        log()

    except Exception as e:
        log(f"\n[CRITICAL ERROR] Code crashed during execution: {e}")

    return "\n".join(logs)

def run_function_grader():
    # Find all student scripts
    student_scripts = glob.glob("*/*.py") 
    print(f"Found {len(student_scripts)} scripts. Starting evaluation...")

    for script_path in student_scripts:
        folder = os.path.dirname(script_path)
        script_name = os.path.basename(script_path)
        
        # Unique module name to prevent conflicts between students
        module_name = f"student_{script_name.replace('.py', '')}"

        print(f"Evaluating {script_path}...")

        output_file = os.path.join(folder, f"test_{script_name}.txt")
        
        with open(output_file, "w", encoding="utf-8") as report:
            report.write(f"FUNCTION TESTS FOR: {script_name}\n")
            report.write("=" * 40 + "\n\n")

            try:
                # 1. Import their code
                mod = load_module_from_path(script_path, module_name)
                
                # 2. Run the tests defined in test_student_logic
                if mod:
                    test_output = test_student_logic(mod)
                    report.write(test_output)
                else:
                    report.write("[ERROR] Could not load module (syntax error?).")

            except Exception as e:
                report.write(f"[SYSTEM ERROR] Could not import file: {e}")

            report.write("\n\n" + "-" * 30 + "\n")

    print("\nDone! Results saved to 'function_test_results.txt' in each folder.")

if __name__ == "__main__":
    run_function_grader()