"""Restaurant rating lister."""

import random

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
    new_restaurant = str(input("(place restaurant name here)")).capitalize()
    new_rating = 0
    while new_rating < 1 or new_rating > 5:
        new_rating = int(input("(rate your restaurant out of 5)"))
        if new_rating < 1 or new_rating > 5:
            print("You must use a number from 1 to 5")

    dictionary[new_restaurant] = new_rating

    sorted_dictionary = {}

    for i in sorted(dictionary):
        sorted_dictionary[i] = dictionary[i]
        print(i, "is rated at", sorted_dictionary[i])

def update():
    num = random.randrange(0, len(dictionary))
    new_value = list(dictionary.items())
    str = new_value[num]

    # print(dictionary.values()[num])
    

while user_input != "quit":
    user_input = input("To see restaurants and their ratings, type : see\n"
        "To add a new restaurant and rating type : add\n"
        "To update the rating of a random restaurant type : update\n"
        "To quit type : quit\n")

    if user_input == "see":
        see()
    if user_input == "add":
        add()
    if user_input == "update":
        update()
