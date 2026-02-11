import subprocess
import glob
import os

# --- CONFIGURATION ---
TEST_DIR = r"tests"      # Folder containing your .in files
TIMEOUT = 3             # Safety timeout in seconds
# ---------------------

def run_simple_grader():
    # 1. Get all test inputs
    test_inputs = sorted(glob.glob(os.path.join(TEST_DIR, "*.txt")))
    if not test_inputs:
        print(f"Error: No .in files found in {TEST_DIR}")
        return

    # 2. Find all .py files in subdirectories (e.g., "student_name/hw1.py")
    student_scripts = glob.glob("*/*.py") 

    print(f"Found {len(student_scripts)} scripts. Starting execution...")

    for script_path in student_scripts:
        folder = os.path.dirname(script_path)
        script_name = os.path.basename(script_path)
        output_file = os.path.join(folder, "test_results.txt")

        print(f"Running {script_path}...")

        with open(output_file, "w", encoding="utf-8") as report:
            report.write(f"OUTPUT CAPTURE FOR: {script_name}\n")
            report.write("=" * 40 + "\n\n")

            for test_in in test_inputs:
                report.write(f"--- TEST CASE: {os.path.basename(test_in)} ---\n")
                
                try:
                    # We open the .in file and pass it directly to stdin
                    with open(test_in, 'r', encoding='utf-8') as infile:
                        result = subprocess.run(
                            ["python", script_path],
                            stdin=infile,        # Direct file-to-script input
                            capture_output=True,
                            text=True,
                            timeout=TIMEOUT
                        )
                    
                    # Capture standard output
                    if result.stdout:
                        report.write(result.stdout.strip() + "\n")
                    else:
                        report.write("(No output captured)\n")
                    
                    # Capture errors if they occurred
                    if result.returncode != 0:
                        report.write(f"\n[PROCESS EXITED WITH ERROR CODE {result.returncode}]\n")
                        if result.stderr:
                            report.write(f"Error Details: {result.stderr.strip()}\n")
                        
                except subprocess.TimeoutExpired:
                    report.write(f"\n[TIMEOUT] Program killed after {TIMEOUT}s.\n")
                except Exception as e:
                    report.write(f"\n[SYSTEM ERROR]: {str(e)}\n")
                
                report.write("\n" + "-" * 30 + "\n\n")

    print("\nDone! Results saved to 'test_results.txt' in each folder.")

if __name__ == "__main__":
    if os.path.exists(TEST_DIR):
        run_simple_grader()
    else:
        print(f"Error: '{TEST_DIR}' folder not found.")