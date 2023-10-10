// 026 Power Two(pairSummingToPowerOfTwo)
// Give a array of integers, find all the pairs that the sum of them is the power of 2.
// find out all the possible pairs. and if there is any duplicates, then count them as the new one.

// using unordered map

public long pairSummingToPowerOfTwo(vector<int> a){
        
        unordered_map<int,int> mymap;
        unordered_map<int,int> powers2;
        
        for(int x:a)  mymap[x]++;
        
        long ans=0;
        for(int x:a){// need 0<=y<x
            int y=nextpower2(x)-x;            
            if(x==0)  continue;
            if(y==0)  powers2[x]++;

            ans+=mymap[y];
        }
        for(auto it=powers2.begin();it!=powers2.end();++it)
            ans+=it->second*(it->second+1)/2;
        
        return ans;
    }
  
  public int nextpower2(int v){//fast bit trick to get the next power of two
     v--;
     v |= v >> 1;
     v |= v >> 2;
     v |= v >> 4;
     v |= v >> 8;
     v |= v >> 16;
     return v+1;
   }
};
