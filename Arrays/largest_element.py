def find_largest(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Test the function
my_list = [10, 25, 8, 45, 30]
print(f"The largest element is: {find_largest(my_list)}")