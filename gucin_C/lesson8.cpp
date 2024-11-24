#include <iostream>
#include <math.h>
#include "row.h"
using namespace std;

    Row::Row(double first, int r): first(first), r(r){
        cout<<"The first elemenet of progresy is: "<<first<<"\n"<<"constant attitude: "<<r<<"\n";
    }

    Row::~Row(){
        cout<<"Row was destroyed"<<"\n";
    }

    void Row::Element(int j){
        double aj = first * pow(r, j);
        cout<<"received result: "<<aj<<"\n";
    }

int main(){
    int first_elem, r_first, j;
    cout<<"Enter the ai elem: ";
    cin>>first_elem;
    cout<<"Enter the r elem: ";
    cin>>r_first;
    Row row(first_elem, r_first);
    cout<<"Enter the number j of need element: ";
    cin>>j;
    row.Element(j);
    return 0;
}