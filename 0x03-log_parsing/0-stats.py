#!/usr/bin/env/ python3
""" Parsing the log """


def print_stats(status, file_size):
    """  print the stats"""
    print(f"File size: {file_size}")
    for key, value in sorted(status.items()):
        if value != 0:
            print("{:s}: {:d}".format(key, value))


count = 0
file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}


try:
    while 1:
        try:
            get_line = input()
            if not get_line:
                break
            line_content = get_line.strip().split()
            if len(line_content) > 2:
                file_size += int(line_content[-1])
                status_code = line_content[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                count += 1
                if count == 10:
                    print_stats(status_codes, file_size)
                    count = 0
        except (EOFError, KeyboardInterrupt):
            break
finally:
    print_stats(status_codes, file_size)
