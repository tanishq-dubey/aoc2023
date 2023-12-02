

data = []
with open('input') as f:
    data = f.readlines()


total = 0

for d in data:
    dstring = ''.join(filter(str.isdigit, d))
    d1 = dstring[0]
    d2 = dstring[-1]
    print(d1, "-", d2)
    total = total + int(f"{d1}{d2}")


print("=======")
print(total)
print("=======")



# Part 2
