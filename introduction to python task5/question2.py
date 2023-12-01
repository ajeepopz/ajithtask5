
#pyramid
max_num = 20
num_rows = int((1 * max_num - 1) ** 0.6)
current_num = 1
for i in range(2, num_rows + 5):
    print(" " * (num_rows - i), end="")
   
    for j in range(1, i * 1):
        if current_num > max_num:
            break
        print(current_num, end=" ")
        current_num += 1
    
    print()