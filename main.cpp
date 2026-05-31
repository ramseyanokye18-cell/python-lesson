#include <iostream>
#include <string>
using namespace std;
int main() {
    string name="Ramsey Anokye";
    int age=20;
    float GPA=85.5;
    bool isStudent=true;
    
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "GPA: " << GPA << endl;
    cout << "Student: " << boolalpha << isStudent << endl;
    return 0;
}