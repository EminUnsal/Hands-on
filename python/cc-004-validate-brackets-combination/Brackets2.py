def paraCheck( seq ):  
   while True:  
       if '()' in seq :  
           seq = seq.replace ( '()' , '' )  
       elif '{}' in seq :  
           seq = seq.replace ( '{}' , '' )  
       elif '[]' in seq :  
           seq = seq.replace ( '[]' , '' )  
       else :  
           return not seq  
  
seq1 =  "()"      
print(paraCheck(seq1))  
seq2 = "()[]{}"  
print(paraCheck(seq2))  
seq3 = "(]"
print(paraCheck (seq3)) 
seq4 = "([)]"
print(paraCheck(seq4))
seq5 = "{[]}"
print(paraCheck(seq5))
seq6 = ""
print(paraCheck(seq6))