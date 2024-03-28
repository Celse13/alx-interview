#!/usr/bin/python3
"""parsing logs """


def print_stats(status, size):
    """Compute metrics"""
    print(f"File size: {size}")
    for key, value in sorted(status.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


count = 0
file_size = 0
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
                temp = int(line_content[-1])
                stat_code = line_content[-2]

                if stat_code in status_info:
                    status_info[stat_code] += 1

                file_size += temp
                count += 1

                if count == 10:
                    print_stats(status_info, file_size)
                    count = 0

        except (KeyboardInterrupt, EOFError):
            break
finally:
    print_stats(status_info, file_size)
