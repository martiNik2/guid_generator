import random

def generate_guid():
    byte_order=[4,2,2,2,6]

    guid="-"

    for i,n in enumerate(byte_order):
        byte_order[i]=random.randbytes(n).hex()

    return guid.join(byte_order)