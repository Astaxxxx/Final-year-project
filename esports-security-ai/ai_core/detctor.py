import os
import time
import scapy.all as scapy
import tensorflow.lite as tflite
import paramiko

# Load AI Model
interpreter = tflite.Interpreter(model_path="ai_engine/model.tflite")
interpreter.allocate_tensors()

def scan_for_cheats():
    suspicious_files = []
    cheat_keywords = ["aimbot", "wallhack", "triggerbot", "cheatengine"]
    
    for root, _, files in os.walk("C:/Users"):
        for file in files:
            if any(keyword in file.lower() for keyword in cheat_keywords):
                suspicious_files.append(os.path.join(root, file))
    
    return suspicious_files

def network_monitor():
    def process_packet(packet):
        if packet.haslayer(scapy.IP):
            src = packet[scapy.IP].src
            dst = packet[scapy.IP].dst
            print(f"Packet: {src} → {dst}")
    
    scapy.sniff(filter="tcp", prn=process_packet, store=False)

if __name__ == "__main__":
    print("🔍 Scanning for cheats...")
    cheats = scan_for_cheats()
    
    if cheats:
        print(f"⚠️ Detected cheat files: {cheats}")
    
    print("🌐 Starting network monitor...")
    network_monitor()
