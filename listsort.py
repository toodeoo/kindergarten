s = input().split()
array = []
for i in range(len(s)):
    array.append(int(s[i]))
    # array.sort()默认升序
array.sort(reverse=True)  # 降序排列
print(array)
