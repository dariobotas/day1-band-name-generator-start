#1. Create a greeting for your program.
print("Welcome to Band Name Generator")
#2. Ask the user for the city that they grew up in.
city_name = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pets_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be "+city_name+" "+pets_name)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("What was the total bill? ")
tip = input("What was the tip you like to give? 10, 12 or 15? ")
number_of_people = input("How many people to split the bill? ")

payment_per_each_person = (bill / number_of_people) * (1 + tip / 100)

print(round(payment_per_each_person, 2))