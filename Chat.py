
from cryptography.fernet import Fernet
import os
import sys
import requests
import base64

os.system("clear")
N = input("Name : ")

X = input("Type Message :")
#----------Send part-----------  
sample_string = f"{X}"
sample_string_bytes = sample_string.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
  
X2 = base64_string

data = {
  "Name": f"{N}",
  "Message": f"{X2}",
}


url = 'http://bore.pub:1983/Save.php'
response = requests.post(url, data=data)

#----------Reception part-----------
