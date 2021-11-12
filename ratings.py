"""Restaurant rating lister."""

import random

scores = open("scores.txt", "r")
scores = scores.readlines()
scores.sort()

user_input = ""


dictionary = {}
sorted_dictionary = {}

for i in scores:
    i = i.rstrip().split(":")
    dictionary[ str(i[0]) ] = str(i[1])
    # print(score)



def see():
    for i in sorted(dictionary):
        sorted_dictionary[i] = dictionary[i]
        print(i, "is rated at", sorted_dictionary[i])


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

def update_random():
    num = random.randrange(0, len(dictionary))
    new_value = list(dictionary.items())
    str = new_value[num]
    new_rating = 0
    print(F"The random restaurant selected is {str[0]} : current rating is {str[1]}")
    while new_rating < 1 or new_rating > 5:
        new_rating = int(input(F"(rate {str[0]} out of 5)"))
        if new_rating < 1 or new_rating > 5:
            print("You must use a number from 1 to 5")


    dictionary[str[0]] = (new_rating)
    
def update():
    restaurant_name = "1l23k4jh"
    
    while not restaurant_name in dictionary:
        for i in sorted(dictionary):
            print(i)
        if not restaurant_name in dictionary and restaurant_name != "1l23k4jh":
            print("You must update a restaurant from the list")
        restaurant_name = input("What restaurant would you like to rate?\n"
            "(Type restaurant name here)")
        if not restaurant_name in dictionary:
            print("You must update a restaurant from the list")
    new_rating = 0
    print(F"Previous rating for {restaurant_name} is {dictionary.get(restaurant_name)}")
    while new_rating < 1 or new_rating > 5:
        new_rating = int(input(F"(Give rating for {restaurant_name} out of 5)"))
        dictionary[restaurant_name] = (new_rating)
        if new_rating < 1 or new_rating > 5:
            print("You must use a number from 1 to 5")



def start():
    global user_input
    while user_input != "quit":
        user_input = input("To see restaurants and their ratings, type : see\n"
            "To add a new restaurant and rating type : add\n"
            "To update the rating of a random restaurant type : random\n"
            "To update the rating of a restaurant fo choice type : update\n"
            "To quit type : quit\n")

        if user_input == "see":
            see()
        if user_input == "add":
            add()
        if user_input == "random":
            update_random()
        if user_input == "update":
            update()
start()