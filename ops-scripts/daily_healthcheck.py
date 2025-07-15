import subprocess 
import os
import datetime 

LOG_FILE = '/srv/build2teach/daily_healthcheck.log'

def log(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {message}"
    print(log_entry) 
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry + '\n') 
        
def check_docker_running(): 
    try: 
        subprocess.run(['docker', 'ps'], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError
        log("Docker is not running.")

def check_app_container():
    try: 
        result = subprocess.run(['docker', 'ps', '--filter', 'name=django-app', '--format', '{{.Names}}'],
                                capture_output=True, text=True, check=True)
        if not result.strip():
            log("App container is not running.")
    except Exception as e:
        log(f"Error checking app container: {str(e)}")
        
def check_disk_space():
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    log("Disk space usage: {lines[1]}")  # Logs relevant line 
    
def main():
    log("=== Starting daily health check ===")
    check_docker_running()
    check_app_container()
    check_disk_space()
    log("=== Daily health check completed ===")
    
if __name__ == "__main__":
    main()  