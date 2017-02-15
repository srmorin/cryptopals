from copy import deepcopy

base64chars = list(chr(x) for x in range(ord('A'), ord('Z') + 1)) + \
              list(chr(x) for x in range(ord('a'), ord('z') + 1)) + \
              list(chr(x) for x in range(ord('0'), ord('9') + 1)) + \
              list('+') + \
              list('/')


def base64char(value):
    """
    Converts a 6 bit value to the base64 encoded string
    :param value: 6 bit value
    :return:
    """
    return base64chars[value]


def base64string(x):
    """
    Converts a string to base64 representation
    :param x: bytearray to convert
    :return: base64 string representation
    """

    local = deepcopy(x)

    # in the event the string doesn't have an equal number of bytes
    while (len(local) % 3 != 0):
        local.insert(0, int(0))

    ret = ''
    while (len(local) > 0):
        b = local[0:3]
        ret += base64char(b[0] >> 2)                                     # 6 - shift b[0] 6 bits to the right
        ret += base64char(((b[0] & 0x03) << 4) + ((b[1] & 0xF0) >> 4))   # 2/4 - shift b[0] & 0b00000011 to the left, and take first four bits of b[1]
        ret += base64char(((b[1] & 0x0F) << 2) + ((b[2] & 0xC0) >> 6))   # 4/2 - shift b[1]
        ret += base64char((b[2] & 0x3F))                                 # 6 - LSB for the b[2]
        local = local[3:]

    return ret
