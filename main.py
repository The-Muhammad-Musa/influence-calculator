import math as ma

'''
Influence Calculator for NationStates. Developed by Hesskin Empire and Volstrostia

The Formula variables are as follows:
e = endos
d = days
c = current influence
t = target nation's influence
k = target nation's endos
s = stabilized (decaying) influence

The Formulas are as follows:
Essentials:
i = 2ed + 2d + c
e = ((i - c) / (2d)) - 1
d = (i - c) / (2e + 2)

Banjections:
RO -> d = (t - c) / (2k - 2e)
WAD -> d = (t - 2c) / (-2k + 4e + 2)

Decay:
s = 360e + 360
e = (s / 360) - 1
'''


def calculate_inf():
    endorsements = int(input("Please enter the amount of endorsements on the nation: "))
    days = float(input("Please enter the amount of days: "))
    current = int(input("Please enter the current total influence: "))
    influence = (2 * endorsements * days) + (2 * days) + current
    print(f"The total influence on a nation with {endorsements}e in {days} days is {influence}.")


def calculate_end():
    influence = int(input("Please enter the target amount of influence: "))
    days = float(input("Please enter the amount of days: "))
    current = int(input("Please enter the current total influence: "))
    endorsements = ((influence - current) / (2 * days)) - 1
    print(f"The amount of endorsements needed to get {influence} influence in {days} days is {endorsements}.")


def calculate_day():
    endorsements = int(input("Please enter the amount of endorsements on the nation: "))
    influence = int(input("Please enter the target amount of influence: "))
    current = int(input("Please enter the current total influence: "))
    days = (influence - current) / (2 * endorsements + 2)
    print(f"The amount of days to get {influence} influence with {endorsements}e is {days}.")


def calculate_rob():
    endorsements = int(input("Please enter the amount of endorsements on the nation: "))
    current = int(input("Please enter the current total influence: "))
    t_endorsements = int(input("Please enter the amount of endorsements on the nation: "))
    t_current = int(input("Please enter the current total influence: "))
    days = (t_current - current) / (2 * t_endorsements - 2 * endorsements)
    print(f"The amount of days for the BCRO to ban the target nation is {days}.")


def calculate_wdb():
    endorsements = int(input("Please enter the amount of endorsements on the nation: "))
    current = int(input("Please enter the current total influence: "))
    t_endorsements = int(input("Please enter the amount of endorsements on the nation: "))
    t_current = int(input("Please enter the current total influence: "))
    days = (t_current - 2 * current) / (-2 * t_endorsements + 4 * endorsements + 2)
    print(f"The amount of days for the WAD to ban the target nation is {days}.")


def calculate_stb():
    stable = int(input("Please enter the stable influence you want to gain in 6 months: "))
    endorsements = ma.ceil(stable / 360) - 1
    print(f"The endorsement count needed to have a total of {stable} inf is {endorsements}.")


def calculate_sen():
    endorsements = int(input("Please enter the total endorsements on the nation: "))
    stable = 360 * endorsements + 360
    print(f"The stable influence after six months with {endorsements} endorsements is {stable}.")


def main():
    print("Hello! Welcome and thank you for using our influence calculator!")
    print("There are currently 7 mathematical operations to choose from, they are as follows (enter 3 letter code):")
    print("Calculate total influence after certain amount of days with a certain amount of endorsements. (INF)")
    print("Calculate how many endorsements are needed to hit an amount of total influence in an amount of days. (END)")
    print("Calculate how many days are needed to hit an amount of total influence with provided endorsements. (DAY)")
    print("How many days it will take for RO to banject a nation with provided endorsements and total influence. (ROB)")
    print("How many days it will take for WAD to banject a nation with provided endorsements and total influence. (WDB")
    print("The total amount of influence that will stabilize in a region with decaying influence. (STB)")
    print("How many endorsements are needed to hit a specific stabilized influence. (SEN)")
    answer = str(input("Please enter the 3 letter code or 'exit' to exit: ")).lower()
    while answer != 'exit':
        if answer == "inf":
            calculate_inf()
        elif answer == "end":
            calculate_end()
        elif answer == "day":
            calculate_day()
        elif answer == "rob":
            calculate_rob()
        elif answer == "wdb":
            calculate_wdb()
        elif answer == "stb":
            calculate_stb()
        elif answer == "sen":
            calculate_sen()
        else:
            print(f"I am sorry but {answer} is not a valid entry.")
        answer = str(input("Please enter the 3 letter code or 'exit' to exit: ")).lower()
    else:
        print("Thank you for using our influence calculator!")


if __name__ == "__main__":
    main()
