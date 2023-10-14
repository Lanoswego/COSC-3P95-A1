import random
import sortingAlgo as algo

class testSortingAlgo:

    def __init__(self):
        self.intList = []
        self.sortingAlgo = algo.sortingAlgo()
        return
        
    #This method generates a list of integers (between 1 and 10) where the elements of the list are randomly generated. Range of the list size is 1 to 100.
    def randomList(self):
        listSize = random.randint(1,20)     #generates a random integer between 1 and 20 for the list size

        while len(self.intList) < listSize:
            self.intList.append(random.randint(1,10))   #generates a random number between 1 and 10, and adds it to the array

        return
    
    #generates a string form of the list given
    def generateStringList(self, list):
        l = "["
    
        for num in enumerate(list):
            if num[0] == len(list) -1:
                l += f"{num[1]}"
            else:
                l += f"{num[1]}, "
        l += "]"

        return l

    
    #takes a randomly generated list, sorts it with the sorting algorithm, and checks the sorted list for errors
    def testSort(self):
        self.randomList()                                                   #generates a random list of integers
        
        print(f"Original list: {self.intList}")                             #prints the original list
        
        self.intList = self.sortingAlgo.altSort(self.intList)               #alt sorts the list

        print(f"Sorted list: {self.intList}")                               #prints the original list

        #if the list was sorted without errors print positive result, otherwise print negative result
        if self.intList == sorted(self.intList):
            print("Result: List was sorted CORRECTLY")
        else:
            print("\nResult: List was sorted INCORRECTLY")
    

test = testSortingAlgo()
test.testSort()


