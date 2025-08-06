import itertools

s = "dvdf"
result = ""
temp = ""
for item in s:
    if item in temp:
        print(temp)
        temp = temp.replace(item, "")
    if item not in temp:
        temp += item
        if len(result) < len(temp):
            result = temp
    elif len(result) < len(temp):
        result = temp
        temp = item
if len(result) < len(temp):
    result = temp

print(result)