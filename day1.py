#!/usr/bin/env python3
import sys

"""
🎅🏻 Day 1: Secret Entrance
"""

def day1_solution(filename: str):
    rotations=[]
    with open(filename) as f:
        for line in f:
            l = line.strip()
            rotations.append((l[0], int(l[1:])))

    pos = 50
    click = 0
    landed_on_zero = 0

    for d, m in rotations:
        c = 0
        match d:
            case 'R':
                c = 1
            case 'L':
                c = -1
            case _:
                sys.exit("invalid direction specified")

        for n in range(0, m):
            pos += c
            if pos > 99:
                pos = 0
            if pos < 0:
                pos = 99
            if pos == 0:
                click += 1

        if not pos:
            landed_on_zero += 1

    print("answer #1", landed_on_zero, "answer #2", click)

if __name__ == "__main__":
    day1_solution("input_day1.txt")
