"""
Program name : SLmethod.py
Author       : Prateek Mahadev Waghmare
Written on   : 27-Apr-24 23:37:06 IST
Description  : I am presently engaged in learning Python and have developed this modest code to assess my proficiency 
in Python programming. The program is designed to address fundamental trigonometric problems, and I have endeavored 
to craft it to the best of my abilities. Should you wish to offer corrections or enhancements to this code, your 
input would be welcomed. 
"""

import random
"""
Used to convert a given String(It should contain whitespaces) to List
For Ex:- 
        alpha = "Hello World !" (!!!Note:- whitespaces are important)
        gamma = convert_to_list(alpha)
        print(gamma) # Output:- ['Hello', 'World', '!']
"""


def convert_to_list(eqt):
    # Split the inputed eqution string at whitespace
    terms = eqt.split()

    # Initialize an empty list to store the converted elements
    eq_list = []

    # Iterate over the terms
    for term in terms:
        # If term is not whitespace, add it to the list
        if term.strip() != "":
            eq_list.append(term.strip())

    return eq_list


"""
Here,
length = It is the length of password.
argument = Here we pass the terms we want in our password. For ex:- A-Z a-z special.
L_list = It stores the list which is created from this function.
list1 to list4 = This are the list which are used to generate password.

For Ex:-
    pass_creator(max, argument="A-Z a-z 0-9", L_list=L_password,list1=U_alphabet,list2=l_alphabet,list3=numeric,list4=special_char)
"""

def pass_creator(length, argument, L_list, list1, list2, list3, list4):
    if length > 0:
        while length>0:
            if argument != "":
                    new_list = convert_to_list(argument) 
                    for element in new_list:
                        if element == "A-Z":
                            index = random.sample(population=list1, k=1)
                            L_list.append(index)
                            pass
                        elif element == "a-z":
                            index = random.sample(population=list2, k=1)
                            L_list.append(index)
                            pass
                        elif element == "0-9":
                            index = random.sample(population=list3, k=1)
                            L_list.append(index)
                            pass
                        elif element == "special":
                            index = random.sample(population=list4, k=1)
                            L_list.append(index)
                            pass
                        else:
                            print(f"You Entered Invalid Term {element} in terms {new_list}")
                            exit()
            elif argument != "A-Z" or argument != "a-z" or argument != "0-9" or argument != "special":
                 print("Enter Valid Term")
                 exit()
            elif argument == "":
                print("The term field cannot be empty")
                exit()
            else:
                    print("Please enter some terms to run code !")
                    exit()
            length-=1 # reduce value of length by 1
    else:
        print("You entered password length less than 1 !")


"""
Here,
length = It is the length of password.
argument = Here we pass the terms we want in our password. For ex:- A-Z a-z special.
L_list = It stores the list which is created from this function.
list1 to list4 = This are the list which are used to generate password.

It is similar to pass_creator but the only difference is that here same term can be repeated.

For Ex:-
    pass_creator(max, argument="A-Z a-z 0-9", L_list=L_password,list1=U_alphabet,list2=l_alphabet,list3=numeric,list4=special_char)
"""

def pass_creator2(length, argument, L_list, list1, list2, list3, list4):
    if length > 0:
        while length>0:
            if argument != "":
                    new_list = convert_to_list(argument) 
                    for element in new_list:
                        if element == "A-Z":
                            index = random.choice(seq=list1)
                            L_list.append(index)
                            pass
                        elif element == "a-z":
                            index = random.choice(seq=list2)
                            L_list.append(index)
                            pass
                        elif element == "0-9":
                            index = random.choice(seq=list3)
                            L_list.append(index)
                            pass
                        elif element == "special":
                            index = random.choice(seq=list4)
                            L_list.append(index)
                            pass
                        else:
                            print(f"You Entered Invalid Term {element} in terms {new_list}")
                            exit()
            elif argument != "A-Z" or argument != "a-z" or argument != "0-9" or argument != "special":
                 print("Enter Valid Term")
                 exit()
            elif argument == "":
                print("The term field cannot be empty")
                exit()
            else:
                    print("Please enter some terms to run code !")
                    exit()
            length-=1 # reduce value of length by 1
    else:
        print("You entered password length less than 1 !") 