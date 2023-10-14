
#this class finds the set of characters within a string that result in an incorrect output
class testProcessString:
    
    def __init__(self):
        self.errorSet = []

    #converts a string's uppercase values into lowercase values and vice-versa
    def processString(self, input_str):
        output_str = ""
        for char in input_str:
            if char.isupper():
                output_str += char.lower()
            elif char.isnumeric():
                output_str += char * 2
            else:
                output_str += char.upper()
        return output_str
    
    #uses binary search on an input to determine the characters in the string that cause the errors 
    def deltaDebug(self, str, i):
        #if the sting is empty just return
        if len(str) == 0:
            return
        #elif the string has one character and causes an error, add that character to the error set if it is not already in it
        elif len(str) == 1 and len(str) != len(self.processString(str)):
            if str not in self.errorSet: self.errorSet.append(str)
            return
        #elif the string generates an error
        elif len(str) != len(self.processString(str)):
            self.deltaDebug(str[:(len(str)) // 2], i+1)   #checks the left half of the string
            self.deltaDebug(str[(len(str)) // 2:], i+1)   #checks the right half of the string
        
        #if this is the end of the root level, print error set and clear error set
        if i == 0: 
            print(f"Error Set for {str}: {self.errorSet} \n")
            self.errorSet = []
        
        return

   
test = testProcessString()          #creates instance of testProcessString class

#tests various inputs to find the error sets within them
test.deltaDebug("abcdefG1", 0)      
test.deltaDebug("CCDDEExy", 0)
test.deltaDebug("1234567b", 0)
test.deltaDebug("8665", 0)
                
    
