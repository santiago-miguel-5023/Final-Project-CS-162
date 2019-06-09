# Final Project
Mico Santiago
CS 162
Professor Joe Paris
## Introduction

The rule of my game of life follows the same rules as Conway's game of life:

    1)  Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2)  Any live cell with two or three live neighbors lives on to the next generation.
    3)  Any live cell with more than three live neighbors dies, as if by overcrowding.
    4)  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Documentation


   ```python
   """
   Brief assignment description.

   Longer, more detailed explanation of your solution. This may be anywhere from
   a couple of sentences to several paragraphs depending on how complex the
   assignment is. It should be detailed enough that someone who has never seen the
   code can understand what it does just by reading this explanation. You may
   also want to include examples of using the program if it accepts command line
   arguments.

   Your name
   Your partner's/collaborator's name
   """
   ```

   ```python
    def random_number_generator(arg1, arg2):
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1.
    arg2 : str
        Description of arg2.

    Returns
    -------
    int
        Description of return value. This may be omitted if the function does not explicitly return a value.

    """
   ```

## Requirements

In order to receive full credit your project must include all of the following:
    • Object oriented design: your code must be written in an object-oriented manner. You must
      design and implement a set of classes in a logical hierarchy.
    • Functional decomposition: in each class, your code needs to be written as a set of functions that
      each perform a single task.
    • At least one of these functions must be recursive.
    • Error handling: you should use exception handling to deal with errors that occur during the
      execution of your program. Recover from errors when possible, provide the user with a friendly
      explanation of what went wrong before exiting the program if you cannot recover.
    • File I/O: your program must read from and write to one or more files.
    • You must write tests for all your functions. Be sure your tests cover both good and bad input.
      For example, when asking for numeric input from the user you should write tests that supply
      input that both can and cannot be successfully cast.

### Part 1



### Part 2



```python
with pytest.raises(Exception):
    my_func()
```
