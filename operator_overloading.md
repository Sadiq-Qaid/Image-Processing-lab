# Write a C++ program to perform operator overloading.
# description:
Using operator overloading in C++, you can specify more than one meaning for an operator in one scope. The purpose of operator overloading is to provide a special meaning of an operator for a user-defined data type.

With the help of operator overloading, you can redefine the majority of the C++ operators. You can also use operator overloading to perform different operations using one operator. 
In C++, we can change the way operators work for user-defined types like objects and structures. This is known as operator overloading. For example,

Suppose we have created three objects c1, c2 and result from a class named Complex that represents complex numbers.

Since operator overloading allows us to change how operators work, we can redefine how the + operator works and use it to add the complex numbers of c1 and c2 by writing the following code:

result = c1 + c2;

instead of something like

result = c1.addNumbers(c2);

This makes our code intuitive and easy to understand.

Note: We cannot use operator overloading for fundamental data types like int, float, char and so on.
# Code
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

# output operator_overloading:
![image](https://user-images.githubusercontent.com/72402606/104446142-058adb00-55c0-11eb-84a9-b7ac5146d572.png)
