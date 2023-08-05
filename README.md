# Backdoor-reverse-shell-in-python

Here I've written a simple python reverse-shell-backdoor in python.

A reverse shell, also known as a remote shell or “connect-back shell,” takes advantage of the target system’s vulnerabilities to initiate a shell session and then access the victim’s computer. The goal is to connect to a remote computer and redirect the input and output connections of the target system’s shell so the attacker can access it remotely. Reverse shells allow attackers to open ports to the target machines, forcing communication and enabling a complete takeover of the target machine. Therefore it is a severe security threat. This method is also commonly used in penetration tests.

Make sure to change this in exe file, so that you can run this in windows.

To convert to .exe file:

Make sure you've installed PyInstaller 
If not use: pip install PyInstaller (You can do this in vs code terminal)
In terminal(vs code):
PyInstaller (file name) --noconsole --onefile

You can check now, you got a .exe file
