from utils.conversion import HexString
from utils.conversion import ByteArray


def main():
    exercise_string_1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    b_exercise_string_1 = HexString.convertToBinaryArray(exercise_string_1)

    #TODO(srmorin): add frequency analysis to guess at specific ones
    #TODO(srmorin): add a function to do the single digit xoring

    for i in range(0, 255):
        newarray = bytearray()
        for c in range(0, len(b_exercise_string_1)):
            newarray.append(i ^ b_exercise_string_1[c])

        print '%i: %s' % (i, newarray)


if __name__ == "__main__":
    main()
