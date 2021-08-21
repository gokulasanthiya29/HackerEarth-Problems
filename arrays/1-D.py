n = int(input())
arr = [ int(input()) for i in range(n) ]
store = arr[::-1]

for item in store:
    print(item)
