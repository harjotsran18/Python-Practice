#exception handling

try:
    #code that raise an exception
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result:",result)
except ValueError:
    print("Invalid input! Plese enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An unexpected error occured:" , e)
