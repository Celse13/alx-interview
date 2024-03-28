#!/usr/bin/python3
"""Parse logs"""


def print_status(status, sizes):
    """ print stats"""
    print(f"File size: {sizes}")
    for key, value in sorted(status.items()):
        if value != 0:
            print(f"{key}: {value}")


occurence = 0
get_size = 0
status_info = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}

try:
    while True:
        try:
            get_line = input()
            line_content = get_line.strip().split()

            if not get_line:
                break

            if len(line_content) > 2:
                size = int(line_content[-1])
                stat_code = line_content[-2]

                if stat_code in status_info:
                    status_info[stat_code] += 1

                get_size += size
                occurence += 1

                if occurence == 10:
                    print_status(status_info, get_size)
                    occurence = 0

        except (KeyboardInterrupt, EOFError):
            break
finally:
    print_status(status_info, get_size)
