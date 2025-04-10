print("hello world")

dic1 = {"name": "John", "age": 30, "city": "New York"}
dic2 = {"name": "Jane", "age": 25, "city": "Los Angeles"}


def compare_dicts(dict1, dict2):
    """
    Compare two dictionaries and return a list of keys that are different.
    """
    differences = []
    for key in dict1.keys():
        if key not in dict2:
            differences.append(f"{key} is missing in dict2")
        elif dict1[key] != dict2[key]:
            differences.append(f"{key} is different: {dict1[key]} vs {dict2[key]}")
    for key in dict2.keys():
        if key not in dict1:
            differences.append(f"{key} is missing in dict1")
    return differences

print(compare_dicts(dic1, dic2))
