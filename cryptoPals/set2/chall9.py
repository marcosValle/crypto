# Implement PKCS#7 padding

def pad(msg, size):
    padSize = size - len(msg)%size
    return msg+padSize*"\\x{:02x}".format(padSize)

if __name__ == "__main__":
    msg = "YELLOW SUBMARINE"
    size = 20
    print(pad(msg, size))

