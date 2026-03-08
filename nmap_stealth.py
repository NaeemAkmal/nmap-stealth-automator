import os

def print_banner():
    print("-" * 60)
    print("      🛡️ NMAP ADVANCED STEALTH & VERBOSE AUTOMATOR 🛡️")
    print("-" * 60)

def run_scanner():
    target = input("Enter Target IP: ")
    
    print("\nSelect Scanning Technique:")
    print("1. TCP SYN Scan (Stealth) + Verbose [Recommended]")
    print("2. TCP Connect Scan (Full Connection) + Verbose")
    print("3. XMAS Tree Scan (Firewall Evasion) + Verbose")
    print("4. Idle/Zombie Scan (Anonymity)")
    print("5. Decoy Scan (Hide Source IP with -v)")
    print("6. Fragmentation & MTU Evasion (Bypass IDS)")
    
    choice = input("\nEnter choice (1-6): ")

    # Sequence set: TCP SYN Priority
    if choice == '1':
        print("\n[*] Running Detailed TCP SYN Scan...")
        # -sS (SYN), -v (Verbose), -sV (Version)
        os.system(f"sudo nmap -sS -Pn -sV -v {target}")

    elif choice == '2':
        print("\n[*] Running Detailed TCP Connect Scan...")
        os.system(f"sudo nmap -sT -Pn -sV -v {target}")

    elif choice == '3':
        print("\n[*] Running XMAS Tree Scan with Verbose Output...")
        os.system(f"sudo nmap -sX -Pn -v {target}")

    elif choice == '4':
        zombie = input("Enter Zombie/Idle Host IP: ")
        print(f"[*] Running Anonymous Idle Scan via {zombie}...")
        os.system(f"sudo nmap -sI {zombie} -v {target}")

    elif choice == '5':
        print("1. Single Decoy (171.124.180.173)")
        print("2. 10 Random Decoys (RND:10)")
        d_choice = input("Choice: ")
        if d_choice == '1':
            os.system(f"sudo nmap -D 171.124.180.173 -g 80 -Pn -v {target}")
        else:
            os.system(f"sudo nmap -D RND:10 -g 53 -Pn -v {target}")

    elif choice == '6':
        print("\n[*] Running Fragmentation & MTU 16 Evasion...")
        os.system(f"sudo nmap -f -Pn --mtu 16 -v {target}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    print_banner()
    run_scanner()
