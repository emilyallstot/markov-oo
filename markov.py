import sys
from random import choice

class SimpleMarkovGenerator(object):

    def __init__(self):
        pass

    def make_values(self, corpus, word_key):

        word_key = tuple(word_key)

        values_list = []
        
        file = open(corpus)

        lastword = ""
        last_key = ()

        for line in file:
            line = line.strip()
            words = line.split(" ")
            
            if last_key == word_key:
                values_list.append(words[0])

            if word_key[1] == words[0]:
            
                if word_key[0] == lastword:
                    # print word_key
                    values_list.append(words[1])
                    
            i = 0
            while i < len(words) - 2:
                if word_key[0] == words[i]:
                    if word_key[1] == words[i + 1]:
                        values_list.append(words[i + 2])
                i += 1

            last_key = tuple(words[-2:])
            lastword = words[-1]

        return values_list

    def read_files(self,corpus):
        """Takes input text as string; returns dictionary of markov chains."""

        file = open(corpus)
        markov_dictionary = {}
        word_key = ['None', 'None']
        word_list = []
        lastword = ""
    #use for loop to make lines in file a list
        for line in file:
            line = line.strip()
            words = line.split(" ")
            
            # generate keys
            word_key[0] = lastword
            word_key[1] = words[0]
            
            if lastword:
                markov_dictionary[tuple(word_key)] = self.make_values(corpus, word_key)

            i = 0
            while i < len(words) - 1:
                word_key[0] = words[i]
                word_key[1] = words[i + 1]
         
                markov_dictionary[tuple(word_key)] = self.make_values(corpus, word_key)

                i += 1

            lastword = words[len(words) - 1]

        # print "make_chains", markov_dictionary
        return markov_dictionary

x = SimpleMarkovGenerator()
print x.read_files("green-eggs.txt")

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

#     def make_text(self):
#         """Takes dictionary of markov chains; returns random text."""

#         chains = {}

#         words = input_text.split()

#         for i in range(len(words) - 2):
#             key = (words[i], words[i + 1])
#             value = words[i + 2]

#             if key not in chains:
#                 chains[key] = []

#             chains[key].append(value)


#         key = choice(chains.keys())
#         words = [key[0], key[1]]
#         while key in chains:
#             # Keep looping until we have a key that isn't in the chains
#             # (which would mean it was the end of our original text)
#             #
#             # Note that for long texts (like a full book), this might mean
#             # it would run for a very long time.

#             word = choice(chains[key])
#             words.append(word)
#             key = (key[1], word)

#         return " ".join(words)


# # Gather our code in a main() function
# # from http://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script
# def main():

#     input_path = sys.argv[0] 
#     input_text = open(input_path).read()

#     # # Get a Markov chain
#     # chains = make_chains(input_text)

#     # # Produce random text
#     # random_text = make_text(chains)

#     # print random_text
    
#     # we should make an instance of the class
#     x = SimpleMarkovGenerator()

#     # we should call the read_files method with the list of filenames
#     chains = x.read_files(input_path)

#     # we should call the make_text method 5x
#     for i in range(5):
#         x.make_text()





# if __name__ == "__main__":
#     main()
