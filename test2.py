number = int(input("Check if number is prime: "))


while True:
    if number > 1:
    
        for i in range(2, number):
            if (number % i) == 0:
                print("Tis a prime num")
                break
            else:
                print("tis not a prime")


