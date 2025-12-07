import random as rnd
#Developing a random password generator

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
for _ in range(4):
    rndstring = rnd.choice(seq)
    ch = rnd.choice(rndstring)
    passw += ch
#Now we have our password but we are still following a pattern for first 4 char lets shuffle entire string
lst = rnd.sample(list(passw),len(passw))

passw = "".join(lst)# I know this is crazy approach but chalega
print(f"Your random password is {passw}")
