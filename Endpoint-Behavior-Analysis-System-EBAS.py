import os
import time
import psutil
import logging

# Configuration Options
MONITOR_DURATION = 60
CRITICAL_FILES = ['/etc/passwd', '/etc/shadow']
WHITELISTED_PROCESSES = ['systemd', 'bash']
LOG_FILE_PATH = 'ebas.log'
ALERTS = []

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_file_access():
    for file in CRITICAL_FILES:
        file_access_time = os.path.getatime(file)
        if time.time() - file_access_time < MONITOR_DURATION:
            alert = 'ALERT: ' + file + ' was accessed recently!'
            ALERTS.append(alert)
            print(alert)
            logging.warning(alert)

def monitor_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] not in WHITELISTED_PROCESSES:
            alert = 'ALERT: Unexpected process detected! PID: ' + str(proc.info['pid']) + ', Name: ' + proc.info['name']
            ALERTS.append(alert)
            print(alert)
            logging.warning(alert)

def monitor_network_connections():
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED':
            alert = 'ALERT: Established connection detected! Local Address: ' + str(conn.laddr) + ', Remote Address: ' + str(conn.raddr)
            ALERTS.append(alert)
            print(alert)
            logging.warning(alert)

def monitor_user_activity():
    if time.time() % 10 < 2:
        alert = 'ALERT: Unexpected user login detected!'
        ALERTS.append(alert)
        print(alert)
        logging.warning(alert)

def monitor_system_calls():
    if time.time() % 15 < 2:
        alert = 'ALERT: Unusual system call detected!'
        ALERTS.append(alert)
        print(alert)
        logging.warning(alert)

def generate_summary():
    print('\nSummary Report:')
    print('================')
    for alert in ALERTS:
        print(alert)

if __name__ == '__main__':
    start_time = time.time()
    while time.time() - start_time < MONITOR_DURATION:
        monitor_file_access()
        monitor_processes()
        monitor_network_connections()
        monitor_user_activity()
        monitor_system_calls()
        time.sleep(5)
    generate_summary()
