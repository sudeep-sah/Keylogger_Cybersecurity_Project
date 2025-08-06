import os

log_file = "keystrokes.txt"

def check_log_file():
    if os.path.exists(log_file):
        size = os.path.getsize(log_file)
        if size > 0:
            print("[!] Potential keylogging activity detected:")
            print(f"     File: {log_file}, Size: {size} bytes")
        else:
            print("[✓] Log file found but empty.")
    else:
        print("[✓] No keylogger log file present.")

check_log_file()
