# Generate all subsets using backtracking

def subsets(arr, index, current):
    if index == len(arr):
        print(current)
        return
    
    # include
    subsets(arr, index+1, current + [arr[index]])
    
    # exclude
    subsets(arr, index+1, current)

arr = list(map(int, input("Enter elements: ").split()))
subsets(arr, 0, [])