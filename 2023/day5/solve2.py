import re

EXAMPLE_INPUT_FILE = "example.txt"
INPUT_FILE = "input.txt"

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = f.read().strip().split('\n')

raw_seeds = list(map(int, lines[0].split(" ")[1:]))
seeds = [ 
    (raw_seeds[i], raw_seeds[i+1])
    for i in range(0, len(raw_seeds), 2)
]

# generate mappings
maps = []

i = 2
while i < len(lines):
    catA, _, catB = lines[i].split(" ")[0].split("-")
    maps.append([])
    
    i += 1
    while i < len(lines) and not lines[i] == "":
        dstStart, srcStart, rangeLen = map(int, lines[i].split())
        maps[-1].append((dstStart, srcStart, rangeLen))
        i += 1
    
    maps[-1].sort(key=lambda x:x[1])

    i += 1

# Ensure disjoin maps
for m in maps:
    for i in range(len(m)-1):
        if not m[i][1] + m[i][2] <= m[i+1][1]:
            print(m[i], m[i+1])

def remap(lo, hi, m):
    ans = []
    for dst, src, R in m:
        end = src + R - 1
        D = dst - src

        if not (end < lo or src > hi):
            ans.append((max(src, lo), min(end, hi), D))
        
    for i, interval in enumerate(ans):
        l, r, D = interval
        yield (l+D, r+D)

        if i < len(ans) - 1 and ans[i+1][0] > r + 1:
            yield (r+1, ans[i+1][0] - 1)
    
    if len(ans) == 0:
        yield (lo, hi)
        return

    if ans[0][0] != lo:
        yield (lo, ans[0][0]-1)
    if ans[-1][1] != hi:
        yield (ans[-1][1] + 1, hi)

locs = []

ans = 1 << 60

for start, R in seeds:
    cur_intervals = [(start, start + R - 1)]
    new_intervals = []
    for m in maps:
        for lo, hi in cur_intervals:
            for new_interval in remap(lo, hi, m):
                new_intervals.append(new_interval)
        
        cur_intervals, new_intervals = new_intervals, []

    for lo, hi in cur_intervals:
        ans = min(ans, lo)

print(ans)