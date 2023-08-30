# Endpoint Behavior Analysis System (EBAS)

This tool is designed to monitor and analyze endpoint behavior to detect potential threats based on unusual patterns or activities.

## Features

- **File Access Monitoring**: Monitors access to critical system files and alerts if they are accessed recently.
- **Process Monitoring**: Monitors running processes and alerts if any unexpected or non-whitelisted processes are detected.
- **Network Connection Monitoring**: Checks for established network connections and logs them.
- **User Activity Monitoring**: Simulates the detection of unexpected user logins.
- **System Call Monitoring**: Simulates the detection of unusual system calls.
- **Logging**: All alerts and important events are logged for later analysis.
- **Summary Report**: Provides a summary of detected activities at the end of the monitoring duration.

## Usage

1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```
   pip install psutil
   ```
3. Run the script:
   ```
   python ebas.py
   ```

## Configuration

You can modify the configuration options at the beginning of the script to customize the behavior:

- MONITOR_DURATION: Duration for which to monitor behavior.
- CRITICAL_FILES: List of critical system files to monitor.
- WHITELISTED_PROCESSES: Processes that are considered safe.
- LOG_FILE_PATH: Path for the log file.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or add new features.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational purposes only. Always seek permission before conducting any security testing.
