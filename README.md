# Limit-Allocator

Allocate power limits amoungst entities

## Example

```python
from limitallocator import EntityDetails, allocate_water_filling


EXAMPLES = [
    EntityDetails("A", 5.0, 5.0),
    EntityDetails("B", 1.5, 3.0),
    EntityDetails("C", 1.5, 10.0),
]

target = 15
output = allocate_water_filling(target, EXAMPLES)
print(output)  # {'A': 5.0, 'B': 3.0, 'C': 7.05}
```
