from typing import NamedTuple


class EntityDetails(NamedTuple):
    """Represents the allowed ranges for assigning limits"""

    name: str
    min_val: float
    max_val: float


def contains_duplicates(items: list) -> bool:
    values = set(items)
    return len(values) != len(items)


def allocate_mins(entities: list[EntityDetails]) -> dict[str, float]:
    """Allocate target amoungst all entities"""

    # Check inputs
    if contains_duplicates([x.name for x in entities]):
        msg = "Duplicate name in entities"
        raise ValueError(msg)

    # To start with, assign all entities their minimum target
    output = {}
    for name, min_val, _ in entities:
        output[name] = min_val
    return output


def allocate_proportional(
    target: float, entities: list[EntityDetails]
) -> dict[str, float]:
    """Allocate target amoungst all entities"""

    # Cannot allocate more then combined maximums
    max_of_maxes = sum([x.max_val for x in entities])
    if target > max_of_maxes:
        target = max_of_maxes

    # To start with, assign all entities their minimum target
    output = allocate_mins(entities)

    # Check if allocation exhausted or how much remaining
    allocated = sum([x for x in output.values()])
    available = target - allocated
    if available <= 0:
        return output  # Allocation exhaused

    # Calculate proportion remaining
    desired_extra = max_of_maxes - allocated
    proportion = (target - allocated) / desired_extra
    for name, min_val, max_val in entities:
        val = min_val + (max_val - min_val) * proportion
        output[name] = val

    return output


def allocate_water_filling(
    target: float, entities: list[EntityDetails], incr_val: float = 0.05
) -> dict[str, float]:
    """Allocate target amoungst all entities"""

    # Cannot allocate more then combined maximums
    max_of_maxes = sum([x.max_val for x in entities])
    if target > max_of_maxes:
        target = max_of_maxes

    # To start with, assign all entities their minimum target
    output = allocate_mins(entities)

    # Check if allocation exhausted or how much remaining
    allocated = sum([x for x in output.values()])
    available = target - allocated
    if available <= 0:
        return output  # Allocation exhaused

    waterline = min([x.min_val for x in entities])
    while available > 0:
        waterline += incr_val
        for name, min_val, max_val in entities:
            new_val = max(min(max_val, waterline), min_val)
            output[name] = new_val
        allocated = sum([x for x in output.values()])
        available = target - allocated

    return output
