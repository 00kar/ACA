N = int(input("Enter the length of sequence: "))
k = int(input("Enter the count of shifts: "))

if k >= N:
    k -= N*(k//N)

seq = []
for i in range(N):
    seq.append(int(input()))

seq = seq[N-k:] + seq[:N-k]
print(seq)
