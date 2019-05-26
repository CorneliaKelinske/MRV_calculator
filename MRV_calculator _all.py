
gender = input("What is your gender? [m/f] ")
weight = int(input("What is your weight in pounds? [number only] "))
height = int(input("How tall are you in cm? [number only] "))
exp = int(input("For how many years have you been strength training? [number only] "))
age = int(input("How old are you? [number only] "))
diet = input("How is your diet? \na: poor \nb: average \nc: good \n[a b or c] ")
sleep = int(input("How many hours of sleep do you usually get? [number only] "))
stress = input("How much stress do you experience in your daily life? \na: a lot \nb: average \nc: not much \n[a b or c] ")
recov = input("How is your recovery?  \na: poor \nb: average \nc: good \n [a b or c] ")

MRV_av = {"Squat:" : 13, "Bench:" : 17, "Deadlift:" : 9}

print("Your MRVs are as follows:")

for lift, MRV in MRV_av.items():
    if gender == "f":
        MRV +=5
    else:
        MRV = MRV

    if weight < 148:
        MRV += 4
    elif weight in range(148, 165):
        MRV += 2
    elif weight in range(165,221):
        MRV -=2
    else:
        MRV -=4

    if height < 160:
        MRV += 2
    elif height in range (160,176):
        MRV += 1
    elif height in range (176, 191):
        MRV -= 1
    else:
        MRV -=2

    if exp < 4 or exp in range (9, 13):
        MRV = MRV
    elif exp in range (4, 9):
        MRV += 2
    else:
        MRV -= 2

    if age < 19:
        MRV += 2
    elif age in range (19, 30):
        MRV += 1
    elif age in range (30, 40):
        MRV = MRV
    elif age in range (40, 50):
        MRV -= 2
    else:
        MRV -=4

    if diet == "a":
        MRV -= 3
    elif diet == "b":
        MRV = MRV
    else:
        MRV += 1

    if sleep < 6:
        MRV -= 3
    elif sleep > 8:
        MRV += 1
    else:
        MRV = MRV

    if stress == "a":
        MRV -= 3
    elif stress == "b":
        MRV = MRV
    else:
        MRV += 1

    if recov == "a":
        MRV -= 3
    elif recov == "b":
        MRV = MRV
    else:
        MRV += 1
    
    print(lift, MRV)