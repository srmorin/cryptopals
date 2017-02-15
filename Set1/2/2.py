from utils.conversion import HexString
from utils.conversion import ByteArray


def main():
    exercise_string_1 = '1c0111001f010100061a024b53535009181c'
    exercise_string_2 = '686974207468652062756c6c277320657965'
    expected_string = '746865206b696420646f6e277420706c6179'

    b1 = HexString.convertToBinaryArray(exercise_string_1)
    b2 = HexString.convertToBinaryArray(exercise_string_2)

    b3 = ByteArray.xor(b1, b2)

    result = ByteArray.convertToHexString(b3)
    print result
    print result == expected_string


if __name__ == "__main__":
    main()
