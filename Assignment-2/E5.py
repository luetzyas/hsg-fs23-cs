# imports
from code_collection import *

def hash_sentence(s, size):
    return hashlib.blake2s(s.encode(), digest_size=size).hexdigest()


def generate_sentence(i):
    generator = DocumentGenerator()
    g_sentence = generator.sentence()
    print(f"S{i}: " + g_sentence)
    return g_sentence.lstrip()


def generate_sentence_words_fix():
    # Predefined parts of speech
    subjects = ["The cat", "A dog", "My neighbor", "The teacher", "Our team"]
    verbs = ["saw", "met", "is considering", "likes", "dislikes"]
    objects = ["a movie", "the play", "a good book", "the new student", "the game"]
    adverbs = ["quickly", "slowly", "happily", "sadly", "quietly"]
    adjectives = ["a beautiful", "an interesting", "a boring", "a thrilling", "an exciting"]

    # Constructing the sentence
    sentence = random.choice(subjects) + " " + \
               random.choice(verbs) + " " + \
               random.choice(adjectives) + " " + \
               random.choice(objects) + " " + \
               random.choice(adverbs) + "."

    return sentence


g_file_1 = f"output/generates_sentences_1.txt"
g_file_2 = f"output/generates_sentences_2.txt"

hash_list = {}
sentences = []
output_print = "No sentences found!"

# control parameters
size = 6  # bit size
generate = 0  # generate sentence true/false

# clear result file
file_res = open("output/so14.txt", 'w')

# generate sentence with 2 different generators
if generate:
    file_1 = open(g_file_1, 'w')
    file_2 = open(g_file_2, 'w')
    for i in range(1000):
        # this sentence generator is based on the python document sentence generator (random) and takes e.g.
        # 2s/sentence to generate for this file for 6 and 7 bytes no same hash with different sentences could be found
        file_1.write(generate_sentence(i) + "\n")

        # generate random sentences with specific words, structure = more feasible that the same sentence occurs =
        # same hash does not really generate the wanted output
        file_2.write(generate_sentence_words_fix() + "\n")

# decide current used input file
sentences = read_input(g_file_1) + read_input(g_file_2)

for s in sentences:
    hash_value = hash_sentence(s, size)

    # check if generated hash is in the computed hash list
    # AND
    # check if it's not the same sentence
    if hash_value in hash_list and hash_list[hash_value] != s:
        output_print = f"Sentences found!\nS1: {s}\nS2: {hash_list[hash_value]}"

        # write outputfile when found
        file_res.write(f"{hash_list[hash_value]}\n{s}")

        break

    # save key-value pair
    hash_list[hash_value] = s

print("Exercise 5::")
print(output_print)
