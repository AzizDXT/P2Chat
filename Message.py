import os
import requests
import base64
import json
import time
import re
import threading

def send_message():
    os.system("clear")
    os.system("figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf P2Chat | lolcat ")
    print("=" * 40)
    portl = input("Local Port: ")
    if not portl:
        portl = 8080

    os.system(f"gnome-terminal -- php -S 127.0.0.1:{portl}")
    print("Account ID (XXXXX-XXXXX-XXXXX):")
    input_string = input("Or Enter to Skip: ")
    pattern = r'(\d+)-(\d+)-(\d+)'
    match = re.search(pattern, input_string)
    if match:
        # Extract the numbers from the match
        port = match.group(1)
        port1 = match.group(2)
        port2 = match.group(3)
    else:
        port = input("Public Port 1: ")
        port1 = input("Public Port 2: ")
        port2 = input("Public Port 3: ")

    os.system(f"gnome-terminal -- ./bore local {portl} --to bore.pub -p {port}")
    os.system(f"gnome-terminal -- ./bore local {portl} --to bore.pub -p {port1}")
    os.system(f"gnome-terminal -- ./bore local {portl} --to bore.pub -p {port2}")
    print("Run Servers | 4 Windows")
    N = input("Name: ")

    while True:
        X = input("Type Message (or 'exit' to quit): ")

        if X.lower() == "exit":
            break

        try:
            sample_string = f"{X}"
            sample_string_bytes = sample_string.encode("ascii")

            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")

            X2 = base64_string

            data = {
                "Name": f"{N}",
                "Message": f"{X2}",
            }
            urls = [
                f'http://bore.pub:{port}/Save.php',
                f'http://bore.pub:{port1}/Save.php',  
                f'http://bore.pub:{port2}/Save.php',
            ]

            for url in urls:
                try:
                    response = requests.post(url, data=data)

                    if response.status_code == 200:
                        
                        break  # Exit the loop if the message was sent successfully
                    else:
                        print("Failed to send message")
                except Exception as e:
                    print(f"Error sending message to {url}: {str(e)}")

        except Exception as e:
            print(f"Error sending message: {str(e)}")

def process_text_files_in_directory(directory_path="."):
    try:
        while True:
            files = os.listdir(directory_path)
            for file_name in files:
                if file_name.endswith(".txt"):
                    file_path = os.path.join(directory_path, file_name)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                        try:
                            data = json.loads(content)
                            name = data.get("Name", "N/A")
                            received_data = data.get("Message", "N/A")
                            decoded_message_bytes = base64.b64decode(received_data)
                            message = decoded_message_bytes.decode("utf-8")
                            print("=" * 40)
                            print(f"Received from {name}:")
                            print(f"Message: {message}")
                            print("=" * 40)
                        except json.JSONDecodeError as e:
                            print(f"Failed to parse content as JSON in {file_name}: {str(e)}")
                    
                    os.remove(file_path)
                    
            time.sleep(1)  
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    send_thread = threading.Thread(target=send_message)
    send_thread.start()

    process_text_files_in_directory()