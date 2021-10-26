n = int(input("Enter the base width of tree.\nIt must be odd!\n"))

tree = (n//2)*' ' + '*'
print(tree)
for i in range(n//2):
    tree = tree[1:] + '**'
    print(tree)
