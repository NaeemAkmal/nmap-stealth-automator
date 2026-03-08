# 🛡️ Nmap Advanced Stealth & Verbose Automator

This repository hosts a professional Python-based automation script designed for the **Network Enumeration** and **Information Gathering** phase of a penetration test. The tool streamlines complex `nmap` commands, focusing on firewall bypass techniques and stealth scanning.

## 📖 Project Description & Disclaimer
**Description:** The `nmap_stealth.py` script is a menu-driven automation tool that allows security researchers to execute various advanced scanning techniques—from TCP SYN and XMAS scans to highly anonymous Idle/Zombie scans. It automates evasion flags such as packet fragmentation, MTU manipulation, and decoy addresses to simulate real-world attack scenarios and test network resilience.

**⚠️ LEGAL DISCLAIMER:** This tool is intended strictly for **Educational Purposes** and authorized **Ethical Hacking** assessments. Unauthorized scanning or accessing networks without explicit written permission is illegal. The developer (Naeem Akmal) is not responsible for any misuse or damage caused by this tool. Use it only in controlled lab environments or on systems you are legally authorized to test.

## 🚀 Key Technical Features
- **TCP SYN Stealth Scanning:** High-speed discovery using half-open connections to minimize detection.
- **Service Version Detection:** Real-time identification of running services (e.g., FTP, SSH, HTTP) with verbose output.
- **Firewall & IDS Evasion:**
  - **XMAS Tree Scans** to probe stateless firewalls.
  - **Packet Fragmentation & MTU 16** to bypass Deep Packet Inspection (DPI).
  - **Decoy Scanning** to mask the real origin of the scan among multiple IPs.
- **Total Anonymity (Idle Scan):** Advanced probing via a silent "Zombie" host for complete source IP protection.

## 💻 Usage Instructions
1. Ensure Nmap and Python 3 are installed on your Linux environment.
2. Run the script with root privileges:
   ```bash
   sudo python3 nmap_stealth.py
Enter the Target IP and select your desired evasion technique from the menu.
