#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ofstream myfile;
    myfile.open ("data.txt");
    for(int i=0;i<500;i++){
        myfile<<rand() % 100<<" ";
    }
    myfile.close();
    return 0;
}