#Python Basics Exercises

#1. Simple Message
msg="This is a simple message."
print(msg)
print("\n")

#2. Simple Messages
msg_1="This is a simple msg_1"
print(msg_1)
print("\n")

#3. Personal Message
person="“Hello Eric, would you like to learn some Python today?"
print(person)
print("\n")

#4. Name Cases
person_name="Afia"
person_name_title=person_name.title()
person_name_lower=person_name.lower()
person_name_upper=person_name.upper()
print(person_name_title,person_name_lower,person_name_upper)
print("\n")

#5. Famous Quote
author="Bruce Lee"
quote='"A wise man can learn more from a foolish question than a fool can learn from a wise answer."'
print("{} once said,{}".format(author,quote))
print("\n")

#6. Famous Quote 2
famous_person="Bruce Lee"
message='{} once said,"A wise man can learn more from a foolish question than a fool can learn from a wise answer."'.format(famous_person)
print(message)
print("\n")

#7. Stripping Names
prsn_name="\t\n Afia \t\n"
print("person name with spaces=",prsn_name)
print("Person name without leading whitespaces=",prsn_name.lstrip())
print("Person name without  trailing whitespaces=",prsn_name.rstrip())
print("Person name without  whitespaces=",prsn_name.strip())
print("\n")

#8. Variable Sum
x=5
y=10
z=15
sum=x+y+z
print("The sum is=",sum)
print("\n")

#9. Variable Swap
a,b=1,2
print('Before swap, a={}\tb={}'.format(a,b))
a,b=b,a
print("After swap, a={}\tb={}".format(a,b))
print("\n")

#10. Favorite Color
fav_clr_1="Purple"
print(fav_clr_1)
clr=fav_clr_1
print(clr)
print("\n")

#11. Changing Pet Name
pet_name="Buddy"
print("The pet name is=",pet_name)
pet_name="Max"
print("The new pet name is=",pet_name)
print("\n")



#13. Reassigning Score
initial_score=100
print("The initial score is",initial_score)
final_score=200
print("The final score is",final_score)
print("\n")

#14. City Name
city="Islamabad"
print("The name of city is",city)
print("\n")

#15. Title Case Text
text="python programming"
text_title_case=text.title()
print(text_title_case)
print("\n")

#16. Lowercase Conversion
string="tODayIsMONday"
string_lower_case=string.lower()
print(string_lower_case)
print("\n")

#17. Uppercase Conversion
string_1="tODayIsMONday"
string_upper_case=string.upper()
print(string_upper_case)
print("\n")

#18. Current Temperature
temperature=25
print("The current temperature is {}".format(temperature))
print("\n")

#19. Printing a Poem

#triple quotes for multiline strings
poem="""Beneath a sky where shadows weave,
        Majesty and power breathe,
        In twilight’s shroud,
        the stars proclaim,Mysteries whispered in their flame."""
print(poem)
print("\n")

#12. Observing Name Error
sunshine="Sunshine"
print("The correct variable name=",sunshine)
print("The wrong variable name=",sunsine)