'''
arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3
'''

from collections import defaultdict
import heapq

arr = [4, 7, 6, 4, 5, 4, 3, 8, 10]
k = 2
res = 0

count = defaultdict(int)
freq_heap = []  # max heap for frequencies (using negative values)
modes = []

# Calculate frequency for the first window
for i in range(k):
    count[arr[i]] += 1

# Build initial heap with frequencies (negative for max heap)
for freq in count.values():
    heapq.heappush(freq_heap, -freq)

# Find mode for first window
max_freq = -freq_heap[0]  # Convert back from negative
mode = min(element for element, freq in count.items() if freq == max_freq)
modes.append(mode)
res += mode

# Slide the window for remaining positions
for left in range(1, len(arr) - k + 1):
    # Remove the element going out of window
    outgoing = arr[left - 1]
    old_freq = count[outgoing]
    count[outgoing] -= 1
    
    # Add the new element coming into window
    incoming = arr[left + k - 1]
    count[incoming] += 1
    new_freq = count[incoming]
    
    # Rebuild heap with current frequencies
    freq_heap = []
    for element, freq in count.items():
        if freq > 0:  # Only add elements still in window
            heapq.heappush(freq_heap, -freq)
    
    # Find mode for current window
    max_freq = -freq_heap[0] if freq_heap else 0
    mode = min(element for element, freq in count.items() if freq == max_freq and freq > 0)
    modes.append(mode)
    res += mode
    
    # Clean up zero frequencies
    if count[outgoing] == 0:
        del count[outgoing]


return res