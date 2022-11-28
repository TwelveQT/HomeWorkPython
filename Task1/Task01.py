def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("It's not a number!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print(num, "->Yes")
    elif 0 < num < 6:
        print(num,"-> No")
    else:
        print("It's not a day")


num = InputNumbers("Press number: ")
checkNumber(num)
