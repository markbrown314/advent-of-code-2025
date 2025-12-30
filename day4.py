#!/usr/bin/env python3
"""
🎅🏻 Day 4: Printing Department
"""

def adj_scan(c :tuple, space: set):
    adj = 0
    offsets = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(1, -1),(1, 0),(1, 1), (0, 1)]
    for o in offsets:
        if (c[0]+o[0], c[1]+o[1]) in space:
            adj += 1
    return adj

def day4_solution(filename: str):
    p_space = set()
    with open(filename) as f:
        y = 0
        marked = 0
        for l in f:
            x = 0
            for p in l.replace('\n', ''):
                if p == '@':
                    p_space.add((x,y))
                x += 1
            y += 1
        for c in p_space:
            if adj_scan(c, p_space) < 4:
                marked += 1

        found = True
        removed = 0

        while found:
            space = set.copy(p_space)
            found = False
            for c in space:
                if adj_scan(c, space) < 4:
                    found = True
                    p_space.remove(c)
                    removed += 1

        print("answer #1", marked, "answer #2", removed)

if __name__ == "__main__":
    day4_solution("input_day4.txt")