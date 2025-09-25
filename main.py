import random

def get_random_number(min, max):
    return random.randint(max, min) 

def print_numbers(n):
    for i in range(n):
        print("Number is: " + i)  

def divide(a, b):
    return a / b

def main()
    nums = get_random_number(1, 10) 
    print_numbers(nums)

    result = divide(10,0) 
    print("Wynik dzielenia:", result)

if __name__ == "__main__":
    main()
