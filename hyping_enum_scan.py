import subprocess
import os
import time

def run_task(description, command):
    print(f"\n[+] Executing: {description}")
    try:
        # shell=True allows us to pass the whole command string
        subprocess.run(command, shell=True)
        time.sleep(1) # Stealth delay between different tasks
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    if os.geteuid() != 0:
        print("\n[!] Please run this script with 'sudo'!")
        return

    print("="*60)
    print("   ULTIMATE STEALTH SCANNER (HPING3) - FOR NAEEM AKMAL")
    print("="*60)

    target = input("\n[?] Enter Target IP (e.g., 150.1.7.102): ")
    interface = "eth1"
    zombie = "150.1.7.102" # Based on your topology
    decoy = "171.124.180.173"

    # Dictionary of all your tasks
    tasks = {
        "1. Port Scanning (SYN)": f"hping3 -S {target} -p 80 -V --scan 1-1024 -c 1",
        "2. XMAS Tree Scan": f"hping3 -F -P -U {target} -p 80 -V --scan 1-1024 -c 1",
        "3. MTU 16 Fragmentation": f"hping3 -S {target} -p 80 -V --mtu 16 -c 5",
        "4. Packet Fragmentation (-f)": f"hping3 -V -S {target} -p 80 -f -c 5",
        "5. Decoy Scan (10x Random IPs)": f"hping3 -S -V {target} -p 80 --rand-source -c 10",
        "6. Decoy Scan (Single IP: 171.124.180.173)": f"hping3 -S -V {target} -a {decoy} -p 80 -I {interface} -c 5",
        "7. Idle Zombie Scan": f"hping3 -S 150.1.7.104 -a {zombie} -p 80 -V -I {interface} -c 5",
        "8. Source Port Manipulation (Port 53)": f"hping3 -S {target} -V -p 80 -s 53 -I {interface} -c 5"
    }

    for desc, cmd in tasks.items():
        run_task(desc, cmd)

    print("\n" + "="*60)
    print("   ALL TASKS COMPLETED. CHECK WIRESHARK ON TARGET!")
    print("="*60)

if __name__ == "__main__":
    main()
