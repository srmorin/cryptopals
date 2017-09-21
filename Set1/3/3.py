from utils.conversion import HexString
from utils.conversion import ByteArray
from utils.consts import english_alphabet_letters


def analyze_text(decoded_string):
    """
    Scores a decoded string to see the likelihood that it contains english words.

    Very basic function that scores phrases based on the number of characters are valid.
    Not a great approach, but it found the one I was looking for on the first shot.
    :param decoded_string: byte array
    :returns: dictionary or score
    """
    #TODO(srmorin): create a better analyzer that does more than count decoded characters

    scored_dict = {}
    total_score = 0
    for c in range(0, len(decoded_string)):
        decoded_char = chr(decoded_string[c]).lower()
        if decoded_char in english_alphabet_letters:
            total_score += 1
            try:
                scored_dict[decoded_char] += 1
            except KeyError:
                scored_dict[decoded_char] = 1

    return total_score, scored_dict


def main():
    exercise_string_1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    b_exercise_string_1 = HexString.convertToBinaryArray(exercise_string_1)

    #TODO(srmorin): add a function to do the single digit xoring
    top_score = 0
    best_phrase = ''

    for i in range(0, 256):
        newarray = bytearray()

        for c in range(0, len(b_exercise_string_1)):
            decoded_c = i ^ b_exercise_string_1[c]
            newarray.append(decoded_c)
        total_score, scored_dict = analyze_text(newarray)

        if total_score > top_score:
            top_score = total_score
            best_phrase = newarray
            index = i

    print '%i: %s' % (index, best_phrase)


if __name__ == "__main__":
    main()
