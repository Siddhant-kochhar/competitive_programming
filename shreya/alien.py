# import sys

# def alien(N, Pulses):
#     """
#     Find the total number of stable signal segments in the transmission.
#     A stable segment is a subarray where each unique element appears exactly 3 times.
#     """
#     count = 0
    
#     # Try all possible starting positions
#     for i in range(N):
#         freq = {}  # frequency map for current subarray
#         freq_count = {}  # count of how many elements have each frequency
        
#         # Extend subarray from position i
#         for j in range(i, N):
#             element = Pulses[j]
            
#             # Update frequency tracking
#             if element in freq:
#                 old_freq = freq[element]
#                 new_freq = old_freq + 1
                
#                 # Update freq_count
#                 freq_count[old_freq] -= 1
#                 if freq_count[old_freq] == 0:
#                     del freq_count[old_freq]
                    
#                 freq_count[new_freq] = freq_count.get(new_freq, 0) + 1
#                 freq[element] = new_freq
#             else:
#                 freq[element] = 1
#                 freq_count[1] = freq_count.get(1, 0) + 1
            
#             # Check if current subarray is stable
#             # All elements should have frequency exactly 3
#             if len(freq_count) == 1 and 3 in freq_count:
#                 count += 1
    
#     return count

# def main():
#     N = int(sys.stdin.readline().strip())
#     Pulses = []
    
#     for i in range(N):
#         Pulses.append(int(sys.stdin.readline().strip()))
    
#     result = alien(N, Pulses)
#     print(result)

# if __name__ == "__main__":
#     main()



# import sys
# from collections import defaultdict

# def alien(N, Pulses):
#     """
#     Highly optimized solution using mathematical properties.
#     Key insight: A stable segment of length L must have exactly L/3 unique elements.
#     """
#     count = 0
    
#     # For each starting position
#     for i in range(N):
#         freq = defaultdict(int)
#         unique_count = 0
        
#         # Try extending from position i
#         for j in range(i, N):
#             element = Pulses[j]
            
#             # Add current element
#             if freq[element] == 0:
#                 unique_count += 1
#             freq[element] += 1
            
#             # Early termination: if any element appears > 3 times
#             if freq[element] > 3:
#                 break
            
#             # Current segment length
#             length = j - i + 1
            
#             # Quick check: length must be multiple of 3
#             if length % 3 != 0:
#                 continue
            
#             # Expected number of unique elements
#             expected_unique = length // 3
            
#             # Quick check: if we have more unique elements than expected
#             if unique_count > expected_unique:
#                 continue
            
#             # Check if this is a stable segment
#             if unique_count == expected_unique:
#                 # Verify all elements have frequency exactly 3
#                 if all(freq[el] == 3 for el in freq):
#                     count += 1
    
#     return count

# def main():
#     N = int(sys.stdin.readline().strip())
#     Pulses = []
    
#     for i in range(N):
#         Pulses.append(int(sys.stdin.readline().strip()))
    
#     result = alien(N, Pulses)
#     print(result)

# if __name__ == "__main__":
#     main()




import sys

def alien(N, Pulses):
    """
    Correct and optimized solution for stable segments.
    A stable segment is where each unique element appears exactly 3 times.
    """
    count = 0
    
    # Try all possible starting positions
    for i in range(N):
        freq = {}
        
        # Try all possible ending positions from i
        for j in range(i, N):
            element = Pulses[j]
            
            # Update frequency
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1
            
            # Early termination: if any element appears more than 3 times
            if freq[element] > 3:
                break
            
            # Only check for stability if length is multiple of 3
            length = j - i + 1
            if length % 3 == 0:
                # Check if current subarray [i:j+1] is stable
                # All unique elements must have frequency exactly 3
                all_have_freq_3 = True
                for val in freq:
                    if freq[val] != 3:
                        all_have_freq_3 = False
                        break
                
                if all_have_freq_3:
                    count += 1
    
    return count

def main():
    N = int(sys.stdin.readline().strip())
    Pulses = []
    
    for i in range(N):
        Pulses.append(int(sys.stdin.readline().strip()))
    
    result = alien(N, Pulses)
    print(result)

if __name__ == "__main__":
    main()






























