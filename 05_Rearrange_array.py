# Q   - Rearrange array elements by sign
# Exp - Given an array of integers, rearrange the elements so that all positive numbers come before all negative numbers.

n = int(input())
arr = list(map(int, input().split()))

pos = []
neg = []

for x in arr:
    if x > 0:
        pos.append(x)
    else:
        neg.append(x)

result = []
i = 0

while i < len(pos) and i < len(neg):
    result.append(pos[i])
    result.append(neg[i])
    i += 1

print(result)