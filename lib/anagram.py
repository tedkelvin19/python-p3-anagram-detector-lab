# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        matches = []
        for anagram in possible_anagrams:
            if sorted(anagram.lower()) == sorted(self.word.lower()) and anagram.lower() != self.word.lower():
                matches.append(anagram)
        return matches
    
listen = Anagram("listen")
print(listen.match(["enlist", "google", "inlets", "banana"]))
print(sorted([1,3,2])==sorted([3,2,1]))


