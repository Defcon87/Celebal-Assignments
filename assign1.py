def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

# Example usage
print("Lower Triangular:")
lower_triangular(5)

print("\nUpper Triangular:")
upper_triangular(5)

print("\nPyramid:")
pyramid(5)
