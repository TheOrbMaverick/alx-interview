#!/usr/bin/python3
"""
This script reads from stdin line by line, processes each line to extract
file size and status code if the line matches the expected format, and 
computes cumulative statistics. It prints the total file size and the count 
of each status code after every 10 lines and upon keyboard interruption (CTRL+C).
format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import signal

# Initialize counters and storage for the metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the current statistics: total file size and count of status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_signal(sig, frame):
    """Handles the keyboard interruption (CTRL+C) signal."""
    print_stats()
    sys.exit(0)


# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_signal)

# Read input from stdin
for line in sys.stdin:
    parts = line.split()

    # Ensure the line has the correct format
    if len(parts) == 10 and parts[5] == '"GET' and parts[6] == '/projects/260' and parts[7] == 'HTTP/1.1"':
        try:
            # Extract and accumulate file size
            file_size = int(parts[-1])
            total_file_size += file_size

            # Extract and count the status code
            status_code = int(parts[-2])
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except ValueError:
            # Skip lines with invalid integers for file size or status code
            continue

    # Increment line count
    line_count += 1

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()
