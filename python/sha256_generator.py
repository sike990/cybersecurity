import hashlib

def hash_msg(string:str)->str:
    """Returns hash code in hexadecimal"""
    string_byte = string.encode("utf-8","replace")
    string_shaobject = hashlib.sha256(string_byte)
    return string_shaobject.hexdigest()
pass = "yoloboi"
print(f"Password is {pass}")
print("The hashed version of it : ",hash_msg(pass))

    
