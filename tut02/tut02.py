def get_memory_score():
    mem = []
    ans = 0
    for i in input_nums:
        if i in mem:
            ans += 1
            continue

        if len(mem) < 5:
            mem.append(i)
        else:
            del mem[0]
            mem.append(i)

    return ans


input_nums =  [3, 4, 1, 6, 3, 9, 1, 0, 0, 0]
res = []
flag = 0
for i in input_nums:
    if not isinstance(i, int) or i>9 or i<0:
        flag = 1
        res.append(i)

if flag == 1:
    print("Please enter a valid input list. Invalid input detected: ", res)
else:
    print("Score:", get_memory_score())