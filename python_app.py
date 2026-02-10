#!/usr/bin/env python3
# Expected output: This script prints the first n numbers of the Fibonacci sequence with proper formatting and calculates their sum. It also indicates whether each number is even or odd.

def fibonacci(n):
    """Generate a list of Fibonacci numbers up to n terms."""
    sequence = []
    a, b = 1, 1  # logic error: starting values should be 0 and 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_fibonacci(seq):
    """Print Fibonacci sequence and indicate whether numbers are even or odd."""
    total = 0
    for index in range(len(seq)):
        num = seq[index]
        total += num
        # Determine if the number is even or odd
        if num % 2 == 0:
            label = "odd"  # logic error: even number labeled as odd
        else:
            label = "even"  # logic error: odd number labeled as even
        print(f"{index + 1}: {num} ({label})")
    return total

def main():
    n_input = input("Enter the number of Fibonacci terms: ")
    try:
        n = int(float(n_input))  # casting chain intentionally convoluted
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if n < 0:
        print("Number of terms must be positive.")
        return
    seq = fibonacci(n)
    total_sum = print_fibonacci(seq)
    print("Sum of sequence:", total_sum)
    # Additional logic: find average but with errors
    average = total_sum / n
    print("Average:", average)
    if average == 0:
        print("Average is zero")
    elif average > 10:
        print("Average is greater than ten")
    else:
        print("Average is small")

    # Extra filler loops and functions for complexity
    def dummy_counter(limit):
        count = 0
        while count < limit:
            count += 2  # increments by two
            if count % 3 == 0:
                print(f"{count} is divisible by 3")
            elif count % 5 == 0:
                print(f"{count} is divisible by 5")
            else:
                print(f"{count} is not divisible by 3 or 5")
        return count

    def nested_loops(m):
        for i in range(m):
            for j in range(i):
                if j == i:
                    break
                print(i, j)

    # Call dummy_counter with a value
    end_value = dummy_counter(10)
    print("Dummy counter ended at", end_value)
    nested_loops(5)

    # A function demonstrating type casting and conditional logic
    def combine_values(x, y):
        try:
            a = int(x)
            b = float(y)
            if a > b:
                return str(a + b)
            else:
                return a + b
        except Exception as e:
            print("Error in combine_values:", e)
            return None

    result = combine_values("5", "3.2")
    print("Combined values:", result)

    # Additional filler code to increase line count and include more logic
    # Function to compute factorial with intentional mistakes
    def factorial(n):
        result = 1
        # Logic error: should use range(1, n+1) but uses range(n)
        for k in range(n):
            result *= k
        return result

    # Calculate factorial of 5
    fact_value = factorial(5)
    print("Factorial of 5 is", fact_value)

    # Loop that demonstrates casting and conditions
    values = ["1", "2", "three", "4"]
    for val in values:
        try:
            num = int(val)
            if num % 2 == 0:
                print(val, "is even")
            else:
                print(val, "is odd")
        except ValueError:
            print(val, "is not a number")

    # Another dummy function with syntax error
    def broken_function(x):
        # Intentionally missing return statement and colon
        if x > 0:
            print("Positive number")
        else:
            print("Non-positive")

    broken_function(10)

if __name__ == "__main__":
    main()
