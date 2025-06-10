# 🧮 Python CLI Calculator

A simple command-line calculator built using Python. This interactive app allows users to perform basic arithmetic operations with user-friendly error handling.

## 📌 Features

- ✅ Addition
- ✅ Subtraction
- ✅ Multiplication
- ✅ Division (with zero check)
- ✅ Percentage calculation
- ✅ Continuous operation until user exits
- ✅ Input validation and error handling

## 🛠️ How It Works

- The program runs in a loop and prompts the user to:
  1. Choose an operation (`add`, `sub`, `div`, `mul`, `percent`, or `exit`)
  2. Enter two numbers
- Based on the operation, it performs the calculation and displays the result.
- It handles invalid inputs gracefully.

## ▶️ Sample Output

Enter the operation(add/sub/div/mul/percent/exit) add
Enter the first number: 10
Enter the second number: 20
The sum is: 30.0

Enter the operation(add/sub/div/mul/percent/exit) div
Enter the first number: 5
Enter the second number: 0
Division cannot be done with 0

Enter the operation(add/sub/div/mul/percent/exit) exit

## 📂 Files

- `calculator.py` — main Python file with all the code

## 🚀 How to Run

1. Make sure you have Python installed.
2. Run the program using:
   ```bash
   python calculator.py
👨‍💻 Made with Python – as part of the "Zero to Hero" learning path.
