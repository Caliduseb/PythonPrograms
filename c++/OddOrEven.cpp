#include <iostream>
using namespace std;

bool isEven(int _zahl){
    int i = _zahl;
    while(true)
    {
        i += 2;
        if(i == 1)
        {
            cout << "Odd \n";
            return false;
        }
        if(i == 0)
        {
            cout << "Even \n";
            return true;
        }
    }
}

int main()
{
    int i;
    cout << "Enter a number: ";
    cin >> i;
    isEven(i);
    return 0;
}

