#include <iostream>
#include <string>
using namespace std;
int main() {
    string name;
    int age;
    string subject;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter your age: ";
    cin >> age;
    cout << "Enter your favorite subject: ";
    cin.ignore();
    getline(cin, subject);
    cout << "Hello, " << name << "!" << endl;
    cout << "You are " << age << " years old." << endl;
    cout << "Your favorite subject is " << subject << "." << endl;
    return 0;
}


