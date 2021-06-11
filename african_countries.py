import numpy as np
import random

# Reading the csv file using numpy getfromtxt method
countries_file = np.genfromtxt("african_countries.csv", delimiter=",", dtype="U", autostrip=True)

#print(dir(countries_file))
#print(countries_file.ndim, countries_file.size, countries_file.shape)

# Creating a list of countries
countries = [x[0] for x in countries_file]

# Creating a list of capitals
capitals = [x[1].lower() for x in countries_file]
capitals = [x.replace(' * ', '*').split('*') if '*' in x else x for x in capitals]

# Determining the total number of country entries
AFRICAN_COUNTRIES_COUNT = countries_file.shape[0]

# Initializing the counter loop
COUNTER = 10

# All answer entries are collected here
capital_cities_answers_list = []

# list where generated random numbers are entered
random_number_list = []

# Function to generate random numbers for the loop
def generate_random_numbers():
    return random.randint(0, AFRICAN_COUNTRIES_COUNT)

print("African Capital Game: Have Fun!")
print("Press ENTER after each input")

# Start the game
while COUNTER:
    random_number = generate_random_numbers()

    # If the random number has been generated before, regenerate another one
    while random_number in random_number_list:
        random_number = generate_random_numbers()
    
    # Input from user
    entered_input = input("What is the capital of " + countries[random_number] + ": ")

    # Append random number generated to random_number list
    random_number_list.append(random_number)

    # Append the entered input to capital_cities_answers_list list
    capital_cities_answers_list.append(entered_input.lower())

    # Decrease counter
    COUNTER = COUNTER - 1

# Picking out the index numbers of multi-capital cities
MULTIPLE_CAPITALS = [capitals.index(x) for x in capitals if type(x) ==  type([])]
#print("Multiple capitals is: ", MULTIPLE_CAPITALS)

CORRECT_ANSWERS = 0

# Loop through the answers given and the corresponding index of the countries
for capital_city, random_no in zip(capital_cities_answers_list, random_number_list):
    # Check if it is a multi-capital city
    if random_no in MULTIPLE_CAPITALS:
        for c in capitals[random_no]:
            if capital_city == c:
                CORRECT_ANSWERS = CORRECT_ANSWERS + 1
                break      
    else:
        if capital_city == capitals[random_no]:
            CORRECT_ANSWERS = CORRECT_ANSWERS + 1

print("Total Score = ", CORRECT_ANSWERS * 5, "/", 50)