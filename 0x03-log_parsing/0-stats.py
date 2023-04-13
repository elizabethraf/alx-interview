#!/usr/bin/python3
"""Display that reads stdin and computes metrics"""
import sys
from collections import defaultdict


def print_metrics(total_size, status_code_counts):
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print("{}: {}".format(status_code, count))


def process_line(line, total_size, status_code_counts):
    parts = line.split()
    if len(parts) != 9:
        return total_size, status_code_counts
    ip_address, _, _, timestamp, _, method, path, status_code, filesize = parts
    try:
        status_code = int(status_code)
        file_size = int(parts[-1])
    except ValueError:
        return total_size, status_code_counts
    total_size += file_size
    status_code_counts[status_code] += 1
    return total_size, status_code_counts


total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        total_size, status_code_counts = process_line
        (line, total_size, status_code_counts)
        if line_count % 10 == 0:
            print_metrics(total_size, status_code_counts)
except KeyboardInterrupt:
    print_metrics(total_size, status_code_counts)
