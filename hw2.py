# 1. create a list of numbers, print their sum
# nums = [12, 3, 4, 93, 83]
# print(sum(nums))
# sum = 0
# for num in nums:
#     sum += num
# print(sum)

# 2. Largest Number
# create a list of numbers, print the largest number


# nums = [12, 3, 4, 93, 83]
# nums.sort()
# print(nums[-1])
# max_num = 0
# for num in nums:
#     if num > max_num:
#         max_num = num
# print(max_num)

# 3. smallest number
# Create a list of numbers, print the smallest number
# import math
# nums = [12, 3, 4, 93, 83]
# # nums.sort()
# # print(nums[0])
# min_num = math.inf
# for num in nums:
#     if num < min_num:
#         min_num = num
# print(min_num)

# 4. Even numbers
# create a list of numbers, print each number that is even 
# nums = [12, 3, 4, 93, 83]
# for num in nums:
#     if num % 2 == 0:
#         print(num)

# 5. positive numbers
# create a list of numbers, print each number that is greater than zero 
# nums = [12, -3, -2, 3, 4, 93, 83]
# for num in nums:
#     if num > 0:
#         print(num)

# 6. positive numbers II
# create a list of numbers, create a new list which contains every number in the given list which is positive 
# nums = [12, -3, -2, 3, 4, 93, 83]
# positive_nums = [num for num in nums if num > 0]
# positive_nums = []
# for num in nums:
#     if num > 0:
#         positive_nums.append(num)
# print(positive_nums)

# 7. multiply a list
# create a list of numbers and a single factor
# create a new list that is the element multiplied by the factor
# nums = [12, -3, -2, 3, 4, 93, 83]
# factor = 3
# multiplied_nums = [num * factor for num in nums]
# multiplied_nums = []
# for num in nums:
#     multiplied_nums.append(num * factor)
# print(multiplied_nums)

# 8. reverse a string
# given a string, print the string reversed
# string = input("Please input some text: ")
# print("".join(reversed(string)))
# reversed_string = reversed(string)
# print("".join(reversed_string))
# reversed_string = ""
# for index in range(len(string) - 1, -1, -1):
#     reversed_string += string[index]
# print(reversed_string)


# Medium Problems 


# 1. multiply vectors 
# given two lists of numbers that are same length, create a new list by multiplying the two lists together 
# nums1 = [2, 4, 5]
# nums2 = [2, 3, 6]
# multiplied_nums = []
# for index in range(len(nums1)):
#     multiplied_nums.append(nums1[index] * nums2[index])
# print(multiplied_nums)

# 2. and 3. Matrix addition I and II
# calculate result of adding 2 matrices of same size 
# matrix1 = [[1, 3, 5], [2, 4]]
# matrix2 = [[5, 2, 3], [1, 0]]
# new_matrix = []
# for row in range(len(matrix1)):
#     new_matrix.append([])
#     for column in range(len(matrix1[row])):
#         new_matrix[row].append(matrix1[row][column] + matrix2[row][column])
# print(new_matrix)

# 4. De-dup
# remove duplicate items from a list and print it 
# my_list = ["the", "cat", "ran", "over", 3, "over", 3, "dog", "cat", 1]
# print(list(set(my_list)))
# my_dict = {}
# for element in my_list:
#     my_dict.update({element: True})
#     my_dict[element] = True
# new_list = list(my_dict)
# print(new_list)

# 5. Leetspeak 
# string = input("Enter text to be translated: ")
# translate_list_letters = ["A", "E", "G", "I", "O", "S", "T"]
# translate_list_nums = ["4", "3", "6", "1", "0", "5", "7"]
# new_string = ""
# for index, letter in enumerate(string):
#     char = letter.upper()
#     try:
#         letter_index = translate_list_letters.index(char)
#         new_string += translate_list_nums[letter_index]
#     except ValueError:
#         new_string += letter
# print(new_string)

# 5. Leetspeak 
# another method using a dictionary to hold translation 
# string_list = list(input("Enter text to be translated: "))
# translator = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "T": "7"}
# for index, letter in enumerate(string_list):
#     char = letter.upper()
#     if char in translator:
#         string_list[index] = translator[char]
# print("".join(string_list))

# string = input("Enter text to be translated: ")
# translator = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "T": "7"}
# new_string = ""
# for index, letter in enumerate(string):
#     char = letter.upper()
#     if char in translator:
#         new_string += translator[char]
#     else:
#         new_string += letter
# print(new_string)

# 6. Long-long vowels
# extend long-vowels to a length of 5 
# word = input("Enter a word: ")
# new_word = ""
# for index in range(len(word)):
#     if index < len(word) - 1 and word[index] in "aeoiu": 
#         if word[index + 1] in "aeoui":
#             new_word += word[index] * 5
#         elif index < len(word) - 2 and word[index + 2] in "aoeui":
#             new_word += word[index] * 5
#         else:
#             new_word += word[index]
#     else:
#         new_word += word[index]
# print(new_word)

# 7. Caesar Cipher 
# given an encrypted string, return the deciphered text 
# shift the letters by 13 
# a to z unicode values go from 97 to 122
# encrypted_string = list(input("Encrypted text: "))
# key = int(input("Enter encryption key value: "))
# for index, char in enumerate(encrypted_string):
#     unicode_value = ord(char)
#     if unicode_value == 32:
#         continue
#     new_value = unicode_value + key
#     while new_value < 97 or new_value > 122:
#         if new_value < 97:
#             new_value += 26 
#         elif new_value > 122:
#             new_value -= 26
#     encrypted_string[index] = chr(new_value)
# print("".join(encrypted_string))