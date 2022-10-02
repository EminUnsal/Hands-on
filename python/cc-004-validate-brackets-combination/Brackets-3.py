def validBraces(iterable):
      while "{}" in iterable or "()" in iterable or "[]" in iterable:

            iterable = iterable.replace("{}","")
            iterable = iterable.replace("[]","")
            iterable = iterable.replace("()","")
      return iterable == ""

seq1 =  "()"      
print(validBraces(seq1))  
seq2 = "()[]{}"  
print(validBraces(seq2))  
seq3 = "(]"
print(validBraces(seq3)) 
seq4 = "([)]"
print(validBraces(seq4))
seq5 = "{[]}"
print(validBraces(seq5))
seq6 = ""
print(validBraces(seq6))