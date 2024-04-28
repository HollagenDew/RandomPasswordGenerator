"""
Program name : randomPasswordGeneratator.py
Author       : Prateek Mahadev Waghmare
Written on   : 27-Apr-24 22:00:00 IST
Description  : I am presently engaged in learning Python and have developed this modest code to assess my proficiency 
in Python programming. The program is designed to address fundamental trigonometric problems, and I have endeavored 
to craft it to the best of my abilities. Should you wish to offer corrections or enhancements to this code, your 
input would be welcomed. 
"""

import SLmethod # Created by Prateek Mahadev Waghmare

numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
U_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_char = ("~", "`", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', ",", "<", ">", ".", "/", "\\")

banner = """
 ______                  _             ______                                     _  ______                                              
(_____ \                | |           (_____ \                                   | |/ _____)                             _               
 _____) ) ____ ____   _ | | ___  ____  _____) )___  ___  ___ _ _ _  ___   ____ _ | | /  ___  ____ ____   ____  ____ ____| |_  ___   ____ 
(_____ ( / _  |  _ \ / || |/ _ \|    \|  ____/ _  |/___)/___) | | |/ _ \ / ___) || | | (___)/ _  )  _ \ / _  )/ ___) _  |  _)/ _ \ / ___)
      | ( ( | | | | ( (_| | |_| | | | | |   ( ( | |___ |___ | | | | |_| | |  ( (_| | \____/( (/ /| | | ( (/ /| |  ( ( | | |_| |_| | |    
      |_|\_||_|_| |_|\____|\___/|_|_|_|_|    \_||_(___/(___/ \____|\___/|_|   \____|\_____/ \____)_| |_|\____)_|   \_||_|\___)___/|_|    
                                                                                                                                         
"""

print(banner) # Prints banner i.e. name of the tool

des = """
Type the terms you want in password from following:
  A-Z  a-z  0-9  special

  !!!Note:- special stands for special character  like @, %, $, etc...

For ex:- A-Z a-z special
         0-9 special
"""

print(des) # Prints the description
phrase = input("Enter the terms: ") # Takes the term required for combination

value = input("Enter password length: ")  # Asking for input and converting it to a string

# Error Handler
if value == "":
    print("Please enter some length. It cannot be empty")
    exit()
elif not value.isdigit():
    print(f"You entered a non-numeric value: {value}")
    exit()
elif int(value) < 0:
    print("Please enter a positive value for password length")
    exit()

max = int(value)
repeat = input("Do you want to repeat a term? (Y/n) (default=n): ")

# Error Handling: Setting repeat to default="n"
if repeat == "":
    repeat = "n"
    print("Default set to n.")
elif repeat not in ['Y', 'n']:
    print("Please enter a valid option.")

SLmethod.sec(max, phrase)

L_password = [] # Empty list which will store new generated password in the form of list

if repeat == "Y":
    SLmethod.pass_creator2(max, argument=phrase, L_list=L_password,list1=U_alphabet,list2=l_alphabet,list3=numeric,list4=special_char)
    rm_list = int(len(L_password)/3) # Used  because the length of L_password is getting doubled i.e (length*3)
    counter = rm_list 

    while len(L_password) != rm_list: # Continue removing elements from L_password until it's length is equal to rm_list
        L_password.pop(counter) # removes Extra elements from list
        counter -= 1

    # It is used to convert [['R'], ['e'], [']'], ['P'], ['m'], ['<']] --> ['R', 'e', ']', 'P', 'm', '<']
    # l_password = sum(L_password, [])
    password = ''.join(L_password) # Here list is converted to string i.e ['R', 'e', ']', 'P', 'm', '<'] --> "Re]Pm<"
    print(password)
elif repeat == "n":
    SLmethod.pass_creator(max, argument=phrase, L_list=L_password,list1=U_alphabet,list2=l_alphabet,list3=numeric,list4=special_char) 

    rm_list = int(len(L_password)/3) # Used  because the length of L_password is getting doubled i.e (length*3)
    counter = rm_list 
    
    while len(L_password) != rm_list: # Continue removing elements from L_password until it's length is equal to rm_list
        L_password.pop(counter) # removes Extra elements from list
        counter -= 1

    # It is used to convert [['R'], ['e'], [']'], ['P'], ['m'], ['<']] --> ['R', 'e', ']', 'P', 'm', '<']
    l_password = sum(L_password, [])
    password = ''.join(l_password) # Here list is converted to string i.e ['R', 'e', ']', 'P', 'm', '<'] --> "Re]Pm<"
    print(password)

# # It is used to convert [['R'], ['e'], [']'], ['P'], ['m'], ['<']] --> ['R', 'e', ']', 'P', 'm', '<']
# l_password = sum(L_password, [])
# password = ''.join(l_password) # Here list is converted to string i.e ['R', 'e', ']', 'P', 'm', '<'] --> "Re]Pm<"
# print(password)
