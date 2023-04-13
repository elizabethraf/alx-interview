#!/usr/bin/python3
"""Display that reads stdin and computes metrics"""
import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


line_count = 0
file_sizes = {}
total_file_size = 0
status_code_counts = {}

try:
    for line in sys.stdin:
        line_count += 1

        try:
            ip_address, _, date, request, status_code_str, file_size_str, _ = line.split()
            status_code = int(status_code_str)
            file_size = int(file_size_str)

            if status_code in status_codes:
                if status_code not in status_code_counts:
                    status_code_counts[status_code] = 0
                status_code_counts[status_code] += 1

            if file_size > 0:
                total_file_size += file_size
                if request not in file_sizes:
                    file_sizes[request] = 0
                file_sizes[request] += file_size

        except ValueError:
            continue

        if line_count % 10 == 0:
            print("Total file size: File size: {}".format(total_file_size))
            for status_code in sorted(status_code_counts.keys()):
                print("{}: {}".format(status_code, status_code_counts[status_code]))
            line_count = 0

    print("Total file size: File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts.keys()):
        print("{}: {}".format(status_code, status_code_counts[status_code]))

except BrokenPipeError:
    pass
