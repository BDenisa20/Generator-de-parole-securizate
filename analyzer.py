import math
import string 
 
def load_common_password(file_path="common_pasword.txt"):
  try:
     with open(file_path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f)
  except FileNotFoundError:
     return set()
  
COMMON_PASSWORD=load_common_password()

def calculate_entrpy(password):
   pool_size=0
   if any(c in string.ascii_lowercase for c in password):
      pool_size=pool_size+26
   if any(c in string.ascii_uppercase for c in password):
      pool_size=pool_size+26
   if any(c in string.ascii_digits for c in password):
      pool_size=pool_size+10
   if any(c in string.punctuation for c in password):
      pool_size=pool_size+len(string.punctuation)

   if pool_size ==0:
      return 0
   
   entropy=len(password)*math.log2(pool_size)
   return round(entropy,2)