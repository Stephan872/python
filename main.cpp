#include <iostream> 
#include <algorithm> 
#include <iterator> 
#include <string> 
#include <set> 
#include <fstream>
#include <map> 
#include "MapArray.h" 
#include "SetList.h" 

using namespace std; 

void lowerCase(string & i) 
{ 
 	std::transform(i.begin(), i.end(), i.begin(), ::tolower); 
} 

int main()
{
    SetList<string> S;
    MapArray M(10000);
    int x;
    int y;
    ifstream F1("stopwords.txt");
    for_each( istream_iterator<string>(F1), istream_iterator<string>(), [&](string i) 
    { 
        x++;
        S.insert(i); 
    }); 
    ifstream F2("sample_doc.txt");                    
    for_each( istream_iterator<string>(F2), istream_iterator<string>(), [&](string i) 
    { 
        int count;
        lowerCase(i); 
        if( S.find(i)== end(S) ) 
        { 
            count = count + 1;
            M[i] = M[i] + 1;  
        } 
    });     
         
    set<string> Set;
          
    ofstream F; 
    int num;
 		F.open("frequency.txt"); 
    for (MapArray :: iterator p = begin(M); p != end(M); ++p )
    {
        string x;
        x = p -> first + ": " + to_string(p -> second);
        Set.insert(x);
        
    }	 
    
    for(auto p: Set)
    {
        F << p << endl;
        cout << p << endl;
    }
 		return 0; 
}
