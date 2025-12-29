import math
import string 
 
def load_common_password(file_path="common_password.txt"):
  try:
     with open(file_path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f)
  except FileNotFoundError:
     return set()
  
COMMON_PASSWORDS=load_common_password()

def calculate_entropy(password):
   pool_size=0
   if any(c in string.ascii_lowercase for c in password):
      pool_size=pool_size+26
   if any(c in string.ascii_uppercase for c in password):
      pool_size=pool_size+26
   if any(c in string.digits for c in password):
      pool_size=pool_size+10
   if any(c in string.punctuation for c in password):
      pool_size=pool_size+len(string.punctuation)

   if pool_size ==0:
      return 0
   
   entropy=len(password)*math.log2(pool_size)
   return round(entropy,2)

def password_strength(entropy):
   if entropy < 30:
      return "SLABA", 25
   elif entropy < 50:
      return "MEDIE", 50
   elif entropy < 75:
      return "PUTERNICA", 75
   else:
      return "FOARTE PUTERNICA", 100
   
def analyze_password(password):
   problems=[]
   suggestions=[]
   if len(password)<12:
      problems.append("Prea scurta")
      suggestions.append("Creste lungimea parolei")
   if not any(c.islower() for c in password):
      problems.append("Lipsesc litere mici")
      suggestions.append("Adauga litere mici")
   if not any(c.isupper() for c in password):
      problems.append("Lipsesc litere mari")
      suggestions.append("Adauga litere mari")
   if not any(c in string.punctuation for c in password):
      problems.append("Lipsesc caractere speciale")
      suggestions.append("Adauga caractere speciale")
   if password.lower() in COMMON_PASSWORDS:
      problems.append("Parola este in lista de parole comune")
      suggestions.append("Evita parolele comune")
   
   entropy=calculate_entropy(password)
   strength,score=password_strength(entropy)
   
   return {
      "password":password,
      "entropy":entropy,
      "strength":strength,
      "score":score,
      "problems":problems,
      "suggestions":suggestions
   }