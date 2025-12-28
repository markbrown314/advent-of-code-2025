#!/usr/bin/env python3
"""
🎅🏻 Day 3: Lobby
"""

def day3_solution(filename: str, k: int):
    with open(filename) as f:
        total = 0
        max_pos = None
        for line in f:
            d = dict()
            l = line.replace('\n', '')
            cnt = len(l) - 1
            max_pos = cnt
            for pos, n in enumerate(l):
                v = d.get(int(n), [])
                v.append(cnt-pos)
                d[int(n)] = v
            # sort postions in dict
            for n in range(9, -1, -1):
                v = d.get(n, [])
                if v:
                    d[n] = sorted(v, reverse=True)
            bank = [0] * k
            for i in range(k - 1, -1, -1):
                for n in range(9, -1, -1):
                    v = d.get(n, [])
                    # cleanup array
                    if v and v[0] > max_pos:
                        v = [x for x in v if x <= max_pos]
                    pos = k - 1 - i
                    if v and v[0] >= i and n > bank[pos]:
                        max_pos = max([v[0] - 1, 0])
                        bank[pos] = n
                        v.pop(0)
                        d[n] = v
                        break
            total += int("".join([str(x) for x in bank]))
        return total


if __name__ == "__main__":
    print("answer #1", day3_solution("input_day3.txt", 2), end=" ")
    print("answer #2", day3_solution("input_day3.txt", 12))
