"""Restaurant rating lister."""

scores = open("scores.txt", "r")
scores = scores.readlines()
scores.sort()

user_input = ""


dictionary = {}


for i in scores:
    i = i.rstrip().split(":")
    dictionary[ str(i[0]) ] = str(i[1])
    # print(score)



def see():
    for i in dictionary:
        print(i, "is rated at", dictionary[i])


def add():
    new_restaurant = str(input("(place restaurant name here)"))
    new_rating = 0
    while new_rating < 1 or new_rating > 5:
        new_rating = int(input("(rate your restaurant out of 5)"))
        if new_rating < 1 or new_rating > 5:
            print("You must use a number from 1 to 5")

    dictionary[new_restaurant] = new_rating

    sorted_dictionary = {}

    for i in sorted(dictionary):
        sorted_dictionary[i] = dictionary[i]

    print(sorted_dictionary)

    for i in sorted_dictionary:
        print(i, "is rated at", sorted_dictionary[i])

while user_input != "quit":
    user_input = input("If you want to see restaurants and their ratings type : see\n"
        "If you want to add a new restaurant and rating type : add\n"
        "If you want to quit type : quit\n")

    if user_input == "see":
        see()
    if user_input == "add":
        add()