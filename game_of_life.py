#! /usr/bin/env python3
"""
Conway's Game of Life

The square class is what we use to set up the grid for the program.
The grid class is what we use to set up the rules and manipulate the squares.
The app class is what we use to set up the program with TKinter.

Mico Santiago
"""


import tkinter as tk
import random


class Square:
    """Square class: For each cell."""

    def __init__(
        self,
        coords,
        map_size,
        side_length,
        is_alive=False,
        alive_col="black",
        dead_col="white",
    ):
        """
        Initialization function.

        Extended description of function.

        Parameters
        ----------
        map_size : int
            side_length of map
        coords : str
            Top left corner
        side_length : int
            map_size of one side
        is_alive : boolean
            Alive or dead
        alive_colour  : str
            Colour if alive
        dead_colour : str
            Colour if dead

        """

        self.map_size = map_size
        self.coords = coords
        self.side_length = side_length
        self.is_alive = is_alive
        self.alive_colour = alive_col
        self.dead_colour = dead_col

    def rect(self):
        """
        Gives the bottom right values of square

        Returns
        -------
        self.coords[0] + self.side_length, self.coords[1] + self.side_length
            x+side_length, y+side_length

        """
        return (self.coords[0] + self.side_length, self.coords[1] + self.side_length)

    def inbounds(self, coord):
        """
        Returns whether a coordinate is inbounds in the grid.

        Checks if x value is >= 0 and if the right side of the square is not
        off the board as x value is top left.
        Checks if y value is >= 0 and if the bottom side of the square is not
        off the board as y value is top left.

        Returns
        -------
        Boolean
            True or false

        """
        (x_coor, y_coor) = coord

        return (0 <= x_coor <= self.map_size - self.side_length) and (
            0 <= y_coor <= self.map_size - self.side_length
        )

    def neighbours(self):
        """
        Returns all the neighbours to the object

        self.coords is a tuple. Extracting the x and y of it

        filter(func, iterable) loops over each value and keeps the value if the
        function called per value is true.
        I convert back to list as filter object isn't easy to deal with in my
        program.
        Each item in the list is dictated by the current x or y +/- side_length.

        Returns
        -------
        Boleans
            Returns a colour whether the object is alive or dead

        """
        (x_coord, y_coord) = self.coords

        return list(
            filter(
                self.inbounds,
                [
                    (x_coord - self.side_length, y_coord + self.side_length),
                    (x_coord, y_coord + self.side_length),
                    (x_coord + self.side_length, y_coord + self.side_length),
                    (x_coord - self.side_length, y_coord),
                    (x_coord + self.side_length, y_coord),
                    (x_coord - self.side_length, y_coord - self.side_length),
                    (x_coord, y_coord - self.side_length),
                    (x_coord + self.side_length, y_coord - self.side_length),
                ],
            )
        )

    def get_colour(self):
        """
        Returns a colour whether the object is alive or dead

        Short hand if is_alivement
        If object is alive return alive colour
        Or else (only two options possible) return dead colour

        Returns
        -------
        str
            If object is alive return alive colour or else return dead colour

        """
        return self.alive_colour if self.is_alive else self.dead_colour


class Grid:
    """Grid class: The map of each square"""

    def __init__(
        self, map_size, side_length, tolerance, alive_col="black", dead_col="white"
    ):
        """
        Initialization function.

        Extended description of function.

        Parameters
        ----------
        map_size : int
            The map_size of the map
        side_length : int
            map_size of one side
        tolerance : float
            The tolerance of generating alive cells randomly
        alive_col  : str
            Colour if alive
        dead_col : str
            Colour if dead

        """

        self.map_size = map_size
        self.tolerance = tolerance
        self.alive_col = alive_col
        self.dead_col = dead_col

        self.squares = self.make_squares(side_length)

    def make_squares(self, side_length):
        """
        Creates a dictionary of square objects

        Row loop through the 'map_size' in steps of 'side_length'
        (so as to get the right top left corner each time),
        then cells loop through the 'map_size' in steps of 'side_length'
        (so as to get the right top left corner each time).
        If the random float is less than tolerance then make it start dead.
        Otherwise make it alive.

        Returns
        -------
        dict
            Returns a dictionary of squares.
        """
        squares = {}
        for y in range(0, self.map_size, side_length):
            for x in range(0, self.map_size, side_length):
                if random.random() < self.tolerance:
                    squares[(x, y)] = Square(
                        (x, y),
                        self.map_size,
                        side_length,
                        alive_col=self.alive_col,
                        dead_col=self.dead_col,
                    )
                else:
                    squares[(x, y)] = Square(
                        (x, y),
                        self.map_size,
                        side_length,
                        is_alive=True,
                        alive_col=self.alive_col,
                        dead_col=self.dead_col,
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
                square.is_alive = True

    def rules(self):
        """
        A set of rules , as defined at the top of this script, to be applied to
        the grid.

        Looping through each square
            Create a variable to keep track of alive neighbours and
            refreshes each square.
            Grab all the squares neighbours
            Loop through each neighbour
                If the neighbour is alive:
                    Increment the counter of alive neighbours.
            If the square is alive:
                RULE 1:
                    Kill the square.
                RULE 2:
                    Keep it alive.
                RULE 3:
                    Kill the square.
            If the square isn't alive:
                RULE 4:
                    Bring the square to life.
        """
        for coord, square in self.squares.items():
            alive_neighbours = 0
            neighbours = square.neighbours()

            for neighbour in neighbours:
                if self.squares[neighbour].is_alive:
                    alive_neighbours += 1

            if square.is_alive:
                if alive_neighbours < 2:
                    square.is_alive = False
                elif alive_neighbours > 3:
                    square.is_alive = False
                else:
                    continue

            else:
                if alive_neighbours == 3:
                    square.is_alive = True


class App:
    """App class: the actual tkinter usage"""

    def __init__(self, map_size, side_length, tolerance=0.8):
        """
        Initialization function.

        Will raise exception if the side_length of the boxes isn't a factor of the
        window side_length then, the boxes don't fit evenly.


        Parameters
        ----------
        map_size : int
            map_size of side of window
        side_length : int
            map_size of square
        tolerance : float
            The tolerance of generating alive cells randomly
        """

        self.map_size = map_size
        self.side_length = side_length

        if not self.map_size % self.side_length == 0:
            raise Exception(
                "The squares don't fit evenly on the screen. Box side_length needs to be a factor of window side_length."
            )

        self.grid = Grid(
            self.map_size,
            self.side_length,
            tolerance,
            alive_col="#BAEDCC",
            dead_col="BLACK",
        )

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=self.map_size, width=self.map_size)
        self.canvas.pack()
        self.items = self.update_canvas()
        self.root.after(5, self.refresh_screen)
        self.root.mainloop()

    def refresh_screen(self):
        """Applies the rules to the squares."""
        self.grid.rules()
        self.update_canvas(canvas_done=True, canvas_items=self.items)
        self.root.after(5, self.refresh_screen)

    def update_canvas(self, canvas_done=False, canvas_items={}):
        """
        If the canvas hasn't already been populated with the .create_rect()
            then Loop through the squares.
        Draws a rectangle and stores the data in a dict corresponding to the
        rectangle drawn.
        Need this to update the rectangles' colours later
        If canvas_items has been specified
            Loop through the canvas items
                Update the canvas to the new colour

        Returns
        -------
        dict
            Returns the canvas items
        ValueError
            No canvas_items so raise a value error
        """
        square_items = self.grid.squares

        if not canvas_done:
            for coords, square in square_items.items():
                (b_r_x, b_r_y) = square.rect()
                (t_l_x, t_l_y) = coords

                canvas_items[coords] = self.canvas.create_rectangle(
                    t_l_x, t_l_y, b_r_x, b_r_y, fill=square.get_colour()
                )

            return canvas_items

        else:

            if canvas_items:
                for coords, item in canvas_items.items():

                    self.canvas.itemconfig(item, fill=square_items[coords].get_colour())
            else:
                raise ValueError(
                    "No canvas_items given for re-iterating over canvas squares."
                )


if __name__ == "__main__":
    APP = App(1, 25, tolerance=0)  # raise Exception
    # APP = App(1000, 25, tolerance=0.08)
