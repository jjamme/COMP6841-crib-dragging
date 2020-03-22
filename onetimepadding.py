LETTER_TO_NUM = {}
NUM_TO_LETTER = {}

def dictionary_fill():
    global LETTER_TO_NUM, NUM_TO_LETTER

    for alpha in "abcdefghijklmnopqrstuvwxyz":
        LETTER_TO_NUM[alpha] = ord(alpha) - 96
        NUM_TO_LETTER[ord(alpha) - 96] = alpha


def make_key(guess_word, guess_cipher):
    index = 0
    key = ""

    while index < len(guess_word):
        x = (LETTER_TO_NUM[guess_cipher[index]] - LETTER_TO_NUM[guess_word[index]]) % 26
        x = 26 if x == 0 else x
        key += NUM_TO_LETTER[x]
        index += 1
    
    return key
    

def decoder(cipher, key):
    new_cipher = ""

    index = 0
    while index < len(key):
        new_cipher += NUM_TO_LETTER[(LETTER_TO_NUM[cipher[index]] - LETTER_TO_NUM[key[index]]) % 26]
        index += 1
    
    return new_cipher


def main():
    ciphers = [
        'lpagbbfctnipvwdbjnpuqolhhtygwheuafjlirfpxxl',
        'wdafvnbcdymxeeulwotpoofnilwnglhblufecvqaxs',
        'uijmltdjeumxunbikstvdrvhcodasulrvdypegublg',
        'lpaalrhgmjikgjdmllcsnnymisopcglagtkeqcemiu',
        'lpadohqcozvbglebjpdtnotzbyrbuwgftfltlipiqp'
    ]

    guess_word = str(input("Guess the words on the plaintext: "))
    guess_cipher = int(input("Which ciphertext? "))

    key = make_key(guess_word, ciphers[guess_cipher])

    print("Your key:", key)

    for cipher in ciphers:
        print(decoder(cipher, key))
    
    


if __name__ == "__main__":
    dictionary_fill()
    main()
