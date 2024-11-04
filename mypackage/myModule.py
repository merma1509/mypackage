def top_n(items, n):
    """
    Return the top n items in the list in the descending other
    
    Args:
       items (list): A list of items
       n (int): The number of top items to return
       
    Return:
    list: The top n items in the list in descending order
    
    Examples:
    >>> top_n([1, 2, 3, 4, 5],3)
    [5, 4, 3]
    """
    for  i in range(n): # keep sorting until we have  n items
        for j in  range(len(items)-1-i):
            if items[j] > items[j+1]: # Checking if the current item is bigger than the next one
                items[j], items[j+1] = items[j+1], items[j] # if True, Swap between two items
        
    # print the top last n items            
    top_n = items[-n:]
    
    return top_n[::-1] # return the descending order  
print(top_n([1, 2, 3, 4, 5],3))