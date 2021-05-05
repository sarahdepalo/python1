print("""Please fill in the blanks below:
___(name)___'s favorite subject in school is ___(subject)__""")

user_name = input("What's your name? ")
user_subject = input("What's your favorite subject? ")

print("%s's favoirte subject in school is %s." % (user_name, user_subject))


print("Let's play again!")
verb1 = input("Pick a verb in the past tense ")
adj1 = input("Pick an adjective ")
adverb1 = input("Pick an adverb ")
noun1 = input("Pick a noun ")

print(f"The {adj1} {noun1} {adverb1} {verb1}. ")


 # Asks for name and capitalizes the whole statement
user_name = input("what's your name?")
upper_case = ("Nice to meet you  %s" % (user_name))
print(upper_case.upper())