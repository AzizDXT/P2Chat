sudo apt-get update -y
sudo apt-get install python3 python2 python3-pip figlet lolcat git php dbus-x11 gnome-terminal tar -y
pip install  cryptography requests json time os threading folium geopy psutil wmi Dispatch ping3 termcolor re base64
sudo apt-get update -y
mkdir -p ~/.local/share/fonts/figlet-fonts/
git clone https://github.com/xero/figlet-fonts.git ~/.local/share/fonts/figlet-fonts/
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
wget https://github.com/ekzhang/bore/releases/download/v0.5.0/bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
tar xzvf bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
clear
sleep 1
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
rm -rf figlet-fonts bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
wget -O ~/.local/share/fonts/figlet-fonts/Reg.flf https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Regular.flf
clear
sleep 2
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Finish! | lolcat
sleep 2
clear
echo Running Service.
sleep 1
clear
echo Running Service..
sleep 1
clear
echo Running Service...
sleep 1
clear
gnome-terminal -- python3 Chat.py
