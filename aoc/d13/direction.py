from enum import Enum

from .vertical_folder import VerticalFolder
from .horizontal_folder import HorizontalFolder


class Direction(Enum):
    LEFT = HorizontalFolder()
    UP = VerticalFolder()
