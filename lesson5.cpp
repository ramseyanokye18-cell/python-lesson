#include <iostream>
using namespace std;
bool isEven(int num);
// function to square a number
int square(int num) {
    return num * num;
}

// void function to print multiplication table of a number
void multiplicationTable(int num) {
    cout << "Multiplication Table of " << num << ":" << endl;
    for (int i = 1; i <= 10; i++) {
        cout << num << " x " << i << " = " << num * i << endl;
    }
}
int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;

    // Call the square function
    int squared = square(number);
    cout << "Square of " << number << " is " << squared << endl;

    // Call the multiplicationTable function
    multiplicationTable(number);

    // Call the isEven function
    if (isEven(number)) {
        cout << number << " is even." << endl;
    } else {
        cout << number << " is odd." << endl;
    }
return 0;
}
// isEven function to check if a number is even
bool isEven(int num) {
    return num % 2 == 0;
}