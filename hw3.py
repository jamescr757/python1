# import math 

# 1. Find the smallest number 
# def smallest(num_list):
#     smallest_num = math.inf
#     for num in num_list:
#         if num < smallest_num:
#             smallest_num = num
#     return smallest_num

# 2. Find the largest number
# def largest(num_list):
#     largest_num = -math.inf
#     for num in num_list:
#         if num > largest_num:
#             largest_num = num
#     return largest_num

# 3. Find the shortest string
# takes in a list of strings 
# returns the shortest string
# def shortest(string_list):
#     shortest_string_length = math.inf
#     shortest_string = ""
#     for string in string_list:
#         if len(string) < shortest_string_length:
#             shortest_string_length = len(string)
#             shortest_string = string
#     return shortest_string
# print(shortest(["hello", "abc", "james", "ee"]))

# 4. Find the longest string 
# def longest(string_list):
#     longest_string_length = -math.inf
#     longest_string = ""
#     for string in string_list:
#         if len(string) > longest_string_length:
#             longest_string_length = len(string)
#             longest_string = string
#     return longest_string
# print(longest(["hello", "abc", "jamesr", "ee"]))

