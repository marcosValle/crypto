# Implement PKCS#7 padding
def pad(msg, size):
    padSize = size - len(msg)%size
    return msg+bytearray([padSize]*padSize)
  
if __name__ == "__main__":
    msg = b'YELLOW SUBMARINE'
    size = 16
    print(pad(msg, size))

