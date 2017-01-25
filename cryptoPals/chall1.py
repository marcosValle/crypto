# cryptopals chall 1
# Convert hex string to base64
# RULE: Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
import binascii

def h2b64(h):
    #hex to bin
    b = binascii.unhexlify(h)

    #bin to base64
    return binascii.b2a_base64(b)[:-1].decode('ascii')

print(h2b64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
