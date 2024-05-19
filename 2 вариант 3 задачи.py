def is_palindrome_slice(s):
    s = s.lower().replace(" ", "")  # Преобразуем строку в нижний регистр и удаляем пробелы
    return s == s[::-1]  # Сравниваем строку с обратной ей строкой

def is_palindrome_loop(s):
    s = s.lower().replace(" ", "")  # Преобразуем строку в нижний регистр и удаляем пробелы
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

def is_palindrome_recursive(s):
    s = s.lower().replace(" ", "")  # Преобразуем строку в нижний регистр и удаляем пробелы
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False


string1 = "A man a plan a canal Panama"
print(is_palindrome_recursive(string1))  # Выведет True
string2 = "Hello World"
print(is_palindrome_recursive(string2))  # Выведет False

string3 = "A man a plan a canal Panama"
print(is_palindrome_slice(string3))  # Выведет True
string4 = "Hello World"
print(is_palindrome_slice(string4))  # Выведет False

string5 = "A man a plan a canal Panama"
print(is_palindrome_loop(string5))  # Выведет True
string6= "Hello World"
print(is_palindrome_loop(string6))  # Выведет False
