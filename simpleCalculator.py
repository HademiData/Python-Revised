def add(*args):
    return sum(args)

def sub(*args):

    result = args[0]
    for num in args[1:]:
        result -=num
    
    return result

def divide(*args):
    result = args[0]

    for num in args[1:]:

        if num == 0 :
            print("division by zero is not allowed")
            return
        else:
            result /= num
    
    return result

def multiply(*args):

    result = 1
    for num in args:
        result *=num
    
    return result

def showOptions():
    print("==================")
    print("SELECT:")
    print("\t1. Add")
    print("\t2. Subtract")
    print("\t3. Divide")
    print("\t4. Multiply")
    print("\t5. Exit")
    print("==================")


def main():

    while True:

        showOptions()

        option = input("Input your option here:")

        if option == 5:
            print("Goodbye")
            break

        if option not in ["1", "2", "3", "4"]:
            print("option not valid")
            continue

        numbers = input("Enter numbers separated by spaces: ")

        try:
            numbers = [float(num) for num in numbers.split()]

        except ValueError:
            print("Please enter valid number")
            continue

        if len(numbers) < 2 :
            print("the number of input must be more than 1")
            continue       

        if option == "1":
            result = add(*numbers)

        elif option == "2":
            result = sub(*numbers)

        elif option == "3":
            result = divide(*numbers)

        elif option == "4":
            result = multiply(*numbers)

        print(f"Result: {result}\n")
                
            
if __name__ == "__main__":
    main()
        

     





