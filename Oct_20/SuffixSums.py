n = int(input("Enter count of elements in sequence: "))

seqA = []
for i in range(n):
    seqA.append(float(input()))

seqB = []
for i in range(n):
    seqB.append(sum(seqA[i:]))

print(seqB)
