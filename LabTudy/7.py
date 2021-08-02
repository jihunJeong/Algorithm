arr = list(map(int, list(input())))
length = len(arr)

if sum(arr[:length//2]) == sum(arr[length//2:]):
    print("LUCKY")
else :
    print("READY")