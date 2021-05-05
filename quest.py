user_name = input("Hello! What's your name? ")

#String Concatenation
print("Hello " + user_name + "!")
user_quest = input("What is your quest young traveler? ")

#Another way of doing string concatenations
print(f"So, {user_name}, you're on a quest to {user_quest.lower()}?")

#This transforms a variable into uppercase:
encouragement = "wow that's amazing!"
print(encouragement.upper())


name_of_friend = input("Who are you traveling with? ")
length_of_name = len(name_of_friend)
if length_of_name == 0: 
    length_of_name = input("Please type your friend's name ")
    
# This is string interpolation:
print("Good luck on your quest %s and %s!" % (user_name, name_of_friend))