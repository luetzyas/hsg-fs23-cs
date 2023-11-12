# imports
from code_collection import *

print("Exercise 6::")
m_file = read_input_int("input/aux_5.txt")

# select values from input file
e = m_file.get('e')
N_A = m_file.get('N_A')
N_B = m_file.get('N_B')
c_A = m_file.get('c_a')
c_B = m_file.get('c_b')

# calculate gcd for Alice and Bob
gcd = math.gcd(N_A, N_B)

#decrypt the read messages from the inputfile
decrypt(N_B, gcd, e, c_A, "Bob")  # Bob >> Alice
decrypt(N_A, gcd, e, c_B, "Alice")  # Alice >> Bob

"""
    Exercise 6::
    Message from Bob:  Hi Bob! Aren't I glad that we saved all that energy!
    Message from Alice:  We sure did, I feel so smart now! Go team green!
"""