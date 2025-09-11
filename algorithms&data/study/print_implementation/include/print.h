#ifndef PRINT_H
#define PRINT_H

#include <iostream>
#include <sstream>
#include <type_traits>
using namespace std;


void print()
{
    cout << endl;
}

template<typename T, typename... Args>
void print_helper(ostringstream& stream, const string& sep,
const T& first, const Args&... args)
{
    stream << first;

    if constexpr (sizeof...(args) > 0)
    {
        stream << sep;
        print_helper(stream, sep, args...);
    }
}

void print_helper(ostringstream& stream, const string& sep){}


template<typename... Args>
void print_impl(const string& sep, const string& end, const Args&... args)
{
    ostringstream stream;
    print_helper(stream, sep, args...);
    cout << stream.str() << end;
}

template<typename... Args>
void print(const Args&... args)
{
    print_impl(" ", "\n", args...);
}

template<typename... Args>
void print(const string& sep, const Args&... args)
{
    print_impl(sep, "\n", args...);
}

template<typename... Args>
void print(const string& sep, const string& end, const Args&... args)
{
    print_impl(sep, end, args...);
}

#endif