#!/usr/bin/python3
"""Log parsing"""


def compute_metrics(status_code, file_sz):
    """Compute metrics"""
    print(f"File size: {file_sz}")
    for key, val in sorted(status_code.items()):
        if val != 0:
            print(f"{key}: {val}")


count = 0
file_size = 0
stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}

try:
    while True:
        try:
            line = input()
            data = line.strip().split()

            if not line:
                break

            if len(data) > 2:
                size = int(data[-1])
                stat_code = data[-2]

                if stat_code in stat_codes:
                    stat_codes[stat_code] += 1

                file_size += size
                count += 1

                if count == 10:
                    compute_metrics(stat_codes, file_size)
                    count = 0

        except (KeyboardInterrupt, EOFError):
            break
finally:
    compute_metrics(stat_codes, file_size)
