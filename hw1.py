# 1.
# name = input("What is your name? ")
# print(f"Hello, {name}!")

# 2. 
# name = input("WHAT IS YOUR NAME? ") 
# print(f'HELLO, {name.upper()}!')
# print(f'YOUR NAME HAS {len(name)} LETTERS IN IT! AWESOME!')

# 3. 
# print('Please fill in the blanks below:')
# print("____(name)____'s favorite subject in school is _____(subject)______.")
# name = input("What is name? ")
# subject = input("What is subject? ")
# print(f"{name}'s favorite subject in school is {subject}.")

# 4. 
# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sunday')
# elif day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")

# 5. 
# day = int(input("Day (0-6)? "))
# if day == 0 or day == 6:
#     print("Sleep in")
# elif 0 < day < 6:
#     print("Go to work")


# 6. 
# temp_c = int(input("Temperature in C? "))
# temp_f = (temp_c * (9 / 5)) + 32
# print("%.1f F" % temp_f)

# 7.
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1

# 8. 
# starting_value = int(input("Start from: "))
# ending_value = int(input("End on: "))
# while starting_value <= ending_value:
#     print(starting_value)
#     starting_value += 1

# 9. 
# counter = 1
# while counter <= 5:
#     print('*****')
#     counter += 1

# 10.
# size_of_square = int(input("How big is the square? "))
# counter1 = 1
# while counter1 <= size_of_square:
#     counter2 = 1
#     stars = ""
#     while counter2 <= size_of_square:
#         stars += "*"
#         counter2 += 1
#     print(stars)
#     counter1 += 1


# Medium

# 1. 
# bill_amount = float(input("Total bill amount? "))
# level_of_service = input("Level of service? ").lower().strip()
# if level_of_service == "good":
#     tip_amount = bill_amount * 0.2
# elif level_of_service == "fair":
#     tip_amount = bill_amount * 0.15
# elif level_of_service == 'bad':
#     tip_amount = bill_amount * 0.1
# total = bill_amount + tip_amount
# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)

# 2. 
# bill_amount = float(input("Total bill amount? "))
# level_of_service = input("Level of service? ").lower().strip()
# number_of_splits = int(input("Split how many ways? "))

# if level_of_service == "good":
#     tip_amount = bill_amount * 0.2
# elif level_of_service == "fair":
#     tip_amount = bill_amount * 0.15
# elif level_of_service == 'bad':
#     tip_amount = bill_amount * 0.1

# total = bill_amount + tip_amount
# total_per_person = total / number_of_splits

# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)
# print("Amount per person: $%.2f" % total_per_person)

# 3. 
# answer = ""
# num_of_coins = 0
# while answer != "no":
#     print(f"You have {num_of_coins} coins.")
#     answer = input("Do you want another? ")
#     num_of_coins += 1
# print("Bye")

# 4. 
# width = int(input("Width? "))
# height = int(input("Height? "))
# counter1 = 1
# while counter1 <= height:
#     counter2 = 1
#     stars = ""
#     while counter2 <= width:
#         if counter1 == 1 or counter1 == height:
#             stars += "*"
#         else:
#             if counter2 == 1 or counter2 == width:
#                 stars += "*"
#             else:
#                 stars += " "
#         counter2 += 1
#     print(stars)
#     counter1 += 1


# count = 1
# down = 3

# while count < 9:
#     print((down * " ") + (count * '*'))
#     down-=1
#     count+=2

# 5. 
# triangle_height = int(input("Please input height of triangle: "))
# counter = 1
# spaces = triangle_height - 1
# while counter <= triangle_height * 2:
#     print((spaces * " ") + counter * "*")
#     spaces -= 1
#     counter += 2

# 6. 
# counter1 = 1
# while counter1 <= 10:
#     counter2 = 1
#     while counter2 <= 10:
#         print(f"{counter1} X {counter2} = {counter1 * counter2}")
#         counter2 += 1
#     counter1 += 1


# Large 

# 3. Guess a Number 
# import random

# playing = True
# while playing:
#     print("I'm thinking of a number between 1 and 10.") 
#     secret_number = random.randint(1, 10)
#     guessed_number = ""
#     number_of_guesses = 5
#     while secret_number != guessed_number and number_of_guesses > 0:
#         print(f"You have {number_of_guesses} guesses left.")
#         guessed_number = int(input("What's the number? "))
#         if guessed_number < secret_number:
#             print(f"{guessed_number} is too low.")
#         elif guessed_number > secret_number:
#             print(f"{guessed_number} is too high.")
#         number_of_guesses -= 1

#     if secret_number == guessed_number:
#         print("Yes! You win!")
#     else:
#         print("You ran out of guesses!")
    
#     play_again = input("Do you want to play again (Y or N)? ").upper().strip()
#     if play_again == "N":
#         playing = False
        
# print("Bye!")