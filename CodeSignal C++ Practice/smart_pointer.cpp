#include <iostream>

using namespace std;

namespace sp
{
    template <typename T>
    class unique_ptr
    {
    private:
        T *_ptr;

    public:
        unique_ptr(T *ptr) : _ptr(ptr) {}
        ~unique_ptr() { delete _ptr; }

        unique_ptr(const unique_ptr &other) = delete;
        unique_ptr &operator=(const unique_ptr &other) = delete;

        T &operator*() { return *_ptr; }
        T *operator->() { return _ptr; }

        T *get() const { return _ptr; }
    };

    class shared_ptr_control
    {
    private:
        int count;

    public:
        shared_ptr_control()
        {
            count = 0;
        }
    };

    template <typename T>
    class shared_ptr
    {
    private:
        T *_ptr;
        int *count;

    public:
        shared_ptr() : _ptr(nullptr), count(nullptr) {}

        shared_ptr(T *ptr) : _ptr(ptr)
        {
            count = new int(1);
        }

        ~shared_ptr()
        {
            if (--(*count) == 0)
            {
                delete _ptr;
                delete count;
            }
        }

        shared_ptr<T>(const shared_ptr<T> &other)
        {
            _ptr = other.get();
            count = other.get_count();
            (*count)++;
        }

        shared_ptr &operator=(const shared_ptr &other)
        {
            _ptr = other.get();
            count = other.get_count();
            (*count)++;
            return *this;
        }

        T *get() const { return _ptr; }
        int *get_count() const { return count; }

        T &operator*() { return *_ptr; }
        T *operator->() { return _ptr; }
    };
}

int main()
{
    sp::unique_ptr<std::string> p(new std::string("hello"));
    std::cout << *p << std::endl;

    sp::shared_ptr<std::string> s(new std::string("hello"));
    std::cout << *s << std::endl;

    sp::shared_ptr<string> s2;
    s2 = s;
    *s = "hi";
    std::cout << *(s.get_count()) << " " << *(s2.get_count()) << "\n";
    cout << *s2 << endl;
}