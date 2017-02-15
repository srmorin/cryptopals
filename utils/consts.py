base64chars = list(chr(x) for x in range(ord('A'), ord('Z') + 1)) + \
              list(chr(x) for x in range(ord('a'), ord('z') + 1)) + \
              list(chr(x) for x in range(ord('0'), ord('9') + 1)) + \
              list('+') + \
              list('/')

english_alphabet_letters = list(chr(x) for x in range(ord('a'), ord('z') + 1))

# Source for these is wikipedia
english_letter_frequency = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                            'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                            'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
                            'q': 0.10, 'z': 0.07}

english_letter_frequency_bow = {'a': 11.6, 'b': 4.7, 'c': 3.51, 'd': 2.67, 'e': 2.01, 'f': 3.78, 'g': 1.95, 'h': 7.23,
                                'i': 6.29, 'j': 0.6, 'k': 0.59, 'l': 2.71, 'm': 4.38, 'n': 2.37, 'o': 6.26, 'p': 2.55,
                                'q': 0.17, 'r': 1.65, 's': 7.76, 't': 16.67, 'u': 1.49, 'v': 0.65, 'w': 6.75, 'x': 0.02,
                                'y': 1.62, 'z': 0.03}


