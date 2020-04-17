
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
    

  
  


  
  
    
    
    