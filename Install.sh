sudo apt-get update -y
sudo apt-get install python3 python2 python3-pip figlet lolcat git php dbus-x11 gnome-terminal -y ; sudo apt-get update -y ; pip install re cryptography requests base64 json time os threading ; sudo apt-get install python3 figlet ; sudo apt-get install python3 python2 python3-pip figlet lolcat git php dbus-x11 gnome-terminal -y
mkdir -p ~/.local/share/fonts/figlet-fonts/
git clone https://github.com/xero/figlet-fonts.git ~/.local/share/fonts/figlet-fonts/
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
pip install folium geopy psutil wmi Dispatch ping3 termcolor
wget https://github.com/ekzhang/bore/releases/download/v0.5.0/bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
clear
sleep 1
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installing... | lolcat
sudo apt install tar
tar xzvf bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
rm -rf figlet-fonts bore-v0.5.0-x86_64-unknown-linux-musl.tar.gz
cd ..
mv SetupFile/bore .
rm -rf SetupFile
wget -P ~/.local/share/fonts/figlet-fonts/ https://raw.githubusercontent.com/xero/figlet-fonts/master/ANSI%20Regular.flf 
cd ~/.local/share/fonts/figlet-fonts/
mv 'ANSI Regular.flf' Reg.flf
clear
figlet -c -f ~/.local/share/fonts/figlet-fonts/3d.flf Installed! | lolcat
sleep 2
clear
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
exit

