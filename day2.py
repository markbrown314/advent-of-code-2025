#!/usr/bin/env python3
"""
🎅🏻 Day 2: Gift Shop
"""

def check_sub_patterns(s: str):
    sl = len(s)
    matched = False
    m = 0
    for st in range (1, sl//2 + 1):
        matched = True
        for p in range(0, sl, st):
            if p == 0:
                m = s[p:p+st]
            if m != s[p:p+st]:
                matched = False
                break
        if matched:
            break
    return matched

def day2_solution(filename: str):
    ra = []
    with open(filename) as f:
        for line in f:
            l = line.replace('\n', '')
            for r in l.split(','):
                if r == "":
                    continue
                ra.append(tuple(r.split('-')))
    ans1 = 0
    ans2 = 0
    for t in ra:
        for v in range(int(t[0]), int(t[1])+1):
            s = str(v)
            sl = len(s)
            if check_sub_patterns(s):
                ans2 += v
            if s[:sl//2] == s[sl//2:]:
                ans1 += v
    print("answer #1", ans1, "answer #2", ans2)

if __name__ == "__main__":
    day2_solution("input_day2.txt")
