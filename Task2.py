import math

def calculate_math_functions():

    try:
        number = float(input("Enter a number: "))

        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)

        print(f"Square root: {square_root}")
        print(f"Natural logarithm: {natural_log}")
        print(f"Sine (radians): {sine_value}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    calculate_math_functions()