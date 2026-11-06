import subprocess
import sys

def run_test(args, expected_output, expected_code=0):
    process = subprocess.run(['./app'] + args, capture_output=True, text=True)
    if expected_output not in process.stdout and expected_code == 0:
        print(f"FAIL: Expected {expected_output}, got {process.stdout}")
        sys.exit(1)
    if process.returncode != expected_code:
        print(f"FAIL: Expected code {expected_code}, got {process.returncode}")
        sys.exit(1)
    print(f"PASS: {args}")


run_test(['10', '+', '5'], '15')

run_test(['10', '-', '3'], '7')

run_test(['10', '/', '0'], 'Division by zero', 1)