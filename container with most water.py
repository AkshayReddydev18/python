def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate the area
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_water = max(max_water, area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage:
heights = [1,8,6,2,5,4,8,3,9,7]
print(max_area(heights))  # Output: 49