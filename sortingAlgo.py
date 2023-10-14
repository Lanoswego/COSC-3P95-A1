class sortingAlgo:
    """This class sorts a given list using on of two methods. The method used is determined by the value passed"""

    #This method sorts the list of integers excluding positions with 3 ("bug" that ignores 3's in the list)
    def altSort(self, list):
        listSize = len(list)        #size of the original list
        indicies = []               #list of positions in the list that are 3
        leftover = []               #list of items from the list that are not 3
        result = []                 #resulting "sorted" list of integers

        #checks the pairs of [index, int] for the list and adds the index number to the indicies list if int = 3. Otherwise it adds the int to the leftovers list
        for pair in enumerate(list):
            if pair[1] == 3:
                indicies.append(pair[0])
            else:
                leftover.append(pair[1])
        
        if len(indicies) == 0: return sorted(leftover)      #if there are no 3's in the list, simply return the sorted list

        leftover.sort()     #sorts the leftover integers from the list

        currentPos = 0      #current position in the results list
        indPos = 0;         #current position in the indicies list
        
        
        #generates a new list by placing the value in sorted order around the positions of any 3 in the original list
        while currentPos < listSize:
            
            #if this position had a 3 in the original list, then place three for that position in the result list
            #else take the int at the start of the leftover list and place at the current position in the result list
            if currentPos == indicies[indPos]:
                result.append(3)                                        #adds 3 to the result list
                if indPos < len(indicies)-1 : indPos = indPos + 1       #increases indicies position
            else:
                result.append(leftover.pop(0))              #takes int from the beginning of the leftover list and adds it to the result list

            currentPos = currentPos + 1                     #increases result list position
        
        return result