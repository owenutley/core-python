"""Restaurant rating lister."""

scores = open("scores.txt", "r")
scores = scores.readlines()
scores.sort()

dictionary = {}

for i in scores:
    i = i.rstrip().split(":")
    dictionary[ str(i[0]) ] = str(i[1])
    # print(score)
print(dictionary)

for i in dictionary:
        print(i, "is rated at", dictionary[i])

print("We would love for you to rate a new restaurant for our list!")
new_restaurant = str(input("(place restaurant name here)"))
new_rating = str(input("(rate your restaurant here"))

dictionary[new_restaurant] = new_rating

sorted_dictionary = {}

for i in sorted(dictionary):
   sorted_dictionary[i] = dictionary[i]
print(sorted_dictionary)