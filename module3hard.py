data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    total_sum = 0
    total_len = 0
    def structure_checker(item):
        nonlocal total_sum, total_len
        if isinstance(item, (list, tuple, set)):
            for object in item:
                structure_checker(object)
        elif isinstance(item, dict):
            for key, value in item.items():
                structure_checker(key)
                structure_checker(value)
        elif isinstance(item, int):
            total_sum += item
        elif isinstance(item, float):
            total_sum += int(item)
        elif isinstance(item, str):
            total_len += len(item)
    structure_checker(data_structure)
    return total_sum + total_len

result = calculate_structure_sum(data_structure)
print(result)