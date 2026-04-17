"""
Find Minimum in Rotated Sorted Array
Implementations using multiple algorithms
"""


# Algorithm 1: Linear Search (Brute Force)
def find_min_linear(arr):
    """
    Find minimum in rotated sorted array using linear search.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    return min(arr)


# Algorithm 2: Iteration with Comparison
def find_min_iteration(arr):
    """
    Find minimum by iterating and comparing adjacent elements.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return None
    
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


# Algorithm 3: Find Rotation Point
def find_min_rotation_point(arr):
    """
    Find minimum by locating the rotation point.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return None
    
    n = len(arr)
    for i in range(n):
        # Check if current element is the rotation point (minimum)
        if i > 0 and arr[i] < arr[i - 1]:
            return arr[i]
    
    # If no rotation point found, array is sorted, return first element
    return arr[0]


# Algorithm 4: Binary Search (OPTIMAL)
def find_min_binary_search(arr):
    """
    Find minimum in rotated sorted array using binary search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Best for this problem!
    """
    if not arr:
        return None
    
    left, right = 0, len(arr) - 1
    
    # If array is not rotated or has one element
    if arr[left] <= arr[right]:
        return arr[left]
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid element is greater than right element,
        # minimum is in right half
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return arr[left]


# Algorithm 5: Binary Search with Duplicates Handling
def find_min_binary_search_duplicates(arr):
    """
    Find minimum in rotated sorted array with duplicates.
    Time Complexity: O(log n) average, O(n) worst case
    Space Complexity: O(1)
    """
    if not arr:
        return None
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Handle duplicates by shrinking the search space
        if arr[mid] > arr[right]:
            left = mid + 1
        elif arr[mid] < arr[right]:
            right = mid
        else:
            # arr[mid] == arr[right], shrink right to exclude duplicates
            right -= 1
    
    return arr[left]


# Algorithm 6: Recursive Binary Search
def find_min_recursive(arr, left=None, right=None):
    """
    Find minimum using recursive binary search.
    Time Complexity: O(log n)
    Space Complexity: O(log n) for recursion stack
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if not arr:
        return None
    
    # Base case: array has one or two elements
    if right - left <= 1:
        return min(arr[left], arr[right])
    
    mid = left + (right - left) // 2
    
    # If mid is greater than right, minimum is in right half
    if arr[mid] > arr[right]:
        return find_min_recursive(arr, mid + 1, right)
    else:
        # Minimum is in left half (including mid)
        return find_min_recursive(arr, left, mid)
