from termcolor import *


def pcm(msg, color):  # print colored message
    print(colored(msg, color))


pemberatAndMarks = {
    "bm": [6, "x"],
    "eng": [5, "x"],
    "chn": [7, "x"],
    "mm": [5, "x"],
    "sc": [5, "x"],
    "rbt/ask": [4, "x"],
    "sjh": [3, "x"],
    "geo": [3, "x"],
    "cocurriculum": [3, "x"],
}
purata = 0
total_marks_with_pemberat = 0
total_pemberat = 0
x_pemberat_counter = 0

print("Don't waste time on calculator lol")
print("\nIf it is not out type x, if the marks are invalid it will result to x which is not counted")

for subject in pemberatAndMarks:
    try:

        inp = float(input(f"Your {subject} marks: "))
        if 0 <= inp <= 100:
            pemberatAndMarks[subject][1] = inp
    except:
        pass


for subject in pemberatAndMarks:
    if pemberatAndMarks[subject][1] == "x":
        x_pemberat_counter += pemberatAndMarks[subject][0]
    else:
        total_marks_with_pemberat += pemberatAndMarks[subject][1] * pemberatAndMarks[subject][0]
        total_pemberat += pemberatAndMarks[subject][0]

print("\n")

if total_pemberat == 0:
    print("Bruh where your results")
else:
    purata = total_marks_with_pemberat / total_pemberat
    purata_message = "Your 总平均 is {:0.3f}".format(purata)

    if purata >= 60:
        pcm(purata_message, "green")
    else:
        pcm(purata_message, "red")

if x_pemberat_counter != 0:
    print("Type y if you want to or x to quit")
    continue_inp = input("Do you want to know how much you need to reach your target: ")

    if continue_inp == "y":
        check_inp = False
        _input = 0
        while not check_inp:
            try:
                _input = int(input("What is your target: "))
                check_inp = True
            except:
                print("Invalid target... Try again-")

        total_target = (_input * 41 - total_marks_with_pemberat) / x_pemberat_counter
        message = "\nFor the remaining papers you must get an average of {:0.2f}".format(total_target)

        if total_target > 100:
            pcm(message, "red")
        elif total_target > 90:
            pcm(message, "yellow")
        elif total_target < 0:
            print("\nAiya set target higher lolo")
            pcm(message, "blue")
        else:
            pcm(message, "green")

