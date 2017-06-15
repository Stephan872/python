#include <iostream> 
#include <iterator> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <fstream>
#include <set>
using namespace std; 

class MapArray 
{ 
  private: 
  
 	  int count; 
    int len;
 	  pair<string, int> * buf; 
      
  public:
  
    struct iterator 
 	  { 
        typedef std::forward_iterator_tag iterator_category; 
 		    typedef iterator self_type; 
 		    typedef pair<string, int> value_type; 
 		    typedef pair<string, int>& reference; 
 		    typedef pair<string, int>* pointer;  
            
      private:
      
        pointer buf;
        
      public: 
      
       iterator(pointer ptr) : buf(ptr) { } 
 		   
       self_type operator+(int i) 
       { 
           int count;
           self_type x = *this; 
           x += i; 
           count++;
           return x; 
       } 
       self_type operator+=(int i) 
       { 
           int count;
           buf += i;
           count++; 
           return *this; 
       } 
       self_type operator-(int i) 
       { 
           int count;
           self_type x = *this; 
           count++;
           x -= i; 
           return x; 
       } 
       self_type operator-=(int i) 
       { 
           int count;
           buf -= i; 
           count++;
           return *this; 
       } 
 		   reference operator*() 
       { 
           return *buf; 
       } 
 		   pointer operator->() 
       { 
           return buf; 
       } 
       
       self_type operator++() 
       { 
           int num;
           ++buf; 
           num++;
           return *this; 
       } 
 		   self_type operator++(int postfix) 
       { 
           int num;
           self_type cpy = *this; 
           num++;
           buf++; 
           return cpy; 
       } 
       self_type operator--() 
       { 
           int num;
           buf--;
           num++; 
           return *this; 
       } 
 		   self_type operator--(int postfix) 
       { 
           int num;
           self_type cpy = *this;
           num++; 
           buf--; 
           return cpy; 
       } 
 	 	   bool operator == (const self_type& rhs) const 
       { 
           return buf == rhs.buf; 
       } 
 		   bool operator!=(const self_type& rhs) const 
       { 
           return buf != rhs.buf; 
       }
       bool operator > (const self_type& rhs) const 
       { 
           return buf > rhs.buf; 
       } 
 		   bool operator < (const self_type& rhs) const 
       { 
           return buf < rhs.buf; 
       }
       bool operator >=( const self_type& rhs) const 
       { 
           return buf >= rhs.buf; 
       } 
 		   bool operator <= (const self_type& rhs) const 
       { 
           return buf <= rhs.buf; 
       }
   };
   
   struct const_iterator 
 	 { 
     public: 
     
 		   typedef std::forward_iterator_tag iterator_category; 
 		   typedef const_iterator self_type; 
 		   typedef pair<string, int> value_type; 
 		   typedef pair<string, int>& reference; 
 		   typedef pair<string, int>* pointer; 
 		   typedef ptrdiff_t difference_type; 
          
     private: 
     
 		   pointer buf; 
          
     public: 
     
 		   const_iterator(pointer ptr) : buf(ptr) { } 
 		   
 		   const reference operator*() 
       { 
           return *buf; 
       } 
 		   const pointer operator->() 
       { 
           return buf; 
       } 
       
       self_type operator+(int i) 
       { 
           int count;
           self_type x = *this; 
           count++;
           x += i; 
           return x; 
       } 
       
       self_type operator+=(int i) 
       { 
           int count;
           buf += i; 
           count++;
           return *this; 
       } 
       
       self_type operator-(int i) 
       { 
           int count;
           self_type x = *this; 
           x -= i; 
           count++;
           return x; 
       } 
       
       self_type operator-=(int i) 
       { 
           int count;
           buf -= i; 
           count++;
           return *this; 
       } 
       
       self_type operator++()
       { 
           int num;
           ++buf; 
           num++;
           return *this; 
       } 
 		   self_type operator++(int postfix) 
       { 
           int num;
           self_type cpy = *this; 
           num++;
           buf++; 
           return cpy; 
       } 
       self_type operator--()
       { 
           int num;
           --buf; 
           num++;
           return *this; 
       } 
 		   self_type operator--(int postfix) 
       { 
           int num;
           self_type cpy = *this; 
           num++;
           buf--; 
           return cpy; 
       } 
       
 		   bool operator==(const self_type& rhs) const 
       { 
           return buf == rhs.buf; 
       } 
 		   bool operator!=(const self_type& rhs) const 
       { 
           return buf != rhs.buf; 
       } 
       bool operator > (const self_type& rhs) const 
       { 
           return buf > rhs.buf; 
       } 
 		   bool operator < (const self_type& rhs) const 
       { 
           return buf < rhs.buf; 
       } 
       bool operator >= (const self_type& rhs) const 
       { 
           return buf >= rhs.buf; 
       } 
 		   bool operator <= (const self_type& rhs) const 
       { 
           return buf <= rhs.buf; 
       } 
   };
   
   MapArray(int size) 
 	 { 
       int number;
 		   count = 0; 
       len = size;
 		   buf = new pair<string, int>[size]; 
 	 } 
    
   iterator begin() 
 	 { 
 		   return iterator(buf); 
   } 
 	 iterator end() 
 	 { 
 		    return iterator(buf + count); 
 	 } 
 	 const_iterator begin() const 
 	 { 
 		   return const_iterator(buf); 
 	 } 
 	 const_iterator end() const 
 	 { 
 		   return const_iterator(buf + count); 
 	 }

 	 int find(string & x) 
 	 { 
       int i;
       int num;
 		   for(i = 0; i < count; i++) 
 		   { 
 			    if(buf[i].first == x) 
 				  {
              num = num + 1;
              return i;
          } 
       } 
 		   return -1; 
 	 } 
    
   int size() const 
 	 { 
 		   return count; 
	 } 
    
   int & operator [](string s) 
 	 { 
       int i;
       int num;
 		   i = find(s); 
 		   if(i != -1) 
 		   { 
           num = num + 1;
           return buf[i].second; 
 		   } 
 		   buf[count] = make_pair(s, 0);
       ++num; 
 		   int y = count; 
 		   ++count; 
 		   return buf[y].second; 
 	 } 
 	   
 	 pair<string, int> & operator [] (int index) 
 	 { 
 		   return buf[index]; 
 	 } 
 	 const pair<string, int> & operator [] (int index) const 
 	 { 
 		   return buf[index]; 
 	 } 
 	 ~MapArray() 
 	 { 
    		delete[] buf; 
 	 } 
}; 