#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 26th, 2023
# this program calculates the base and height of the triangle using
# a function with parameters.
def calc_area(base: float, height: float) -> None:
    # checking if the base and height are positive numbers
    if base <= 0 or height <= 0:
        print("Invalid input. Base and height must be positive numbers.")
        return

    # calculating the area of the triangle using the formula: (base * height) / 2
    area = (base * height) / 2

    # display the calculated area
    print(
        f"The area of the triangle with base {base} cm and height {height} cm is {area} cm^2."
    )


def main():
    try:
        # getting the user input for base and height
        base = float(input("Enter the base of the triangle in cm: "))
        height = float(input("Enter the height of the triangle in cm: "))

        # calling the calc_area function with the user input
        calc_area(base, height)
    # invalid input response to user
    except ValueError:
        print("Invalid input. Base and height must be numeric values.")


if __name__ == "__main__":
    main()
