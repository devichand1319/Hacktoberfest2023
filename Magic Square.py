def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-sized magic squares are supported")

    magic_square = [[0] * n for _ in range(n)]
    row, col = 0, n // 2

    for num in range(1, n * n + 1):
        magic_square[row][col] = num
        row -= 1
        col += 1

        if num % n == 0:
            row += 2
            col -= 1
        elif row < 0:
            row = n - 1
        elif col == n:
            col = 0

    return magic_square

def print_magic_square(magic_square):
    n = len(magic_square)
    for row in range(n):
        for col in range(n):
            print(f"{magic_square[row][col]:2d}", end=" ")
        print()

if __name__ == "__main__":
    n = 3  # Change this to create a different-sized magic square (must be odd)
    if n % 2 == 0:
        print("Only odd-sized magic squares are supported.")
    else:
        magic_square = generate_magic_square(n)
        print(f"Magic Square of Size {n}x{n}:")
        print_magic_square(magic_square)
