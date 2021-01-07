Task02
class Node:
    def __init__(self,value):
        self.value=value
        self.ref=None
class Stack:
    head=None
    s=0
    def push(self,data):
        self.s+=1
        if self.head==None:
            self.head=Node(data)
        else:
            n = Node(data)
            n.ref=self.head
            self.head=n
    def peek(self):
        return self.head.value
    def pop(self):
        if self.s==0:
            print("Underflow")
            return
        self.s-=1
        temp=self.head
        self.head=self.head.ref
        temp.value=None
        temp.ref=None
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
st = Stack()
a=st.findout('1+2*(3/4)')
print()
st = Stack()
a=st.findout('1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
print()
st = Stack()
a=st.findout('1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14')
print()
st = Stack()
a=st.findout('1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14')
