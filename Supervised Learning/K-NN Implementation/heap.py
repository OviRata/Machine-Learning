#max heap

class Heap():
    heap=[];
    n=0;
    def __init__(self):
        self.n=1;
        self.heap=[0];
    
    # Complexity: O(log(n) )
    def insert(self, x):
        self.heap.append(x);
        self.n+=1;
        cr=self.n-1;
        while cr>1:
            up=int(cr/2);
            up1=self.heap[up]; cr1=self.heap[cr];
            if up1<cr1:
                self.heap[cr]=up1;
                self.heap[up]=cr1;
            else:
                break;
            cr=up;

    #Complexity: O(log(n) )
    def erase_root(self):
  
        
        if self.n<2:
            return ;

        self.heap[1]=self.heap[self.n-1];
        cr=1;
        self.n-=1;
        self.heap.pop();
        lt=rt=lt1=rt1=cr1=-1;
        while (cr*2+1)<self.n:
            lt=cr*2; rt=cr*2+1;
            lt1=self.heap[lt]; rt1=self.heap[rt];
            cr1=self.heap[cr];
            if (rt1>lt1) and (rt1>cr1):
                self.heap[cr*2+1]=cr1;
                self.heap[cr]=rt1;
                cr=rt;
            elif (  lt1>cr1  ):
                self.heap[cr*2]=cr1;
                self.heap[cr]=lt1;
                cr=lt;
            else:
                break;
      
        if (cr*2<self.n) and (self.heap[cr*2]>self.heap[cr]):
            temp=self.heap[cr*2];
            self.heap[cr*2]=self.heap[cr];
            self.heap[cr]=temp;
            cr=cr*2;

    #Complexity: O(1)
    def get_max(self):
        return self.heap[1];
    
    #Complexity: O(1)
    def size(self):
        return self.n;

    
"""
h=Heap();
h.insert(1);
h.insert(5);
h.insert(3);
print(h.get_max() );
h.erase_root();
print(h.get_max() );
"""