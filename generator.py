import secrets
import string
import random

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
  print("Trebuie aleas cel putin un tip de caractere")
  return None

 password= "".join(secrets.choice(char_pool) for _ in range(length))
 return password

def generate_memorable_password(words=3):
  word_list=["soare","luna","mare","munte","carte","pisica","caine","floare","nor","stele"]
  chosen=random.sample(word_list,words)
  return "-".join(chosen)
