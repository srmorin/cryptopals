from utils.consts import base64chars
from utils.conversion import HexString
from utils.base64 import base64string


def main():
    exercise_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    b = HexString.convertToBinaryArray(exercise_string)

    print len(base64string(b))
    print (base64string(b) == expected_string)

    print exercise_string

if __name__ == "__main__":
    main()
