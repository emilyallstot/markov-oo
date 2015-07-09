import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, corpus):
        """Given a list of files, make chains from them."""

        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        return chains


    def make_chains(self, input_text):
        """Takes input text as string; stores chains."""

        chains = {}

        words = input_text.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        return chains


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)


input_path = sys.argv[1]
input_text = open(input_path).read()

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

if __name__ == "__main__":
    # we should get list of filenames from sys.argv
    script = sys.argv[0]
    filename = sys.argv[1]
    

    
    # we should make an instance of the class
    x = SimpleMarkovGenerator()

    # we should call the read_files method with the list of filenames
    chains = x.read_files(filename)

    # we should call the make_text method 5x
    for i in range(5):
        x.make_text(chains)


    pass