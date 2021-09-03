class Node:
    def __init__(self, key):
        self.child = {}
        self.cnt = 0
        
class Trie:
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, data):
        current = self.root
        
        for char in data:
            if char not in current.child:
                current.child[char] = Node(char)
            current.cnt += 1
            current = current.child[char]
        current.cnt += 1
        
    def search(self, query):
        curr_node = self.root
        for q in query:
            if q == "?":
                break
            if q in curr_node.child:
                curr_node = curr_node.child[q]
            else:
                return 0
        return curr_node.cnt
    
def solution(words, queries):
    answer = []
    trie = [Trie() for _ in range(10001)]
    rev_trie = [Trie() for _ in range(10001)]
    for word in words:
        trie[len(word)].insert(word)
        rev_trie[len(word)].insert(word[::-1])
        
    for query in queries:
        if query[-1] == "?":
            rst = trie[len(query)].search(query)
        else :
            rst = rev_trie[len(query)].search(query[::-1])
        answer.append(rst)
    return answer