# It is the First Code Testing Sample

import SLmethod # Created by me

numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
U_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_char = ("~", "`", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', ",", "<", ">", ".", "/", "\\")


des = """
Type the terms you want in password from following:
  A-Z  a-z  0-9  special

  !!!Note:- special stands for special character  like @, %, $, etc...

For ex:- A-Z a-z special
         0-9 special
"""

print(des) # Prints the description
phrase = input("Enter the terms: ") # Takes the term required for combination

max = int(input("Enter password length: ")) # Let's you input maximum length of password

def sec(length):
    if length <= 3:
        print("Password is Weak")
    elif length > 3 and length < 5:
        print("Password is Good")
    elif length == 5 or length < 10:
        print("Password is Strong")
    elif length >= 10:
        print("Password is Very Strong") 

sec(max)

L_password = [] # Empty list which will store new generated password in the form of list

# if max > 0:
#   while max>0:
#       if phrase != "":
#             new_list = SLmethod.convert_to_list(phrase) 
#             for element in new_list:
#                 if element == "A-Z":
#                     index = random.sample(population=U_alphabet, k=1)
#                     L_password.append(index)
#                     pass
#                 elif element == "a-z":
#                     index = random.sample(population=l_alphabet, k=1)
#                     L_password.append(index)
#                     pass
#                 elif element == "0-9":
#                     index = random.sample(population=numeric, k=1)
#                     L_password.append(index)
#                     pass
#                 elif element == "special":
#                     index = random.sample(population=special_char, k=1)
#                     L_password.append(index)
#                     pass
#                 else:
#                     print(f"You Entered Invalid Term {element} in terms {new_list}")
#                     exit()
#       else:
#             print("Please enter some terms to run code !")
#             exit()
#       max-=1 # reduce value of max by 1
# else:
#     print("You entered password length less than 1 !")

SLmethod.pass_creator(max, argument="A-Z a-z 0-9", L_list=L_password,list1=U_alphabet,list2=l_alphabet,list3=numeric,list4=special_char) 
# print(L_password)
#flat_list = [item for sublist in password for item in sublist] # We can also use this
#print(flat_list)

# It is used to convert [['R'], ['e'], [']'], ['P'], ['m'], ['<']] --> ['R', 'e', ']', 'P', 'm', '<']
l_password = sum(L_password, [])
# print(l_password)


password = ''.join(l_password)
print(password)
