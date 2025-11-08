def find(s, n):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] + s[j] == n:
                return [i,j]

nums = [3,3]
target = 6
print(find(nums,target))
