import os
import sys
import time

# Colors for style
C = "\033[36m" # Cyan
G = "\033[32m" # Green
Y = "\033[33m" # Yellow
R = "\033[31m" # Red
W = "\033[0m"  # White

def banner():
    os.system("clear")
    print(f"{C}")
    print("╔══════════════════════════════════════╗")
    print("║     TATIYA DESKTOP INSTALLER v3.0    ║")
    print("║     Multi-Environment Support (GUI)  ║")
    print("╚══════════════════════════════════════╝")
    print(f"{W}")

def install_desktop(name, package, startup_content):
    print(f"\n{Y}[*] Installing {name}...{W}")
    time.sleep(1)
    os.system(f"pkg install {package} -y")
    
    print(f"{Y}[*] Fixing VNC Black Screen...{W}")
    vnc_path = "/data/data/com.termux/files/home/.vnc"
    if not os.path.exists(vnc_path):
        os.makedirs(vnc_path)
    
    # Write xstartup file
    with open(f"{vnc_path}/xstartup", "w") as f:
        f.write("#!/data/data/com.termux/files/usr/bin/sh\n")
        f.write(startup_content)
    
    os.system(f"chmod +x {vnc_path}/xstartup")
    print(f"\n{G}[SUCCESS] {name} Installed!{W}")
    print(f"{C}Type 'vncserver' to start.{W}")

def main():
    banner()
    print("Choose your Desktop Environment:")
    print(f"{G}[1]{W} XFCE4    (Recommended - Best Balance)")
    print(f"{G}[2]{W} LXQt     (Lightweight & Modern)")
    print(f"{G}[3]{W} MATE     (Classic Windows Feel)")
    print(f"{G}[4]{W} Openbox  (Super Fast - For Hackers)")
    print(f"{R}[0]{W} Exit")
    
    choice = input(f"\n{Y}[?] Select Option: {W}")
    
    if choice == "1":
        install_desktop("XFCE4", "xfce4", "xfce4-session &")
    elif choice == "2":
        install_desktop("LXQt", "lxqt", "startlxqt &")
    elif choice == "3":
        install_desktop("MATE", "mate-desktop-environment", "mate-session &")
    elif choice == "4":
        install_desktop("Openbox", "openbox pypanel xorg-xsetroot", "openbox-session &")
    elif choice == "0":
        print(f"{R}[!] Exiting...{W}")
        sys.exit()
    else:
        print(f"{R}Invalid Option!{W}")

if __name__ == "__main__":
    main()

