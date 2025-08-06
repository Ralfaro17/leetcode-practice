# s is the argument LeetCode uses
s = "DCXXI"

possibilities = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}

combined = [x for x in possibilities.keys() if len(x) == 2]

total = 0

processed_combined = False

length_s = len(s)

for step, value in enumerate(s):
    if processed_combined:
        processed_combined = False
        continue
    if step + 1 < length_s:
        try:
            total += possibilities[value + s[step + 1]]
            processed_combined = True
        except:
            processed_combined = False
            total += possibilities[value]
    else:
        total += possibilities[value]

print(total)
# return total