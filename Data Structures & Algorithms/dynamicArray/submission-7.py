import ctypes
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.A=(self.capacity * ctypes.py_object)()
        self.size=0
    def get(self, i: int) -> int:
        return self.A[i]

    def set(self, i: int, n: int) -> None:
        self.A[i]=n

    def pushback(self, n: int) -> None:
        if self.size==self.capacity:
            self.resize()
        self.A[self.size]=n  
        self.size+=1      
    def popback(self) -> int:
        last=self.A[self.size-1]
         
        self.size-=1
        return last
    def resize(self) -> None:
        newCapacity = self.capacity*2
        B=(newCapacity * ctypes.py_object)()
        
        for k in range(0,self.capacity):
            B[k]=self.A[k]
        self.A=B 
        self.capacity=newCapacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity


