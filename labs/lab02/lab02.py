RU_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
CHAR_INDEX = {char: index for index, char in enumerate(RU_ALPHABET)}
INDEX_CHAR = {index: char for index, char in enumerate(RU_ALPHABET)}
CHAR_COUNT = len(RU_ALPHABET)

def pad_plaintext(plaintext, total_length, fill_char="х"):
    text = plaintext.lower().replace(" ", "")
    if len(text) < total_length:
        text += fill_char * (total_length - len(text))
    return text

def column_order(password):
    return sorted(range(len(password)), key=lambda i: password[i].lower())

#1. Маршрутное шифрование. Алгоритм маршрутного шифрования.

def route_encrypt(plaintext, n, m, password):
    assert len(password) == n, "Password length must be equal to n"
    padded = pad_plaintext(plaintext, n * m)
    
    grid = [[None] * n for _ in range(m)]
    idx = 0
    for i in range(m):
        for j in range(n):
            grid[i][j] = padded[idx]
            idx += 1
    order = column_order(password)
    result = []
    for col in order:
        for row in range(m):
            result.append(grid[row][col])
    return "".join(result)

def route_decrypt(ciphertext, n, m, password):
    assert len(password) == n, "Password length must be equal to n"
    order = column_order(password)
    grid = [[None] * n for _ in range(m)]
    idx =0
    for col in order:
        for row in range(m):
            grid[row][col] = ciphertext[idx]
            idx += 1
    result = []
    for i in range(m):
        for j in range(n):
            result.append(grid[i][j])
    return "".join(result)




#Шифрование с помощью решеток.

def rotate_position(i, j, n):
    return (j, n - 1 - i)

def grille_fill_order(k):
    n = 2*k
    holes = [(i, j) for i in range(k) for j in range(k)]
    order = []
    for _ in range (n):
        order.extend(holes)
        holes =  [rotate_position(i, j, n) for (i, j) in holes]
    return order


def grille_encrypt(plaintext, k, password):
    n = 2*k
    assert len(password) == n, "Password length must be equal to 2k"
    padded = pad_plaintext(plaintext, n*n)
    order = grille_fill_order(k)
    grid = [[None] * n for _ in range(n)]
    for idx, (i, j) in enumerate(order):
        grid[i][j] = padded[idx]
    col_order = column_order(password)
    result = []
    for col in col_order:
        for row in range(n):
            result.append(grid[row][col])
    return "".join(result)

def grille_decrypt(ciphertext, k, password):
    n = k*2
    assert len(password) == n, "Password length must be equal to 2k"
    col_order = column_order(password)
    grid = [[None] * n for _ in range(n)]
    idx= 0
    for col in col_order:
        for row in range(n):
            grid[row][col] = ciphertext[idx]
            idx += 1
    order = grille_fill_order(k)
    result = []
    for (i,j) in order:
        result.append(grid[i][j])
    return "".join(result)


#Таблица Виженера.

def vigenere_encrypt(plaintext, password):
    plaintext = plaintext.lower().replace(" ", "")
    password = password.lower()
    result = []
    point_idx = 0
    for ch in plaintext:
        if ch in CHAR_INDEX:
            shift = CHAR_INDEX[password[point_idx]]
            new_idx = (CHAR_INDEX[ch] + shift) % CHAR_COUNT
            result.append(INDEX_CHAR[new_idx])
            point_idx = (point_idx + 1) % len(password)
    return "".join(result)

def vigenere_decrypt(ciphertext, password):
    password = password.lower()
    result= []
    point_idx = 0
    for ch in ciphertext:
        if ch in CHAR_INDEX:
            shift = CHAR_INDEX[password[point_idx]]
            new_idx = (CHAR_INDEX[ch] - shift) % CHAR_COUNT
            result.append(INDEX_CHAR[new_idx])
            point_idx = (point_idx + 1) % len(password)
    return "".join(result)

# demonstration

plaintext = "нельзя недооценивать противника"
c = route_encrypt(plaintext, 6, 5, "пароль")
print("Route ciphertext:", c)
print("Route decrypted: ", route_decrypt(c, 6, 5, "пароль"))


plaintext2="договор подписали"
c2= grille_encrypt(plaintext2, 2, "шифр")
print("\nGrille ciphertext:", c2)
print("Grille decrypted:", grille_decrypt(c2, 2, "шифр"))

plaintext3 = "криптография серьезная наука"
c3 = vigenere_encrypt(plaintext3, "математика")
print("\nVigenere ciphertext:", c3)
print("Vigenere decrypted:", vigenere_decrypt(c3, "математика"))

