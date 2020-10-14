n = int(input("How many integers would you like to enter?\n"))
print("Please enter",n, "integers.")
max_num = -999999
min_num = 9999999
for i in range(0, n):
    k = int(input())
    if k < min_num:
        min_num = k
    if k > max_num:
        max_num = k
print("min:", min_num)
print("max:", max_num)
