#! /usr/bin/env python3
"""
   Conway's Game of Life

   Longer, more detailed explanation of your solution. This may be anywhere from
   a couple of sentences to several paragraphs depending on how complex the
   assignment is. It should be detailed enough that someone who has never seen the
   code can understand what it does just by reading this explanation. You may
   also want to include examples of using the program if it accepts command line
   arguments.

   Mico Santiago
"""


from tkinter import *
import random


class Square:
    """Square class: For each cell."""

    def __init__(
        self,
        coords,
        length,
        size,
        state=False,
        active_col="black",
        inactive_col="white",
    ):
        """
        Initialization function.

        Extended description of function.

        Parameters
        ----------
        length : int
            Size of map
        coords : str
            Top left corner
        size : int
            Length of one side
        state : boolean
            Alive or dead
        active_colour  : str
            Colour if alive
        inactive_colour : str
            Colour if dead

        """

        self.length = length
        self.coords = coords
        self.size = size
        self.state = state
        self.active_colour = active_col
        self.inactive_colour = inactive_col

    def rect(self):
        """
        Gives the bottom right values of square

        Returns
        -------
        self.coords[0] + self.size, self.coords[1] + self.size
            x+size, y+size

        """
        return (self.coords[0] + self.size, self.coords[1] + self.size)

    def inbounds(self, coord):
        """
        Returns whether a coordinate is inbounds in the grid

        Checks if x value is >= 0 and if the right side of the square is not off the board as x value is top left.
        Checks if y value is >= 0 and if the bottom side of the square is not off the board as y value is top left.

        Returns
        -------
        Boolean
            True or false

        """
        (x, y) = coord

        return (x >= 0 and x <= self.length - self.size) and (
            y >= 0 and y <= self.length - self.size
        )

    def neighbours(self):
        """
        Returns all the neighbours to the object

        self.coords is a tuple. Extracting the x and y of it

        filter(func, iterable) loops over each value and keeps the value if the function called per value is true.
        I convert back to list as filter object isn't easy to deal with in my program
        Each item in the list is dictated by the current x or y +/- size.

        Returns
        -------
        Boleans
            Returns a colour whether the object is alive or dead

        """
        (x, y) = self.coords

        return list(
            filter(
                self.inbounds,
                [
                    (x - self.size, y + self.size),
                    (x, y + self.size),
                    (x + self.size, y + self.size),
                    (x - self.size, y),
                    (x + self.size, y),
                    (x - self.size, y - self.size),
                    (x, y - self.size),
                    (x + self.size, y - self.size),
                ],
            )
        )

    def get_colour(self):
        """
        Returns a colour whether the object is alive or dead

        Short hand if statement
        If object is alive return alive colour
        Or else (only two options possible) return dead colour

        Returns
        -------
        str
            If object is alive return alive colour or else return dead colour

        """
        return self.active_colour if self.state else self.inactive_colour


class Grid:
    """Grid class: The map of each square"""

    def __init__(
        self, length, size, tolerance, active_col="black", inactive_col="white"
    ):
        """
        Initialization function.

        Extended description of function.

        Parameters
        ----------
        length : int
            The length of the map
        size : int
            Length of one side
        tolerance : int
            The tolerance of generating alive cells randomly
        active_col  : str
            Colour if alive
        inactive_col : str
            Colour if dead

        """

        self.length = length
        self.tolerance = tolerance
        self.active_col = active_col
        self.inactive_col = inactive_col

        self.squares = self.make_squares(size)

    def make_squares(self, size):
        """
        Creates a dictionary of square objects

        Row loop through the 'length' in steps of 'size' (so as to get the right top left corner each time),
        then cells loop through the 'length' in steps of 'size' (so as to get the right top left corner each time).
        If the random float is less than tolerance then make it start dead. Otherwise make it alive.

        Returns
        -------
        dict
            Returns a dictionary of squares.
        """
        squares = {}
        for y in range(0, self.length, size):
            for x in range(0, self.length, size):
                if random.random() < self.tolerance:
                    squares[(x, y)] = Square(
                        (x, y),
                        self.length,
                        size,
                        active_col=self.active_col,
                        inactive_col=self.inactive_col,
                    )
                else:
                    squares[(x, y)] = Square(
                        (x, y),
                        self.length,
                        size,
                        state=True,
                        active_col=self.active_col,
                        inactive_col=self.inactive_col,
                    )
        return squares

    def set_squares(self, on_coordinates):
        """
        Takes a list of coordinates and makes them alive cells
        Not used but can be used to set alive squares

        Loops through the dictionary of squares
            If the square is in the list of coordinates


        Returns
        -------
        boolean
            Returns True
        """
        for coord, square in self.squares:
            if coord in on_coordinates:
                square.state = True

    def rules(self):
        """
        A set of rules , as defined at the top of this script, to be applied to the grid

        Looping through each square
            Create a variable to keep track of alive neighbours. Refreshes each square
            Grab all the squares neighbours
            Loop through each neighbour
                If the neighbour is alive:
                    Increment the counter of alive neighbours
            If the square is alive:
                RULE 1:
                    Kill the square
                RULE 2:
                    Keep it alive
                RULE 3:
                    Kill the square
            If the square isn't alive:
                RULE 4:
                    Bring the square to life
        """
        for coord, square in self.squares.items():
            alive_neighbours = 0
            neighbours = square.neighbours()

            for neighbour in neighbours:
                if self.squares[neighbour].state:
                    alive_neighbours += 1

            if square.state:
                if alive_neighbours < 2:
                    square.state = False
                elif alive_neighbours > 3:
                    square.state = False
                else:
                    continue

            else:
                if alive_neighbours == 3:
                    square.state = True


class App:
    """App class: the actual tkinter usage"""

    #  Initialization function (all the precalled things)
    def __init__(self, length, size, tolerance=0.8):

        #  length % size NEEDS to = 0
        self.length = length  # Length of side of window
        self.size = size  # Length of square

        #  If the size of the boxes isn't a factor of the window size
        if not self.length % self.size == 0:
            #  The boxes don't fit evenly.
            raise Exception(
                "The squares don't fit evenly on the screen."
                + " Box size needs to be a factor of window size."
            )

        #  Create a grid object which can manipulate the squares
        self.grid = Grid(
            self.length,
            self.size,
            tolerance,
            active_col="#008080",
            inactive_col="white",
        )

        #  tkinter event
        self.root = Tk()

        #  Canvas object to display squares
        self.canvas = Canvas(self.root, height=self.length, width=self.length)
        #  Set on to the window
        self.canvas.pack()

        #  updates canvas
        self.items = self.update_canvas()

        #  Creates a loop within the mainloop
        self.root.after(5, self.refresh_screen)
        #  Mainloop in tkinter, run the code and loop it until exit called
        self.root.mainloop()

    # Refreshes the screen
    def refresh_screen(self):
        #  Applies the rules to the squares
        self.grid.rules()
        #  Updates canvas
        self.update_canvas(canvas_done=True, canvas_items=self.items)

        #  Reruns the loop
        self.root.after(5, self.refresh_screen)

    #  Updates canvas
    def update_canvas(self, canvas_done=False, canvas_items={}):

        #  The dict.items() of each square
        #  { coord of square: square object }
        square_items = self.grid.squares

        #  If the canvas hasn't already been populated with the .create_rect()
        if not canvas_done:
            #  Loop through the squares
            for coords, square in square_items.items():
                (b_r_x, b_r_y) = square.rect()  #  The bottom right coordinates
                (t_l_x, t_l_y) = coords  #  Top left coordinates

                #  Draws a rectangle and stores the data in a dict corresponding to the rectangle drawn
                #  Need this to update the rectangles' colours later
                canvas_items[coords] = self.canvas.create_rectangle(
                    t_l_x, t_l_y, b_r_x, b_r_y, fill=square.get_colour()
                )

            #  Return the canvas items
            #  { coordinates of square drawn: canvas_rectangle object }
            return canvas_items

        #  The canvas has already been populated with squares
        #  Need this as tkinter doesn't draw on top.
        else:
            #  If canvas_items has been specified
            if canvas_items:
                #  Loop through the canvas items
                for coords, item in canvas_items.items():
                    #  Update the canvas to the new colour
                    self.canvas.itemconfig(item, fill=square_items[coords].get_colour())
            #  No canvas_items so raise a value error
            else:
                #  Throws out an error
                raise ValueError(
                    "No canvas_items given for re-iterating over canvas squares."
                )


if __name__ == "__main__":
    app = App(1000, 25, tolerance=0.7)
