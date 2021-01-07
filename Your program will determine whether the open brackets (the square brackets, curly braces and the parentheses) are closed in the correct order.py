class Array:
    array=[]
    indicator=-1
    s=0
    def push(self,element):
        self.array+=[element]
        self.indicator+=1
        self.s+=1
    def peek(self):
        return self.array[self.indicator]
    def pop(self):
        value=self.array[self.indicator]
        self.array=self.array[:-1]
        self.s-=1
        self.indicator-=1
        return value
    def khali(self):
        if self.s==0:
            return True
        else:
            return False
    
    '''def print_array(self):
        i=0
        while  i<=self.indicator:
            print(self.array[i])
            i+=1 '''
    
    def empty(self):
        self.array = []
        self.indicator = -1
        self.s = 0 
        

    def findout(self,word):
        positionArray=[]
        khulo = ["[","{","("] 
        bondho_koro = ["]","}",")"]
        for i in range(len(word)): 
            if word[i] in khulo: 
                self.push(word[i])
                positionArray+=[i+1]
                
            elif word[i] in bondho_koro: 
                loc = bondho_koro.index(word[i])
                if ((self.s > 0) and (khulo[loc] == self.peek())): 
                    self.pop() 
                elif (self.s > 0) and (khulo[loc] != self.peek()):
                    print("This expression is NOT correct.")
                    print('Error at character #',positionArray[self.s-1],".'" ,self.peek(),"'-is not closed",sep='')
                    return
                    
                else:
                    print("This expression is NOT correct.")
                    print('Error at character #',i+1,".'" ,word[i],"'-is not opened",sep='')
                    return
        if self.s == 0: 
            print("This expression is correct.")
            return
        else:
            print("This expression is NOT correct.")
            print('Error at character #',positionArray[self.s-1],".'" ,self.peek(),"'-is not closed",sep='')
            return

stack_2 = Array()
stack_2.findout('1+2*(3/4)')
stack_2.empty()
print()
stack_2.findout('1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
stack_2.empty()
print()
stack_2.findout('1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14')
stack_2.empty()
print()
stack_2.findout('1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
stack_2.empty()
print()
