# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, words):
        return [w for w in words if self.word != w and sorted(self.word) == sorted(w)]
    
listen = Anagram("listen")
print(listen.match(["enlist", "google", "inlets", "banana"]))
