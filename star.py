def generate_diamond(rows):
    """
    Generates a diamond-shaped pattern of asterisks.

    Args:
        rows (int): The number of rows in the top half of the diamond.
                    The total number of rows will be (2 * rows) - 1.
    """
    if rows <= 0:
        print("Number of rows must be a positive integer.")
        return

    # Upper half of the diamond (including the middle row)
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print asterisks
        print("* " * i)

    # Lower half of the diamond
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print asterisks
        print("* " * i)

# Example usage with input from the user:
if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows for the top half of the diamond: "))
        generate_diamond(num_rows)
    except ValueError:
        print("Invalid input. Please enter an integer.")