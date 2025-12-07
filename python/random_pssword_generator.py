import random as rnd
#Developing a random password generator

def random_password_generator(length:int=8)->str:
    """Generates random password of given length"""
    #A-Z
    bigchar = str()
    for a in range(ord("A"),ord("Z")+1):
        bigchar += chr(a)
    #a-z
    smallchar = str()
    for a in range(ord("a"),ord("z")+1):
        smallchar += chr(a)
    #adding special characters
    specialchar = "!@#$%&"
    digits = "0123456789"
    
    #final sequence
    seq = (bigchar,smallchar,specialchar,digits)
    
    #Making the password
    #Logic first add atleast one character from each string and then add randomness in there selection as well
    #first 4
    passw = rnd.choice(bigchar) + rnd.choice(smallchar) + rnd.choice(digits) + rnd.choice(specialchar)
    #rest 4
    for _ in range(length):
        rndstring = rnd.choice(seq)
        ch = rnd.choice(rndstring)
        passw += ch
    #Now we have our password but we are still following a pattern for first 4 char lets shuffle entire string
    lst = rnd.sample(list(passw),len(passw))
    
    passw = "".join(lst)# I know this is crazy approach but chalega

    return passw

length = int(input("Enter the length of the password greater than equal to 8: "))
#The below check is just for fun
strlen = str(length)
set1 = set(list(strlen))
set2 = set(list("0123456789"))
set3 = set1-set2
flag = True if set3 else False
if length < 8 or flag:
    length = 8
passw = random_password_generator(length)
print(f"Your random password is {passw}")
