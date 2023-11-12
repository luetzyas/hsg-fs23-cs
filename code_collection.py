import math
import random
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
from Cryptodome.Random import get_random_bytes
import os


def read_input_int(file_path):
    # Initialize an empty dictionary to store the values
    values = {}

    with open(file_path, 'r') as m_file:
        for line in m_file:
            # print(f"Reading line: {line}")  # Debugging print statement
            parts = line.split('=')
            if len(parts) == 2:
                key = parts[0].strip()
                try:
                    value = int(parts[1].strip())
                    values[key] = value
                except ValueError:
                    print(f"Error parsing line: {line}")  # Error in parsing value

    return values


def read_input_bytes(file_path):
    # Initialize an empty dictionary to store the values
    values = {}

    # Open the file and process each line
    with open(file_path, 'r') as m_file:
        for line in m_file:
            # Split the line into key and value parts
            parts = line.split('=')
            if len(parts) == 2:
                key = parts[0].strip()
                value = bytes.fromhex(parts[1])

                # Store the key-value pair in the dictionary
                values[key] = value

    return values


# This function checks if an integer is prime, returns True if it is and False otherwise
# You do not need to understand how it works, and you can assume that it works correctly.
# The code is just here for completeness
def is_prime(n):
    if n < 0:
        n = -n

    if (n == 2) or (n == 3):
        return True

    if ((n % 2) == 0) or (n == 1) or (n == 0):
        return False

    r, s = 0, n - 1
    while ((s % 2) == 0):
        r += 1
        s //= 2
    for _ in range(20):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_random_prime(seed):
    random.seed(seed)
    p = 1
    while (not is_prime(p)) or ((p % 65537) == 1):
        p = random.randint(2 ** 1023, 2 ** 1024)
    return p


def string_to_int(s):
    return int.from_bytes(s.encode(), byteorder='little')


# Turn an integer back to a string of characters
def int_to_string(i):
    length = math.ceil(i.bit_length() / 8)
    return i.to_bytes(length, byteorder='little').decode()


def hex_to_text(hex_string):
    try:
        # Convert the hex string to bytes
        bytes_data = bytes.fromhex(hex_string)
        # Decode the bytes to a string using UTF-8 encoding
        text = bytes_data.decode('utf-8')
        return text
    except ValueError as e:
        return f"Error converting hex to text: {e}"
    except UnicodeDecodeError as e:
        return f"Error decoding bytes: {e}"


def hex_to_bytes(hex_string):
    return bytes.fromhex(''.join(hex_string.split()))


def decrypt(pk, gcd, e, c, person):
    p = gcd  # set 1. prime
    q = pk // p  # set 2. prime with 1. prime from gcd
    phi = (p - 1) * (q - 1)  # phi using eulers f
    d = pow(e, -1, phi)  # modular inverse
    m = pow(c, d, pk)
    print("Message from " + person + ": ", int_to_string(m))


def decrypt_aes_ctr(k, c, iv):
    ctr = Counter.new(nbits=8, suffix=iv, initial_value=0)
    cipher = AES.new(k, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(c)


def xor(a, b):
    # Ensure that a and b are of the same length
    length = min(len(a), len(b))
    return bytes([a[i] ^ b[i] for i in range(length)])


def get_iv():
    base_b = (b'\x00' * 14)
    iv = {'C21': b'\x00' + base_b,  # first
          'C22': b'\x01' + base_b,  # second
          'C31': b'\x00' + base_b,  # first
          'C33': b'\x02' + base_b   # third
          }
    return iv
