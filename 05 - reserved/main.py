import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(keyword.iskeyword("math"))

def is_reserved_keyword(word):
    return word in keyword.kwlist

# Example usage:
word_to_check = "for"
if is_reserved_keyword(word_to_check):
    print(f"'{word_to_check}' is a reserved keyword in Python.")
else:
    print(f"'{word_to_check}' is not a reserved keyword in Python.")


def get_all_keywords():
    return keyword.kwlist

# Example usage:
all_keywords = get_all_keywords()
print("Reserved keywords in Python:")
for keyword in all_keywords:
    print(keyword)