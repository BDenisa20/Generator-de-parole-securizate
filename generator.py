import secrets
import string

def generate_password(length, use_lower=True, use_upper=True, use_digits=True, use_special=True):
 char_pool=""
 if use_lower:
  char_pool=char_pool+string.ascii_lowercase
 if use_upper:
  char_pool=char_pool+string.ascii_uppercase
 if use_digits:
  char_pool=char_pool+string.digits
 if use_special:
  char_pool=char_pool+"!@#$%^&*()-_=+[]{};:,.<>/?"
 if not char_pool:
  print("Trebuie aleasa cel putin un tip de caractere")
  return None

 password= "".join(secrets.choice(char_pool) for _ in range(length))
 return password
