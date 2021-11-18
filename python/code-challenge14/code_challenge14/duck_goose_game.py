
def duck_duck_goose(n , *strs):
    arr = [*strs]
    r = n
    while r >= len(arr):
        r -= len(arr)
    

    
    arr.remove(arr[r-1])
    
    if len(arr) != 1:
        return duck_duck_goose(n, *arr)
    
    else:
        return arr[0]

if __name__=="__main__":
    print(duck_duck_goose(5,"a","b","c"))
