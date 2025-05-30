



def count_subarrays_with_sum_at_least_x(arr, x):
    n = len(arr)
    count = 0
    left = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += arr[right]

        while curr_sum >= x:
            # Every subarray from current 'left' to 'right' is valid
            count += n - right
            curr_sum -= arr[left]
            left += 1

    return count

arr = [1, 2, 3, 4]
x = 5
# Valid subarrays: [2,3], [3,4], [1,2,3], [2,3,4], [1,2,3,4],
# Total = 5
print(count_subarrays_with_sum_at_least_x(arr, x))  