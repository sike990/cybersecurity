
def valid_password(passw:str)->bool:
    """Return bool for valid password"""
    if len(passw) < 8:
        return False
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
    bc,sc,spc,dc = (0,0,0,0)
    for c in passw:
        if c in bigchar:
            bc += 1
        elif c in smallchar:
            sc += 1
        elif c in specialchar:
            spc += 1
        elif c in digits:
            dc += 1
    if dc and sc and dc and spc:
        return True
    else:
        return False
    
passw1 = "Bolly@wood"
passw2 = "Jolly@3ood"
    
str1 = "Valid" if valid_password(passw1) else "Invalid"
str2 = "Valid" if valid_password(passw2) else "Invalid"
    
print(f"{passw1} is a {str1} password and {passw2} is a {str2} password.")
    
            
    
