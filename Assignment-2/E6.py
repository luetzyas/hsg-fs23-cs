# imports
from Cryptodome.Hash import SHA256
from struct import pack

known_m = "name=yasminesmeralda.luetzelschwab@student.unisg.ch&role=user"
my_hsg_MAC = "186f61d2ce80e8a6fc98a371bf2f91ff2da109ecdb6bdf9344376975e7272355"
key_length = 12  # standard ASCII characters
adversary_data = "&role=admin@attack.successfull!luetzyas"  # attack with the admin role

def calc_sha256_m_pad(m_len, k_len):
    # Total length in bits
    length = (m_len + k_len) * 8

    # Start with a '1' bit followed by '0' bits so that the total length is a multiple of 512
    # minus the 64 bits used to store the length of the message, but must end with it
    padding = '1' + '0' * ((448 - length - 1) % 512) + format(length, '064b')

    # Convert the padding from a string of '0's and '1's to bytes
    padding_b = int(padding, 2).to_bytes((len(padding) + 7) // 8, byteorder='big')
    return padding, padding_b


def perform_length_extension_attack(orig_m, orig_MAC_hex, new_data, k_len):
    orig_MAC_b = bytes.fromhex(orig_MAC_hex)
    orig_m_len = len(orig_m)
    padding, padding_b = calc_sha256_m_pad(orig_m_len, k_len)

    # forge valid new message-MAC pair (m', MAC(k,m'))
    h = SHA256.new()
    h._sha256__h = tuple(int.from_bytes(orig_MAC_b[i:i + 4], 'big') for i in range(0, 32, 4))
    h.update(new_data.encode())
    new_MAC_hex = h.hexdigest()

    res_m = orig_m + padding + new_data
    return new_MAC_hex, res_m


new_MAC, new_m = perform_length_extension_attack(known_m, my_hsg_MAC, adversary_data, key_length)

print("Exercise 6::\n")
print(f"Original MAC: {my_hsg_MAC}")
print(f"Original message: {known_m}")
print(f"New MAC: {new_MAC}")
print(f"New message: {new_m}")
