'''for i in range(1, 5):
    print(i)'''


def multiplication_table(num):
    print(f"Table of {num} is ")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

number= int(input("Enter a number: "))
multiplication_table(number)

