class MyQueue {
public:
int q[100];
int f=0;
int r=0;
    MyQueue() {
        
    }  
    void push(int x) {
        if(r!=200){
            q[r]=x;
            r++;
        }      
    }
    
    int pop() {
        if(empty())
        {
            return false;
        }
        else{
            f++;
            return q[f-1];
        }
    }
    int peek() {
        return q[f];
        
    }
    
    bool empty() {
        if(f==r)
        {
            f=0;
            r=0;
            return true;
        }
        return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */