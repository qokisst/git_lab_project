import subprocess
import sys

def run_test(args, expected_output, expected_code=0):
    process = subprocess.run(['./app'] + args, capture_output=True, text=True)
    output = process.stdout + process.stderr 
    
    if expected_output not in output:
        print(f"FAIL: Expected {expected_output}, got {output}")
        sys.exit(1)
    if process.returncode != expected_code:
        print(f"FAIL: Expected code {expected_code}, got {process.returncode}")
        sys.exit(1)
    print(f"PASS: {args}")

# Тест 1: Сложение
run_test(['10', '+', '5'], '15')
# Тест 2: Вычитание
run_test(['10', '-', '3'], '7')
# Тест 3: Деление на ноль (ожидаем ошибку и код возврата 1)
run_test(['10', '/', '0'], 'Division by zero', 1)