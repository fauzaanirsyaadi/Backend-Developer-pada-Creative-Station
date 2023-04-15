def is_palindrome(n):
    # fungsi untuk memeriksa apakah suatu bilangan merupakan palindrome atau bukan
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    # fungsi untuk mencari palindrome terdekat yang lebih besar dari suatu bilangan
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

# contoh penggunaan
input_num = 125980
result = next_palindrome(input_num)
print(result)
