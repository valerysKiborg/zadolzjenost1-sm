
def is_balanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack

string1 = "{[()]}"
print(is_balanced(string1))

string2 = "{[(])}"
print(is_balanced(string2))
