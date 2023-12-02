

data = []
with open('input') as f:
    data = f.readlines()


total = 0

for d in data:
    dstring = ''.join(filter(str.isdigit, d))
    if len(dstring) < 1:
        continue
    d1 = dstring[0]
    d2 = dstring[-1]
    total = total + int(f"{d1}{d2}")


print("=======")
print(total)
print("=======")



# Part 2
total = 0

dtt = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9n",
}

for d in data:
    tmp = d

    for _, _ in dtt.items():
        minidx = 10000000000
        minval = "invalid"
        for k,v in dtt.items():
            try:
                if tmp.index(k) < minidx:
                    minidx = tmp.index(k)
                    minval = k
            except ValueError as e:
                if "substring not found" in str(e):
                    continue
        if minval != "invalid":
            tmp = tmp.replace(minval, str(dtt[minval]), 1)

    dstring = ''.join(filter(str.isdigit, tmp))
    if len(dstring) < 1:
        continue
    d1 = dstring[0]
    d2 = dstring[-1]
    #print(d1, "-", d2, "----", tmp.strip(), d.strip())
    total = total + int(f"{d1}{d2}")


print("======= PT 2")
print(total)
print("=======")


total = 0
for d in data:
    tmp = d
    for k, v in dtt.items():
        try:
            tmp = tmp.replace(k, str(v))
        except Exception as e:
            pass
    dstring = ''.join(filter(str.isdigit, tmp))
    if len(dstring) < 1:
        continue
    d1 = dstring[0]
    d2 = dstring[-1]
    #print(d1, "-", d2, "----", tmp.strip(), d.strip())
    total = total + int(f"{d1}{d2}")

print("======= PT 2 - 2")
print(total)
print("=======")
