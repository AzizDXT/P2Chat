import os
import requests
import base64
import json
import time

def send_message():
    os.system("clear")
    os.system("figlet P2Chat")
    print("=" * 40)
    N = input("Name: ")

    while True:
        X = input("Type Message (or 'exit' to quit): ")

        if X.lower() == "exit":
            break

        try:
            # ----------Send part-----------
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

            if response.status_code == 200:
                print("Message sent successfully.")
            else:
                print("Failed to send message.")
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
                            print(f"Received from {name}:")
                            print(f"Message: {message}")
                            print("=" * 40)
                        except json.JSONDecodeError as e:
                            print(f"Failed to parse content as JSON in {file_name}: {str(e)}")
                    
                    # Remove the text file
                    os.remove(file_path)
                    
            time.sleep(1)  # Wait for 1 second before scanning again
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Start the message sending loop in a separate thread
    import threading
    send_thread = threading.Thread(target=send_message)
    send_thread.start()

    # Start the file scanning and processing loop in the main thread
    process_text_files_in_directory()
