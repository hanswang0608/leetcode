#include <malloc.h>
#include <iostream>

using namespace std;

template <typename T>
class CustomAllocator
{
private:
    T *array;

public:
    T *allocate(size_t n)
    {
        // array = (T *)malloc(n * sizeof(T));
        array = new T[n];
        return array;
    }

    void deallocate()
    {
        delete[] array;
    }
};

int main()
{
    CustomAllocator<int> arr;
    int *p = arr.allocate(10);

    for (int i = 0; i < 10; i++)
    {
        new (&p[i]) int(i);
        cout << p[i] << endl;
    }

    arr.deallocate();
}