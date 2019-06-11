#! usr/bin/env python3

from game_of_life import App, Grid, Square
import pytest


def test_raise_exception():
    with pytest.raises(Exception) as excinfo:
        obj = App(1, 25, tolerance=0)
    assert (
        "The squares don't fit evenly on the screen. Box side_length needs to be a factor of window side_length."
        in str(excinfo.value)
    )
