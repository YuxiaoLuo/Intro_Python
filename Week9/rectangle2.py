# rectangle2.py
def area(width, length):
    return width*length

# the perimeter function accepts a rectangle's width 
# and length as arguments and returns the perimeter
def perimeter(width, length):
    return 2*(width + length)

# main used to test other functions
def main():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print('The area is', area(width, length))
    print('The perimeter is', perimeter(width, length))

# call the main only if run as standalone program
if __name__ == '__main__':
    main()