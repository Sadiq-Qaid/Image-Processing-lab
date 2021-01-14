# Write a C++ program to perform operator overloading.

#include "bits/stdc++.h"
#include <vector>
#define rows 5
#define cols 5
using namespace std;
int N;

class Matrix {
int arr[rows][cols];
public:
void input(vector<vector<int> >& A);
//void display() ;
void operator=(Matrix x);
void operator+(Matrix x);
void operator-(Matrix x);
void operator*(Matrix x);

};

void Matrix::input(vector<vector<int> >& A)
{
for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {

arr[i][j] = A[i][j];
}
}
 
}

void Matrix::operator=(Matrix x)
{
// Travarse the Matrix x
for (int i = 0; i < rows; i++) {
for (int j = 0; j < cols; j++) {
arr[i][j] =  x.arr[i][j];
}
}

for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {

// Print the element
cout << arr[i][j] << ' ';
}
cout << endl;
}
cout <<"#######################"<< endl;

}

void Matrix::operator+(Matrix x)
{

int mat [rows][cols];
for (int i = 0; i < rows; i++) {
for (int j = 0; j < cols; j++) {
mat[i][j] = arr[i][j]+ x.arr[i][j];
}
}
   for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {
cout << mat[i][j] <<"\t";
}
cout << endl;
}
cout <<"#######################"<< endl;
}


void Matrix::operator-(Matrix x)
{

int mat[rows][cols];


for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {
mat[i][j] = arr[i][j]
- x.arr[i][j];
}
}
for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {

cout << mat[i][j] << ' ';
}
cout << endl;
}
cout <<"#######################"<< endl;

}


void Matrix::operator*(Matrix x)
{

int mat[rows][cols];
for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {
mat[i][j] = 0;

for (int k = 0; k < rows; k++) {
mat[i][j] += arr[i][k]
* (x.arr[k][j]);
}
}
}

for (int i = 0; i < rows; i++) {

for (int j = 0; j < cols; j++) {

cout << mat[i][j] <<"\t";
}
cout << endl;
}
cout <<"#######################"<< endl;

}

int main()
{

vector<vector<int> > v1 (rows, vector<int> (cols, 0));
vector<vector<int> > v2(rows, vector<int> (cols, 0)) ;

for (int i = 0; i < v1.size(); i++) {

for (int j = 0; j < v1[i].size(); j++) {
v1[i][j] = i+j+1;
cout<<v1[i][j]<<" ";
}
cout<<endl;

}

Matrix m1, m2;
m1.input(v1);
cout << "intializing Second Matrix using assignment Operator"<<endl;
m2 = m1;
cout << "Addition of two given"
<< " Matrices is : \n";
m1 + m2;

cout << "Substraction of two given"
<< " Matrices is : \n";
m1 - m2;

cout << "Multiplication of two"
<< " given Matrices is : \n";
m1* m2;

return 0;
} 
