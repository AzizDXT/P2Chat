
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


url = 'http://127.0.0.1:80/Save.php'
response = requests.post(url, data=data)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    print('Request was successful!')
    print('Response content:', response.text)
else:
    print('Request failed with status code:', response.status_code)

#----------Reception part-----------
