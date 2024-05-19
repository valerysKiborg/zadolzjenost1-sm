
def is_palindrome_loop(s):
    s = s.lower().replace(" ", "")  # Преобразуем строку в нижний регистр и удаляем пробелы
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

string3 = "A man a plan a canal Panama"
print(is_palindrome_slice(string3))  # Выведет True
string4 = "Hello World"
print(is_palindrome_slice(string4))  # Выведет False


