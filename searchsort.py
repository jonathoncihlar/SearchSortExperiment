
""" searchsort.py
This Python file contains implementations of classic search and sort 
algorithms so that students can empirically find the growth of the 
worst case running time of each. There are no classes associated - this
file is just a collection of functions.
"""


def buildList(listSize, reverse=False):
  """Constructs a list of integers per the reverse flag. The integers 
    range from 1 to listSize (or vice versa).
    
    Parameters
    ----------
    listSize : int
      The size of the list to create, restricted between 10 and 100,000,000
    reverse : boolean, optional
      Whether to create the list in reverse order (default is False).
    """
    
    # create the list
  if (reverse):
    return [x for x in range(abs(listSize), 0, -1)] 
  else: 
    return [x for x in range(1, abs(listSize)+1)]    
def linearSearch(list, target):
  """Conducts a linear search looking for an item in a slist.
    
    Parameters
    ----------
    list : int[]
      A list of integers to search through - does not need to be sorted
    target : int
      The integer to find in `list`
    
    Returns
    -------
    index : int
      the index where the item is located, None if not found
    """
  
  for index in range(0, len(list)):
    if(list[index] == target):
      return index
      
  return None ## return None if target is not found
         
def binarySearch(list, target):
  """Conducts a binary search looking for an item in a sorted list.
    
    Parameters
    ----------
    list : int[]
      A list of integers to search through - needs to be sorted
      ascending.
    target : int
      The integer to find in `list`
    
    Returns
    -------
    index : int
      the index where the item is located, None if not found
    """
    # use low and high to keep track of where in the list we are
    # start off with the entire list
  low = 0 
  high = len(list) - 1
   # when low and high are next to each other, then we've
   # run the list and should quit
  while (low != high):
    index = int(low + high / 2) # find the middle element of our list
      # if we found the target, then return
    if (list[index] == target): # if we found the target, then return
      return index
      # if what we found is lower than the target, then adjust the 
      # low bound to look at the lower 
    if (list[index] < target):
      low = index 
    
    else:
      high = index
    
    # if we get this far, we didn't find the target so return -1 
  return None
    
def bubbleSort(list):
  """Conducts a bubble sort.
    
    Parameters
    ----------
    list : int[]
      A list of integers to sort.
    
    Returns
    -------
    list : int[]
      The sorted list
    """
  swapped = True # set the swapped flag to true in order to get one pass
    # repeat sorting until no swaps happen on an iteration 
  while (swapped):
    swapped = False # set the flag to false before another iteration
    for i in range (0, len(list)-1):
         # if the elements are out of order, then swap them
      if (list[i] > list[i+1]):
        list[i], list[i+1] = list[i+1], list[i]
        swapped = True # set the flag to true to fire another iteration
        
  return list # return the list when the loop finishes
  
def mergeSort(list):
  """Conducts a merge sort using recursion.
    
    Parameters
    ----------
    list : int[]
      A list of integers to sort.
    
    Returns
    -------
    list : int[]
      The sorted list
    """
    # define base case to end recursion
  if (len(list) <= 1):
    return list

    # split list into left and right
  middle = int(len(list) / 2) # grab the middle
  left = list[:middle] # slice
  right = list[middle:] # slice
  
    # recursively call the function
  left = mergeSort(left)
  right = mergeSort(right)

    # if one of the lists is none, then 
    # simply return the list that is valid
  if left is None or right is None:
    return left or right

    # merge the left and right lists together
    # figure out how many elementss to merge
  merged =[None] * (len(left) + len(right))
  lIndex = rIndex = mIndex = 0
    # do the merge by examining the left and right arrays
    # in order
  while (lIndex < len(left) and rIndex < len(right)):
      # if the item in the left side come first
      # add it to the merged array
    if (left[lIndex] < right[rIndex]):
      merged[mIndex] = left[lIndex]
      lIndex += 1 # move the left index
      # otherwise use the right index
    else:
      merged[mIndex] = right[rIndex]
      rIndex += 1
    mIndex += 1

    # pick up elements from unfinished arrays
    # only one of these will trigger
  while (lIndex < len(left)):
    merged[mIndex] = left[lIndex]
    lIndex += 1
    mIndex += 1

  while (rIndex < len(right)):
    merged[mIndex] = right[rIndex]
    rIndex += 1
    mIndex += 1
  
  return merged
    
        
    