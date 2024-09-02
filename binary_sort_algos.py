
#Task 1: Binary Search Algorithim & Sorting

#Binary Search

# arr = [1, 2, 3, 5, 34, 55, 83]

# target = 5

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid # Return the index if the target has been acquired
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 #if target is not found

#print(binary_search(arr, target))
# Solution is idx 3 for example implemented

#-----------------------------------------------------------------------------------

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def merge_sorted(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sorted(left_half)  # Recursively sort the left half
        merge_sorted(right_half)  # Recursively sort the right half

        # Merge the two halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

#target_title = "The Art of Coding"

def search_video(video_titles, target_title):
    # Step 1: Sort the list using merge sort
    sorted_titles = merge_sorted(video_titles)
    
    # Step 2: Perform binary search on the sorted list
    result_index = binary_search(sorted_titles, target_title)
    
    if result_index != -1:
        return sorted_titles[result_index]
    else:
        return "Video not found"


#print(search_video(video_titles, target_title))