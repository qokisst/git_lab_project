#include <iostream>
#include <string>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cout << "Usage: app <num1> <operation> <num2>\n";
        return 1;
    }

    int a = std::stoi(argv[1]);
    std::string op = argv[2];
    int b = std::stoi(argv[3]);
    int result = 0;

    if (op == "+") {
        result = a + b;
    } else if (op == "-") {
        result = a - b;
    } else if (op == "/") {
        if (b == 0) {
            std::cout << "Division by zero\n"; // Обработка деления на ноль
            return 1; // Возвращаем код ошибки
        }
        result = a / b;
    } else {
        std::cout << "Unknown operation\n";
        return 1;
    }

    std::cout << result << "\n";
    return 0;
}