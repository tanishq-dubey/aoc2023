fname = "input"
data = []

with open(fname) as f:
    data = f.readlines()

"""
if the bag had been loaded with only 
12 red cubes, 
13 green cubes, and 
14 blue cubes
"""
MAXIMUMS = {
    "blue": 14,
    "green": 13,
    "red": 12

}

total = 0

for d in data:
    possible = True
    ginfo = d.split(":")
    gid = int(ginfo[0].split("Game")[-1])

    sets = ginfo[-1].split(";")
    for s in sets:
        d = s.split(",")
        for item in d:
            item = item.strip()
            vals = item.split(" ")
            color = vals[-1]
            count = int(vals[0])
            if count > MAXIMUMS[color]:
                possible = False
    if possible:
        total = total + gid

print(total)

total = 0
for d in data:
    mins = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    ginfo = d.split(":")
    gid = int(ginfo[0].split("Game")[-1])
    sets = ginfo[-1].split(";")
    for s in sets:
        d = s.split(",")
        for item in d:
            item = item.strip()
            vals = item.split(" ")
            color = vals[-1]
            count = int(vals[0])
            if mins[color] < count:
                mins[color] = count
    stotal = 1
    for k, v in mins.items():
        stotal = stotal * v
    total = total + stotal
    print(mins, gid, stotal)

print(total)
