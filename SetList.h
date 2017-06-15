#include <iterator> 
#include <algorithm> 
#include <iostream>
#include <vector>
#include <fstream>
#include <set>
#include <string> 
using namespace std; 

template <typename Type>
class SetList
{
  private:
  
    struct ListNode 
 	  { 
 		    Type info; 
 		    ListNode * next; 
 		    ListNode(Type newInfo, ListNode * newNext) : info( newInfo ), next( newNext ) 
 		    { 
 		    } 
 	  }; 
    ListNode * head;
    static ListNode * reverse(ListNode * L)
    {
        ListNode * result = '\0';
        for ( ListNode * p = L; p != '\0'; p = p->next )
        {  
            result = new ListNode( p->info, result );
        }
        return result;
    }
    static ListNode * copy(ListNode * L) 
 	  { 
        return L == NULL ? NULL : new ListNode(L->info, copy(L->next));
 	  } 
    static int length(ListNode * L) 
 	  { 
        return L == 0 ? 0 : 1 + length(L -> next);
	  } 
    static ListNode * concat(ListNode * L1, ListNode * L2) 
 	  {          
        return L1 == NULL ? NULL : new ListNode(L1->info, concat(L1->next, L2));
 	  } 
     static ListNode * append(ListNode * L1, ListNode * L2) 
    { 
 	      return L1 == NULL ? copy(L2) : new ListNode ( L1 -> info, append(L1 -> next, L2));
    } 
    static void deleteList(ListNode * L)
    {
        if (L != NULL)
        {
            deleteList( L -> next);
            delete L;
        }
    }
    
  public:
  
    struct iterator 
 	  { 
 		    typedef forward_iterator_tag iterator_category; 
        typedef iterator self_type; 
 		    typedef ListNode value_type; 
 		    typedef ListNode & reference; 
 		    typedef ListNode* pointer; 
                    
      private: 
      
        ListNode * buf;
        
      public:
      
        iterator(ListNode * ptr) : buf( ptr ){} 
 	      self_type operator++()
        { 
            buf = buf->next; 
            return *this; 
        } 
 		    self_type operator++(int postifx) 
        {
            self_type cpy = *this; 
            buf = buf->next; 
            return cpy;
        }  
 		    reference operator*()
        { 
            return buf->info; 
        } 
 		    pointer operator->()
        { 
            return buf; 
        } 
        self_type operator+(int i) 
        { 
            int count;
            self_type temp = *this; 
            temp += i; 
            count++;
            return temp; 
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
            self_type temp = *this; 
            count++;
            temp -= i; 
            return temp; 
        } 
       
        self_type operator-=(int i) 
        { 
            int count;
            buf -= i; 
            count++;
            return *this; 
        } 
 		    bool operator == (const self_type & rhs) const 
        {
            return buf == rhs.buf;
        } 
 		    bool operator != (const self_type & rhs) const 
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
     
   struct const_iterator 
 	 { 
 		   typedef std::forward_iterator_tag iterator_category; 
 		   typedef const_iterator self_type; 
 		   typedef Type value_type; 
 		   typedef Type& reference; 
 		   typedef Type* pointer; 
          
     private:
     
       ListNode * buf;
       
     public:
     
       const_iterator(ListNode * ptr) : buf(ptr){} 
 		   self_type operator+()
       { 
           buf = buf->next; 
           return *this; 
       } 
 		   self_type operator++(int postfix)
       {
           self_type cpy = *this; 
           buf = buf->next; 
           return cpy;
       } 
 		   const reference operator*()
       {
           return buf->info;
       } 
 		   const pointer operator->()
       {
           return buf;
       } 
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
 		   bool operator == (const self_type& rhs)const
       {
           return buf == rhs.buf;
       } 
 		   bool operator != (const self_type& rhs)const
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
    
    SetList() 
 	  { 
 		    head = NULL; 
 	  } 
      
    SetList(initializer_list<Type> s)
    {
        head = NULL;
    }
    
    iterator begin() 
 	  { 
 		    return iterator(head); 
 	  } 
 	  iterator end() 
 	  { 
 		    return iterator(NULL); 
 	  } 
 	  const_iterator begin() const 
 	  { 
 		    return const_iterator(head); 
 	  } 
 	  const_iterator end() const 
 	  { 
 		    return const_iterator(NULL); 
 	  }  

    iterator insert(const Type & x) 
 	  { 
 		    if(find(x) == NULL) 
 		    { 
            int count;
 			      if(head != NULL && head->info <= x) 
 				    {
                int num;
                ListNode * current;
                current = head; 
 				        while(current-> next != NULL && current->next->info < x) 
 					      {
                    num = num + 1;
                    current = current->next; 
 				            current->next = new ListNode(x, current->next); 
                }
            }
 			      else if ( head == NULL || head -> info > x)
 			      { 
                count = count + 1;
 				        head = new ListNode(x, head); 
	          } 
 		    } 
 	  } 
      
    iterator find(const Type & x) 
 	  { 
        int count;
        ListNode * p;
 		    for(p = head; p != NULL; p = p->next) 
 		    { 
 			      if( p->info == x ) 
 				    {    
                count = count + 1;
                return iterator(p); 
            }
 		    } 
        return NULL; 
 	  } 
      
    ~SetList() 
 	  { 
 		    deleteList(head);
 	  }
}; 