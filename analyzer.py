import math
import string 
 
def load_common_password(file_path="common_pasword.txt"):
  try:
     with open(file_path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f)
  except FileNotFoundError:
     return set()