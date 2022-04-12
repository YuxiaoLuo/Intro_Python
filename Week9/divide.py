# define main function
def main():
    # get two numbers from user
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    
    # call the divide function
    quotient = divide(num1, num2)
    
    # display the result 
    if quotient is None: 
        print('Cannot divide by zero.')
    else: 
        print(f'{num1} divided by {num2} is {quotient}.')
        
# define divide function
def divide(num1, num2):
    if num2 == 0:
        result = None
    else: 
        result = num1/num2
    return result

# run this program either standalone or as module
if __name__ == '__main__':
    main()