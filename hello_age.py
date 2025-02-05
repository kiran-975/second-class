#age

name = input("Whats your name?\n")

year_now = int(input("What year is it today?\n"))
year_born = int(input("And what year you were born?\n"))

age = year_now - year_born

print(f"hello,{name}.you will be {age} by today.")