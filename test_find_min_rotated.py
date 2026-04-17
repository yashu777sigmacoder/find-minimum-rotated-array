"""
Performance comparison and testing for finding minimum in rotated sorted array
"""

import time
import random
from find_min_rotated_array import (
    find_min_linear,
    find_min_iteration,
    find_min_rotation_point,
    find_min_binary_search,
    find_min_binary_search_duplicates,
    find_min_recursive
)


def measure_time(func, arr):
    """Measure execution time of a function"""
    try:
        start = time.time()
        result = func(arr)
        end = time.time()
        return result, end - start
    except Exception as e:
        return None, str(e)


def run_tests():
    """Run comprehensive tests and comparisons"""
    
    test_cases = [
        ("Empty array", []),
        ("Single element", [5]),
        ("Two elements", [2, 1]),
        ("Not rotated (sorted)", [1, 2, 3, 4, 5]),
        ("Rotated once", [2, 3, 4, 5, 1]),
        ("Rotated multiple times", [4, 5, 1, 2, 3]),
        ("Rotated at start", [5, 1, 2, 3, 4]),
        ("All duplicates", [3, 3, 3, 3, 3]),
        ("Duplicates with rotation", [3, 1, 3, 3, 3]),
        ("Large rotated array", list(range(500, 1000)) + list(range(1, 500))),
        ("Negative numbers", [-2, -1, 0, 1, 2, 3]),
        ("Rotated negatives", [0, 1, 2, 3, -2, -1]),
        ("Mixed pos/neg rotated", [2, 3, 4, -3, -2, -1]),
    ]
    
    algorithms = [
        ("Linear Search", find_min_linear),
        ("Iteration", find_min_iteration),
        ("Rotation Point", find_min_rotation_point),
        ("Binary Search", find_min_binary_search),
        ("Binary Search + Duplicates", find_min_binary_search_duplicates),
        ("Recursive Binary Search", find_min_recursive),
    ]
    
    results = []
    results.append("=" * 120)
    results.append("FIND MINIMUM IN ROTATED SORTED ARRAY - ALGORITHM COMPARISON")
    results.append("=" * 120)
    results.append("")
    
    # Test correctness
    results.append("[1] CORRECTNESS TESTING")
    results.append("=" * 120)
    
    for test_name, test_arr in test_cases:
        if not test_arr:
            expected = None
        else:
            expected = min(test_arr)
        
        results.append(f"\nTest: {test_name}")
        if len(str(test_arr)) > 70:
            results.append(f"  Input: {str(test_arr)[:67]}...")
        else:
            results.append(f"  Input: {test_arr}")
        results.append(f"  Expected: {expected}")
        results.append(f"  {'Algorithm':<30} {'Result':<15} {'Status':<10}")
        results.append(f"  {'-' * 55}")
        
        for algo_name, algo_func in algorithms:
            result, exec_time = measure_time(algo_func, test_arr)
            
            if isinstance(exec_time, str):
                status = "ERROR"
            elif result == expected:
                status = "PASS"
            else:
                status = "FAIL"
            
            results.append(f"  {algo_name:<30} {str(result):<15} {status:<10}")
    
    # Performance comparison
    results.append("\n\n" + "=" * 120)
    results.append("[2] PERFORMANCE TESTING (Speed Comparison)")
    results.append("=" * 120)
    
    perf_test_sizes = [100, 1000, 10000, 100000]
    
    for size in perf_test_sizes:
        results.append(f"\n\nArray Size: {size} elements")
        results.append(f"{'Algorithm':<30} {'Time (seconds)':<20} {'Speed':<15}")
        results.append(f"{'-' * 65}")
        
        # Create test array
        mid = size // 2
        test_arr = list(range(mid, size)) + list(range(0, mid))
        
        times = {}
        for algo_name, algo_func in algorithms:
            _, exec_time = measure_time(algo_func, test_arr)
            if isinstance(exec_time, str):
                times[algo_name] = float('inf')
            else:
                times[algo_name] = exec_time
        
        # Find fastest
        fastest_time = min(times.values())
        
        for algo_name, _ in algorithms:
            exec_time = times[algo_name]
            if isinstance(exec_time, float) and exec_time != float('inf'):
                speedup = exec_time / fastest_time if fastest_time > 0 else 0
                results.append(f"{algo_name:<30} {exec_time:.8f} seconds   {speedup:.2f}x")
            else:
                results.append(f"{algo_name:<30} ERROR")
    
    # Best algorithm analysis
    results.append("\n\n" + "=" * 120)
    results.append("[3] ALGORITHM ANALYSIS & RECOMMENDATION")
    results.append("=" * 120)
    
    analysis = """
LINEAR SEARCH
  Time: O(n) | Space: O(1)
  Pros: Simple, works on unsorted arrays
  Cons: Slowest for large arrays
  
ITERATION  
  Time: O(n) | Space: O(1)
  Pros: Simple, easy to understand
  Cons: Slower than binary search, O(n) complexity
  
ROTATION POINT SEARCH
  Time: O(n) | Space: O(1)
  Pros: Finds rotation point
  Cons: Still O(n), slower than binary search
  
BINARY SEARCH (OPTIMAL)
  Time: O(log n) | Space: O(1)
  Pros: FASTEST, O(log n) complexity, efficient
  Cons: Requires sorted array structure
  
BINARY SEARCH WITH DUPLICATES
  Time: O(log n) avg, O(n) worst | Space: O(1)
  Pros: Handles duplicates, efficient
  Cons: Worst case O(n) with many duplicates
  
RECURSIVE BINARY SEARCH
  Time: O(log n) | Space: O(log n) recursion stack
  Pros: Clean, recursive implementation
  Cons: Extra space for recursion stack

RECOMMENDATION: BINARY SEARCH
  * 100-1000x FASTER than linear search
  * O(log n) time complexity - optimal for this problem
  * O(1) space complexity - no extra space needed
  * Best balance of speed and simplicity
  * Use Binary Search with Duplicates if array may have duplicates
"""
    
    results.extend(analysis.split("\n"))
    
    results.append("\n" + "=" * 120)
    
    return "\n".join(results)


if __name__ == "__main__":
    output = run_tests()
    
    # Print to console
    print(output)
    
    # Save to file
    with open("find_min_rotated_comparison.txt", "w", encoding="utf-8") as f:
        f.write(output)
    
    print("\n[SUCCESS] Results saved to 'find_min_rotated_comparison.txt'")
