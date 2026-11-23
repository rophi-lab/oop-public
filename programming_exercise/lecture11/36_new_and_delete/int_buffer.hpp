#ifndef INT_BUFFER_HPP
#define INT_BUFFER_HPP

#include <cstddef>
#include <string>

/*
Exercise 36: new and delete

Goal:
    Allocate memory on the heap by hand, hand it back by hand, and then let a
    class take over that chore so you cannot forget.

Stack vs heap:
    int x = 5;              lives on the stack, dies automatically at the end
                            of its scope -- you do nothing
    int* p = new int{5};    lives on the heap, stays alive until YOU say
                            delete p; -- nothing happens automatically

Two forms, never mixed:
    new T{...}   pairs with   delete p;
    new T[n]     pairs with   delete[] p;
    Using the wrong one is undefined behaviour, even if it seems to work.

The four classic mistakes:
    1. Forgetting delete            -> a leak; the memory is never returned
    2. Calling delete twice         -> undefined behaviour, often a crash
    3. delete instead of delete[]   -> undefined behaviour
    4. Using a pointer after delete -> a "dangling" pointer reading freed memory

    Setting a pointer to nullptr right after deleting it makes mistakes 2 and
    4 much easier to spot, because deleting a nullptr is harmless.

Why a class helps:
    If a constructor takes ownership of the memory and the destructor releases
    it, then the cleanup happens automatically at the end of the scope -- the
    same guarantee the stack gives you. That idea is called RAII, and it is
    what IntBuffer below is for.

--------------------------------------------------------------------------------
What IntBuffer needs (declare here, define in int_buffer.cpp):

    public
        explicit IntBuffer(std::size_t size);
            Allocate size ints with new int[size]{}, so every element is 0.
            explicit, so IntBuffer b = 3; does not compile.

        ~IntBuffer();
            Free the array with delete[] and then print
                IntBuffer: freed <n> ints

        IntBuffer(const IntBuffer&) = delete;
        IntBuffer& operator=(const IntBuffer&) = delete;
            Copying would copy the pointer, so both objects would delete[]
            the same memory.

        std::size_t size() const;
        int get(std::size_t index) const;
        void set(std::size_t index, int value);
            The indexes in this exercise are always valid. Do not add a
            bounds check.

        void print(const std::string& label) const;
            Print exactly one line:
                <label> size=<n> [a, b, c]
            A comma and a space between elements. No comma after the last one.

    private
        int* data_;
        std::size_t size_;
            Already declared below.

Why remove copying?
    The generated copy constructor would copy the POINTER, so two IntBuffers
    would think they own the same memory and both would free it. Removing the
    copy operations turns that disaster into a compile error. Part B in
    main.cpp asks you to try it.

Hints:
    - `new int[n]{}` gives you n ints that are all zero.
    - Remove a function the same way you removed Timer's default constructor
      in Exercise 33.
    - print() and get() and size() do not change the object, so mark them const.
*/

class IntBuffer {
private:
    int* data_;
    std::size_t size_;

public:
    // TODO: declare the constructor and the destructor.

    // TODO: remove the copy constructor and the copy assignment operator.

    // TODO: declare size, get, set, and print.
};

#endif  // INT_BUFFER_HPP
