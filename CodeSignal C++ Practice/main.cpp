#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

void q1()
{
    string str;
    cout << "Enter your name: ";

    cin >> str;

    cout << "Hello, " + str << endl;
}

void q2()
{
    int a;
    int b;

    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << a + b << endl;
}

void q3()
{
    int a;

    cout << "Enter an integer: ";
    cin >> a;

    cout << a << " is " << (a % 2 == 0 ? "even" : "odd") << endl;
}

void q4()
{
    int pos_count = 0;
    int neg_count = 0;

    int input;
    do
    {
        cout << "Enter a number: ";
        cin >> input;
        if (input > 0)
            pos_count++;
        else if (input < 0)
            neg_count++;
    } while (input);

    cout << "Number of positive numbers entered: " << pos_count << endl;
    cout << "Number of negative numbers entered: " << neg_count << endl;
}

void q5()
{
    string str;
    cout << "Enter a string: ";
    cin >> str;

    for (auto it = str.rbegin(); it != str.rend(); it++)
    {
        cout << *it;
    }
}

void q6()
{
    string str;
    cout << "Enter a string: ";
    cin >> str;
    reverse(str.begin(), str.end());

    ofstream file;
    file.open("output.txt");
    file << str;
    file.close();

    ifstream in_file("output.txt");
    string new_str;
    getline(in_file, new_str);
    cout << "read back: " + new_str;
}

namespace q7
{
    class Car
    {
    private:
        string brand;
        string model;
        int year;

    public:
        void set_brand(const string &brand) { this->brand = brand; }
        void set_model(const string &model) { this->model = model; }
        void set_year(const int &year) { this->year = year; }
        string get_brand() const { return brand; }
        string get_model() const { return model; }
        int get_year() const { return year; }
    };

    void q7()
    {
        q7::Car car;
        car.set_brand("Toyota");
        car.set_model("Corolla");
        car.set_year(2020);
        cout << "Car Details: " << car.get_brand() << " " << car.get_model() << " " << car.get_year() << endl;
    }
}

int main()
{
    q7::q7();
}