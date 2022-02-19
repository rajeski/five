#Password Generator Mini-project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '-']

print("Welcome to your PyPassword Generator!")
nr_letters= int(input("How many letters would you like to use in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like to use in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like to use in your password?\n"))

#Easy Level, The order of the password is not randomized, e.g., 4 letters, 2 symbols, 2 numbers would equal an output of OkdG#*89