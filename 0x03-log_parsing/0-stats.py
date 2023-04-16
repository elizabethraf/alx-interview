#!/usr/bin/python3
"""Display that reads stdin and computes metrics"""
import sys
from collections import defaultdict

stcd = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}
sum = 0


def prev_stats():
    """Function that print stats"""
    global sum

    print('File size: {}'.format(sum))
    stcdor = sorted(stcd.keys())
    for each in stcdor:
        if stcd[each] > 0:
            print('{}: {}'.format(each, stcd[each]))


if __name__ == "__main__":
    count = 0
    try:
        """ Iter the standar input """
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                """If there is a status code"""
                if fact[-2] in stcd:
                    stcd[fact[-2]] += 1
                """If there is a lenght"""
                sum += int(fact[-1])
            except:
                pass
            """Printing control"""
            count += 1
            if count == 10:
                prev_stats()
                count = 0
    except KeyboardInterrupt:
        prev_stats()
        raise
    else:
        prev_stats()
