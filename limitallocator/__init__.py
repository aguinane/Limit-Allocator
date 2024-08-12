"""Functions to allocate power limits"""

from .allocate import EntityDetails, allocate_proportional, allocate_water_filling
from .version import __version__

__all__ = [
    "__version__",
    "EntityDetails",
    "allocate_proportional",
    "allocate_water_filling",
]
