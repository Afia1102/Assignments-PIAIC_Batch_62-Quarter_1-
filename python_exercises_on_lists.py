#python_exercises_on_lists

#Exercise 3-1: Names
names=["Ayesha","Alia","Arshia","Arooj","Alina"]
#print(names[0])
for name in names:
    print(name)
print("\n")

#Exercise 3-2: Greetings
for name in names:
     print("Hello {}!,How are you?".format(name))
print("\n")

#Exercise 3-3: Your Own List
cars=["Lexus LX 600","Mercedes-Benz G-Class","Lamborghini Huracán Sterrato"]
colors=["white","green","black"]
features=["city-driving","off-roading","drifting"]

for index,car in enumerate(cars):
     color=colors[index%len(colors)]
     feature=features[index%len(features)]
     print("I would like to own a {} in {} for {}.".format(car,color,feature))

print("\n")

#Exercise 3-4: Guest List
guests=[" Al-‘Alima al-Baghdadiyya","Ibn Battuta","Ibn Sina"]
for guest in guests:
     print(f"""Dear {guest},
It would be a great pleasure to share an evening with you and engage in delightful conversations.
Please let me know if you are able to join.""")
print("\n")

#