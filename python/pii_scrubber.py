#Does pii redaction for email,phone(+91 style),credit,card using regex
import re

def handle_email(match)->str:
    email = match.group(0)
    
    add,tail = (match.group(1),match.group(2))
    readd = add[0]
    readd += "*"*(len(add)-1)
    final = readd + "@" + tail
    return final
    
def handle_phone(match)->str:
    cc,spac,head,tail = (match.group(1),match.group(2),match.group(3),match.group(4))
    final = cc + spac + "X"*len(head) + tail
    return final

def handle_credit(match)->str:
    length = len(match.groups())
    final = ""
    print(match.groups(0))
    for ind,part in enumerate(match.groups()):
        if len(part) == 4:
            if ind == length-1:
                final += part
            else:
                final += "#"*4
        else:
            final += part
    return final
    
def pii_scrub(logs:str)->str:
    #fix email
    email_pattern = r"\b([A-Za-z0-9\.\_]+)[@]([A-Za-z0-9]{2,}[\.][a-z]{2,})\b"
    x = re.sub(email_pattern,handle_email,logs)
    
    #fix phone number
    phone_pattern = r"(\+91)(\s*)([6-9]\d{5})(\d{4})\b"
    x = re.sub(phone_pattern,handle_phone,x)
   
    
    #fix credit card
    credit_pattern = r"(\d{4})([\-\s]*)(\d{4})([\-\s]*)(\d{4})([\-\s]*)(\d{4})\b"
    x = re.sub(credit_pattern,handle_credit,x)
    
    return x


inp = input("Enter the string : ").strip()
print()
print("User input : ",inp)
redinp = pii_scrub(inp)
print()
print("Modified input : ",redinp)
print()
