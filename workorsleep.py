day = int(input("Pick a day (0-6): "))
days_of_the_week= ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if day <= 5:
    print(f"Go to work!! It's a {days_of_the_week[day]}!")
else:
    print(f"Sleep in today, it's a {days_of_the_week[day]}!")

