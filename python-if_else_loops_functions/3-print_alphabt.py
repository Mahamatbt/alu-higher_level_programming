#!/usr/bin/python3
for i in range(97, 123):
    if i != 113 and i != 101:  # Skip ASCII values for 'q' (113) and 'e' (101)
        print("{:c}".format(i), end="")
