#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main() 
{ 
    std::ifstream file("../TaskA.csv");
    std::string str; 
    
    std::getline(file, str);
    cout<<str<<endl;
    // while (std::getline(file, str))
    // {
    //     // Process str
    // }
}