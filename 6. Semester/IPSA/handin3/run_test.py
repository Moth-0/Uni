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
        if hasattr(student_module, 'generate_labels'):
            n = 4
            log(f"--- Testing generate_labels({n}) ---")
            L = student_module.generate_labels(n)
            log(f"Output: {L}")
        else:
            log("[ERROR] Function 'generate_labels' is missing.")

        log() # Empty line

        # --- TEST 2: Check permute(4) ---
        if hasattr(student_module, 'permute'):
            log(f"--- Testing permute(L) ---")
            p = student_module.permute(L)
            log(f"Output: {p}")
        else:
            log("[ERROR] Function 'permute' is missing.")

        log() # Empty line

        # --- TEST 3: Check pairs ---
        if hasattr(student_module, 'pairs'):
            log(f"--- Testing pairs({p}) ---")
            pair = student_module.pairs(p)
            log(f"Output: {pair}")
        else:
            log("[ERROR] Function 'pairs' is missing.")

        log() 

        # --- TEST 4: Check anchored_triplets ---
        if hasattr(student_module, 'anchored_triplets'):
            L = p
            R = ['X', 'Y', 'Z']
            log(f"--- Testing anchored_triplets({L}, {R}) ---")
            result = student_module.anchored_triplets(L, R)
            # Format list output for readability
            log(f"Output: {result}")
            log(f'Number: {len(result)}')
        else:
            log("[ERROR] Function 'anchored_triplets' is missing.")

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