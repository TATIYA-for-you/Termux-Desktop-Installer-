import os
import time
import sys

# Colors for style
G = "\033[32m" # Green
R = "\033[31m" # Red
W = "\033[0m"  # White

def banner():
    os.system("clear")
    print(f"{G}")
    print("╔════════════════════════════════════════╗")
    print("║     TATIYA DESKTOP INSTALLER v2.0      ║")
    print("║     Turn Termux into a Pro Desktop     ║")
    print("╚════════════════════════════════════════╝")
    print(f"{W}")

def install_xfce():
    print(f"{G}[+] Updating Termux...{W}")
    os.system("pkg update -y && pkg upgrade -y")
    
    print(f"\n{G}[+] Installing X11 Repository...{W}")
    os.system("pkg install x11-repo -y")
    
    print(f"\n{G}[+] Installing XFCE4 Desktop & Tools...{W}")
    # Installing GUI, Browser, Terminal, and Audio
    os.system("pkg install xfce4 firefox termux-api pulseaudio -y")
    
    print(f"\n{G}[+] Configuring VNC Server...{W}")
    os.system("pkg install tigervnc -y")
    
    print(f"\n{G}[SUCCESS] Desktop Installed Successfully!{W}")
    print(f"{G}[INFO] Type 'vncserver' to start your desktop.{W}")

def main():
    banner()
    print("Select an option:")
    print("1. Install XFCE4 Desktop (Lightweight)")
    print("2. Exit")
    
    choice = input("\n[Tatiya] > ")
    
    if choice == "1":
        install_xfce()
    else:
        print("Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()

