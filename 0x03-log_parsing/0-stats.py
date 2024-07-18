#!/usr/bin/python3
"""
This script reads from stdin line by line, processes each line to extract
file size and status code if the line matches the expected format, and
computes cumulative statistics. It prints the total file size and the count
of each status code after every 10 lines and upon keyboard interruption
(CTRL+C).
format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import signal

# Initialize counters and storage for the metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def handle_signal(total_file_size, status_code, status_code_counts):
    """Handles the keyboard interruption (CTRL+C) signal."""
    print(f"{status_code}: {status_code_counts[status_code]}")
    print(f"File size: {total_file_size}")
    sys.exit(0)


if __name__ == "__main__":
    """Process the log lines."""

    # Read input from stdin
    for line in sys.stdin:
        parts = line.split()

        # Ensure the line has the correct format
        # if (len(parts) == 9 and parts[5] == '"GET'):
        try:
            # Extract and accumulate file size
            file_size = int(parts[-1])
            total_file_size += file_size

            # Increment line count
            line_count += 1

            # Extract and count the status code
            status_code = int(parts[-2])
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
                print(f"{status_code}: {status_code_counts[status_code]}")

            if line_count % 10 == 0:
                print(f"File size: {total_file_size}")

        except ValueError:
            # Skip lines with invalid integers for file size or status code
            continue

    # Set up the signal handler for keyboard interruption
    signal.signal(signal.SIGINT, handle_signal(total_file_size, status_code, status_code_counts))
