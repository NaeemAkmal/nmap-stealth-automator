# 🛡️ Automated Hping3 Stealth Enumeration Script

A powerful Python-based automation tool designed for **Network Enumeration** and **Firewall Evasion**. This script automates complex `hping3` commands to identify open ports and services while remaining stealthy using fragmentation and decoy techniques.

## 🚀 Features
- **TCP SYN Scan:** Systematic probing of ports 1-1024.
- **XMAS Tree Scan:** Stealthy scanning using FIN, PSH, and URG flags.
- **Firewall Evasion:** - IP Address Decoy (Single & 10x Random Spoofing).
  - Packet Fragmentation (Standard & Custom MTU 16).
  - Source Port Manipulation (Using DNS Port 53).
- **Idle Zombie Scan:** Advanced scanning using a silent host to hide the attacker's identity.

## 🛠️ Prerequisites
- **OS:** Kali Linux / Parrot OS
- **Tools:** `hping3`, `python3`
- **Privileges:** Sudo/Root access required for raw packet crafting.

## 📋 How to Use
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/hping3-enumeration-script.git](https://github.com/YourUsername/hping3-enumeration-script.git)
