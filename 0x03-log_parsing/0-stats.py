#!/usr/bin/python3
"""Log parsing"""
import sys

if __name__ == '__main__':

    statusCodes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    count = 0
    size = 0$

def printStatus(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0
            printStatus(statusCode, size)

         stlist = line.split:
             count += 1

             try:
                 size += int(stlist[-1])
             except BaseException:
                 pass

             try:
                 if stlist[-2] in statusCodes:
                     statusCodes[stlist[-2]] += 1
              except BaseException:
                  pass
              printStatus(statusCodes, size)

except KeyboardInterrupt:
    printStatus(statusCodes, size)
    raise



