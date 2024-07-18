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


if __name__ == "__main__":
    """Process the log lines."""

    # Initialize counters and storage for the metrics
    total_file_size, line_count = 0, 0
    status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                          "403": 0, "404": 0, "405": 0, "500": 0}

    def print_stats(status_code_counts: dict, file_size: int) -> None:
        print("File size: {:d}".format(total_file_size))
        for key, value in sorted(status_code_counts.items()):
            if value > 0:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            parts = line.split()
            line_count += 1
            try:
                # Extract and count the status code
                status_code = parts[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except BaseException:
                pass
            try:
                file_size = int(parts[-1])
            except BaseException:
                pass

            if line_count % 10 == 0:
                print_stats(status_code_counts, total_file_size)
        print_stats(status_code_counts, total_file_size)

    except KeyboardInterrupt:
        # Print the last lines
        print_stats(status_code_counts, total_file_size)
        raise
