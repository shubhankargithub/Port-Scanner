# Port Scanner

Welcome to the Advanced Port Scanner, a sophisticated Python tool designed for comprehensive network port scanning. This script utilizes advanced networking techniques and industry-standard libraries to deliver precise and detailed insights into the network services running on a target system. Below is a detailed overview of the script's functionality, usage instructions, and its underlying components.

## Overview

The Advanced Port Scanner is engineered to offer a seamless experience in identifying open ports and their associated services on a specified target IP address or domain name. Leveraging the power of the Python programming language and robust networking libraries, it empowers users with the ability to conduct thorough network reconnaissance effortlessly.

## Features

### 1. Full Port Range Scanning

The scanner meticulously examines all ports within the specified range, providing a comprehensive overview of the target system's exposed services. By default, it scans ports from 1 to 1024, covering a broad spectrum of potential vulnerabilities and services.

### 2. Real-time Progress Feedback

During the scanning process, the script offers real-time feedback by displaying the current port being scanned. This feature ensures users are kept informed about the progress of the scan, enhancing transparency and user experience.

### 3. Detailed Service Detection

Upon identifying an open port, the scanner goes a step further by retrieving detailed information about the service running on that port. Utilizing the `socket` library's `getservbyport()` function, it fetches the service name associated with the open port, providing valuable insights for further analysis.

### 4. Enhanced Visualization

To facilitate ease of interpretation and visualization of results, the scanner employs colorful output formatting using the `termcolor` library. This enhances the readability of scan results, making it easier for users to identify open ports and their corresponding services at a glance.

## Usage

1. **Prerequisites**: Ensure Python is installed on your system.
2. **Library Installation**: Install the `termcolor` library using pip:
    ```
    pip install termcolor
    ```
3. **Execution**: Run the script and provide the target IP address or domain name when prompted. Follow the on-screen instructions to initiate the scan and view the results.

## Functions Overview

### `print_port_scanner_pattern()`

This function displays an aesthetically pleasing ASCII art pattern representing the name of the port scanner. It leverages the `termcolor` library to render the pattern in a professional and visually appealing manner.

### `scan_port(target_ip, port)`

The `scan_port()` function is responsible for scanning a specific port on the target IP address. It establishes a TCP connection with the port and determines whether it is open or closed. If the port is open, it retrieves the associated service name using `socket.getservbyport()`.

### `scan_target(target)`

Initiates a full port scan on the specified target IP address or domain name. The function resolves the target to an IP address using `socket.gethostbyname()` and iterates through the port range, invoking `scan_port()` for each port.


## Authorship

The Advanced Port Scanner is meticulously crafted by Dhananjay Chavan, a seasoned professional in the field of cybersecurity. With a focus on reliability, efficiency, and user experience, this tool exemplifies excellence in network reconnaissance and vulnerability assessment.


