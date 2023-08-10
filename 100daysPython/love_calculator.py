# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

# Count number of times the letters "T" "R" "U" "E" appears in name1 and name2
#name1
t = lower_name1.count("t")
r = lower_name1.count("r")
u = lower_name1.count("u")
e = lower_name1.count("e")
true_name1 = t+r+u+e
#print(f"true in name1 is {true_name1}")
#name2
t = lower_name2.count("t")
r = lower_name2.count("r")
u = lower_name2.count("u")
e = lower_name2.count("e")
true_name2 = t+r+u+e
#print(f"true in name2 is {true_name2}")

#calculate true score
true_score  = int(true_name1) +int(true_name2)
#print(f"your true score is {true_score}")

# Count number of times the letters "L" "O" "V" "E" appears in name1 and name2
#name1
l = lower_name1.count("l")
o = lower_name1.count("o")
v = lower_name1.count("v")
e = lower_name1.count("e")
love_name1 = l+o+v+e
#print(f"love in name1 is {love_name1}")

#name2
#name2
l = lower_name2.count("l")
o = lower_name2.count("o")
v = lower_name2.count("v")
e = lower_name2.count("e")
love_name2 = l+o+v+e
#print(f"love in name2 is {love_name2}")

#calculate love score
love_score  = int(love_name1) +int(love_name2)
#print(f"your true score is {love_score}")

#calculate final score
your_score = str(true_score) + str(love_score)
print(f"your score is **{your_score}**")

if int(your_score) < 10 or int(your_score) >90:
    print(f'"Your score is **{your_score}**, you go together like coke and mentos."')
elif int(your_score) >= 40 and int(your_score) <= 50:
    print(f'"Your score is **{your_score}**, you are alright together."')
else:
    print(f'"Your score is **{your_score}**."')
