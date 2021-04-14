# ---Generate Document---

# solution 1
def generate_document(characters: str, document: str) -> bool:
    if len(characters) < len(document):
        return False
    elif document == "":
        return True

    characters_dict = dict()

    for char in characters:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1

    for char in document:
        if char in characters_dict:
            characters_dict[char] -= 1
            if characters_dict[char] < 0:
                return False
        else:
            return False

    return True


a = generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!")
assert a is True
