import time

alf = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

txt = 'In the wake of Hurricane Milton, NASA is deploying resources to support Federal Emergency Management Agency (FEMA) and state emergency management agencies to aid their response effort including satellite and aerial data collection. The agency’s Disasters Response Coordination System and Airborne Science Program are began conducting flights Friday to provide emergency responders with better insight into flooding, damage in Florida, and debris.'
filteredTxt = ''.join([char for char in txt.upper() if char in alf])

key = ['432', 'DCBAE']

alf_polybius = [[] for i in range(5)]
key_polybius = [[] for i in range(5)]
key_polybius_used_letters = set()

def auto_attack():
    t0 = time.time()

    while time.time() - t0 < 5:
        print(time.time() - t0)

# Tablica dla alfabetu
for i, letter in enumerate(alf):
    row_index = i % 5
    alf_polybius[row_index].append(letter)

# Funckja do tworzenia tablicy z kluczem
def add_letter(letter):
    if letter not in key_polybius_used_letters:
        for i in range(5):
            if len(key_polybius[i]) < 5:
                key_polybius[i].append(letter)
                key_polybius_used_letters.add(letter)
                break
            else:
                continue

# Dodawanie liter z klucza do tablicy
for letter in key[1]:
    add_letter(letter)

# Uzupełnianie tablicy pozostałymi literami alfabetu
for letter in alf:
    add_letter(letter)

# Funkcja pomocnicza do szyfrowania - dzieli tekst na fragmenty odpowiedniej długosci (zgodnie z kluczem) i je odwraca
def transpose(txt, key_numeric):
    key_lengths = [int(k) for k in key_numeric]
    result = []
    current_index = 0

    while current_index < len(txt):
        for length in key_lengths:
            if current_index >= len(txt):
                break
            segment = txt[current_index:current_index + length]

            segment = segment[::-1]
            result.append(segment)
            current_index += length
    return ''.join(result)

def encrypt(alf_polybius, key_polybius, txt, key):
    c_txt = ""

    # Znajdź pozycje kolejnej litery tekstu w tablicy alfabetu następnie weź litere która znajduje się pod tą pozycją w tablicy z kluczem
    for letter in txt:
        for i, row in enumerate(alf_polybius):
            if letter in row:
                col = row.index(letter)
                c_txt += key_polybius[i][col]
                break

    c_txt_transpose = transpose(c_txt, key[0])
    return c_txt_transpose

def decrypt(alf_polybius, key_polybius, txt, key):
    p_txt = ""

    # Odwrócona logika względem encrypt
    for letter in txt:
        for i, row in enumerate(key_polybius):
            if letter in row:
                col = row.index(letter)
                p_txt += alf_polybius[i][col]
                break

    p_txt_transpose = transpose(p_txt, key[0])
    return p_txt_transpose

print("Tablica z alfabetem")
for row in alf_polybius:
    print(row)

print("Tablica z kluczem")
for row in key_polybius:
    print(row)

print("Tekst początkowy: ", filteredTxt)

encrypt_txt = encrypt(alf_polybius, key_polybius, filteredTxt, key)
print("Zaszyfrowany tekst: ", encrypt_txt)

decrypt_txt = decrypt(alf_polybius, key_polybius, encrypt_txt, key)
print("Odszyfrowany tekst: ", decrypt_txt)

