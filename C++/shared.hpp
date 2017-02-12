#pragma once

#include <iostream>
#include <string>
#include <cmath>
#include <type_traits>

//-------------------------------------------------------------------------------------------------

template<typename T>
void checkEqual(
    const T& value1, const T& value2,
    const std::string& expr1, const std::string& expr2,
    int line, const std::string& file )
{
    std::cout << "Evaluating constraint on line " << line << " file " << file << std::endl;
    if ( value1 == value2 )
    {
        std::cout << "  passed." << std::endl;
    }
    else
    {
        std::cout << "  FAILED: " << expr1 << " (" << value1 << ") != ";
        std::cout << expr2 << " (" << value2 << ")" << std::endl;
    }
}

//-------------------------------------------------------------------------------------------------

#define CHECK_EQUAL( first, second ) checkEqual( first, second, #first, #second, __LINE__, __FILE__ )

double sum( double a, double b ) {return a + b;}
double power( double a, int exp ) {return std::pow(a, exp);}

//-------------------------------------------------------------------------------------------------

class TestClass
{
public:
    TestClass( double v ) : m_v(v) {}
    
    double sum( double a, double b ) const { return m_v + a + b; }
    double diffPow( double a, int exp ) const { return std::pow( (m_v-a), exp ); }
    double pow( int exp ) const { return std::pow( m_v, exp ); }    
    double diff( double a ) const  { return m_v - a; }
   
private:
    double m_v;
};

//-------------------------------------------------------------------------------------------------

template<typename R, typename ... P> class callable
{
    public:
        virtual ~callable() {}
        virtual R operator()(P ... p) = 0;
};

//-------------------------------------------------------------------------------------------------

template <typename R, typename ... P> class free_function : public callable<R, P...>
{
    public:

        typedef R (*function_t)(P ... p);
        free_function(function_t theFunc) : m_function(theFunc) {}

        R operator() (P ... p)
        {
            return (m_function(p...));
        }

    private:
        function_t m_function;
};

//-------------------------------------------------------------------------------------------------

template <typename CLASS, typename R, typename ... P> class bound_member_function : public callable<R, P...>
{
    public:
        typedef R (CLASS::*function_t)(P ... p) const;
        bound_member_function(CLASS* theObj, function_t theFunc) : m_function(theFunc), m_object(theObj) {}

        R operator() (P ... p)
        {
            return ((*m_object).*m_function)(p...);
        }

    private:
        function_t m_function;
        CLASS* m_object;
};

//-------------------------------------------------------------------------------------------------

template <typename CLASS, typename R, typename ... P> class member_function : public callable<R, P...>
{
    public:

        template <typename X, typename ... REST> struct mem_fun_unpacker
        {
            typedef X CLASSPTR;
            typedef typename std::remove_pointer<CLASSPTR>::type CLASSNOPTR;
            typedef R (CLASSNOPTR::*function_t)(REST...) const;
        };

        typedef typename mem_fun_unpacker<P...>::function_t function_t;
        member_function(function_t theFunc) : m_function(theFunc) {}

        template <typename OBJPTR, typename ... PARAMS> R callFuncWithMember(OBJPTR x, PARAMS ... p)
        {
            return ((*x).*m_function)(p...);
        }

        R operator() (P ... p)
        {
            return callFuncWithMember(p...);
        }

    private:
        function_t m_function;
};

//-------------------------------------------------------------------------------------------------

template <typename T> struct function;

//-------------------------------------------------------------------------------------------------

template <typename R, typename ... P> class function<R(P...)>
{
    public:

        template <typename CLASS> explicit function(CLASS functionPointer)
        {
            typedef typename std::conditional<std::is_member_function_pointer<CLASS>::value, 
                                              member_function<CLASS,R,P...>, 
                                              free_function<R,P...> >::type class_type;

            func = new (buffer) class_type(functionPointer);
        }

        template <typename CLASS> explicit function(CLASS* x, R (CLASS::*memberFunctionPointer)(P...) const)
        {
            func = new (buffer) bound_member_function<CLASS, R, P...>(x, memberFunctionPointer);
        }

        ~function()
        {
            func->~callable<R, P...>(); // Don't use delete, as placement new used to construct on stack-based buffer
        }

        R operator()(P ... p) const
        {
            return (*func)(p ...);
        }

    private:
        // Vile hack, but this should ensure that maxSize is always big enough to store whatever we need to construct
        const static int maxSize = sizeof(bound_member_function<std::string, double, double>);
        char buffer[maxSize]; // Stack-based memory buffer
        callable<R, P...>* func;
};

//-------------------------------------------------------------------------------------------------
