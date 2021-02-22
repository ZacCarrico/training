This repo is composed of problems/solutions for algorithm 
development training.

###Recursion algorithm patterns
* recursion is often convenient when you need to explore paths through 
a matrix
* the base case conditional will typically be the first step in the fn
    * it's usually `<= 0` or `None`
* you can use a nested function to keep the parent function's 
parameter in scope. You don't have to do this, but it's cleaner 
than creating a variable that persists outside the function
    * you can only use a mutable object when multiple recursive 
    calls need to access it. For example, lists or dictionaries, 
    not ints (ie count objects), sets or strings.
    * use the parent's function's local variable instead 
    of trying to pass the variable throughout recursive calls 
    because this fails if there's branching
* it's common to need to return a sum of recursive 
calls (eg `return f(x) + f(x-1)`)
* usually the time and space complexity are the same
