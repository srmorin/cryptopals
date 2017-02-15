
class HexString:

    @staticmethod
    def convertToBinaryArray(hexstr):
        """
        :param hexstr: string represented as a hexademical
        :return: a bytearray representation of the hexstring
        """
        # convert to lower case
        hexstr = hexstr.lower()

        # drop the leading 0 if necessary
        if hexstr.startswith('0x'):
            hexstr = hexstr[2:]

        # in the event the string has an odd number of characters, start with an extra zero
        if len(hexstr) % 2 != 0:
            hexstr = '0' + hexstr

        b = bytearray()
        while len(hexstr) > 0:
            b.append(int(hexstr[:2], 16))
            hexstr = hexstr[2:]

        return b

class ByteArray:

    @staticmethod
    def convertToHexString(bytarray):
        """
        :param bytarray: binaryarray
        :return: a string containing a hexadecimal representation
        """

        ret = ''
        for c in range(0, len(bytarray)):
            ret += hex(bytarray[c]).lower().replace('0x', '')

        return ret
