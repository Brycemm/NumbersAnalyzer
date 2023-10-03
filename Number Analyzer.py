# dunder
if __name__ == "__main__":
    # user data
    name = (input("What is your name? "))

# start of loop
    keep_running = True
    while keep_running:

        num = int((input("Hello, " + name + ", enter a number including or between 1-100: ")))

    # first condition odd and between 59-1
        if num < 60 and num % 2 != 0:
            print(str(num) + " Odd and less than 60.")
    # 2nd condition even and between 1-25
        elif num in range(1, 25) and num % 2 == 0:
            print(str(num) + " Even and less than 25.")
    # 3rd condition even and between 26-60
        elif num in range(25, 61) and num % 2 == 0:
            print(str(num) + " Even and between 26 and 60 inclusive.")
    # 4th condition even and between 60-100
        elif num in range(60, 101) and num % 2 == 0:
            print(str(num) + " Even and greater than 60.")
    # 5th condition odd and between 60-100
        elif num in range(60, 101) and num % 2 != 0:
            print(str(num) + " Odd and greater than 60.")
        # loop response
        response = input("Do you want to continue? y/n ")
        if response == 'y':
            keep_running = True
        elif response == 'n':
            keep_running = False
