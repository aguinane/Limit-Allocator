import pytest

from limitallocator import EntityDetails, allocate_proportional, allocate_water_filling

EXAMPLES = [
    EntityDetails("A", 5, 5),
    EntityDetails("B", 1.5, 3),
    EntityDetails("C", 1.5, 10),
    EntityDetails("D", 1.5, 15),
    EntityDetails("E", 1.5, 20),
]


def test_duplicate_example():
    """Test error if same key"""

    dup_entities = [
        EntityDetails("A", 5, 5),
        EntityDetails("A", 5, 5),
        EntityDetails("B", 1.5, 3),
    ]

    with pytest.raises(ValueError):
        allocate_water_filling(5, dup_entities)


def test_water_filling_min_values():
    """Test min values are all used"""
    all_mins = sum([x.min_val for x in EXAMPLES])
    target = all_mins - 5
    output = allocate_water_filling(target, EXAMPLES, incr_val=0.01)
    assert len(output) == 5
    total = sum([output[x] for x in output])
    assert total == all_mins


def test_proportional_min_values():
    """Test min values are all used"""
    all_mins = sum([x.min_val for x in EXAMPLES])
    target = all_mins - 5
    output = allocate_proportional(target, EXAMPLES)
    assert len(output) == 5
    total = sum([output[x] for x in output])
    assert total == all_mins


def test_water_filling():
    """Test water filling method"""
    all_mins = sum([x.min_val for x in EXAMPLES])
    all_maxs = sum([x.max_val for x in EXAMPLES])
    for x in range(10, 100, 10):
        target = all_mins + x
        output = allocate_water_filling(target, EXAMPLES)
        assert len(output) == 5
        total = sum([output[x] for x in output])
        assert round(total, 0) == round(min(target, all_maxs), 0)


def test_proportional():
    """Test proportional method"""
    all_mins = sum([x.min_val for x in EXAMPLES])
    all_maxs = sum([x.max_val for x in EXAMPLES])
    for x in range(10, 100, 10):
        target = all_mins + x
        output = allocate_proportional(target, EXAMPLES)
        assert len(output) == 5
        total = sum([output[x] for x in output])
        assert round(total, 0) == round(min(target, all_maxs), 0)
