base64chars = list(chr(x) for x in range(ord('A'), ord('Z') + 1)) + \
              list(chr(x) for x in range(ord('a'), ord('z') + 1)) + \
              list(chr(x) for x in range(ord('0'), ord('9') + 1)) + \
              list('+') + \
              list('/')
