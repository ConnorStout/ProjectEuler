def recurse(n, deep):
    if (n == 1):
        return (1)
    if (n % 2 == 0):
        return 1 + recurse(n / 2, deep)
    else:
        return 1 + recurse(((3 * n) + 1), deep)



longest = 10
longestNum = 13
curr = 13

while curr<890000:
    currRun = recurse(curr,2)



    if(longest<currRun):
        longest = currRun
        longestNum = curr
    curr = curr + 2

print(longestNum)
print(longest)