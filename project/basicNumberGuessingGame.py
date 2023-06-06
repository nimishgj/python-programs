from random import choice as cho

num = []
for i in range(0, 100):
    num.append(i)
comp_choice = cho(num)
last = len(num) - 1
user_choice = []
points = 10
print("\n\n" + "." * 20 + "NUMBER GUESSING GAME" + "." * 20 + "\n" + "RULES:-" + "")
print(
    "Initially 10 Points are awarded.\nFor each wrong guess 1 Point is deducted.\nGAME OVER at 0 Points.\n\n" + "GOOD LUCK" + "\n(●'◡'●) \n")
print(f"Enter a number Between {num[0]} and {num[last]}")
uchoice = int(input("->"))
user_choice.append(uchoice)
for i in user_choice:
    if uchoice == comp_choice:
        print("Correct Guess.\n\n¯\_(ツ)_/¯\n")
        print("Thank you for Playing")
        print("\n\n")

    elif uchoice > comp_choice:
        print("Oops number is too big! \n Points deducted.")
        uchoice = int(input("Enter your choice again:"))
        points -= 1
        print("\n\n")
        user_choice.append(uchoice)

    elif uchoice < comp_choice:
        print("Oops number is too small! \nPoints deducted.")
        uchoice = int(input("Enter your choice again:"))
        print("\n\n")
        points -= 1
        user_choice.append(uchoice)

print(f"Total Points -->{points}. \nCongratulation")
