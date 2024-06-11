import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculate(operation, num1, num2):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)
    return result

st.title("Perfect Calculator")

num1 = st.number_input("Enter first number:")
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])
num2 = st.number_input("Enter second number:")

if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")
