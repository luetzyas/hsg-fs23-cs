import hmac

known_m = "name=yasminesmeralda.luetzelschwab@student.unisg.ch&role=user"
my_hsg_MAC = "186f61d2ce80e8a6fc98a371bf2f91ff2da109ecdb6bdf9344376975e7272355"
key_length = 12  # standard ASCII characters
adversary_data = "&role=admin@attack.successfull!luetzyas"  # attack with the admin role

def length_extension_attack(known_m, my_hsg_MAC, key_length, adversary_data):
    known_m_decoded = known_m
    my_hsg_MAC_decoded = bytes.fromhex(my_hsg_MAC)

    # The length of the unknown string should be equal to the length of the MAC
    unknown_m_length = len(my_hsg_MAC_decoded)

    # We iterate from the length of the known string until the length of the unknown string
    for i in range(len(known_m_decoded), unknown_m_length):
        # We add the known string and the part of the unknown string
        test_string = known_m_decoded + bytes([i - len(known_m_decoded)])

        # We generate the HMAC of the test string with a padding of zeros
        test_hmac = hmac.new(b'\x00' * key_length, test_string, hashlib.sha256).digest()

        # We XOR the first part of the test HMAC with the first part of the original MAC
        test_hmac = bytearray(test_hmac)
        test_hmac[:len(my_hsg_MAC_decoded)] = [x ^ y for x, y in zip(test_hmac, my_hsg_MAC_decoded)]

        # If the XOR operation resulted in a valid MAC, we have found the unknown string
        if hmac.compare_digest(test_hmac.hex(), my_hsg_MAC):
            return test_string.hex()

    # If the unknown string was not found, we return None
    return None

new_message = length_extension_attack(known_m, my_hsg_MAC, key_length, adversary_data)

if new_message:
    print("The new message is: " + new_message)
else:
    print("The new message could not be found.")