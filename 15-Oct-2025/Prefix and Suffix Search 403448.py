# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = {}
        for index, word in enumerate(words):
            self.insert(word, index)

        
    def insert_rev(self, word, node, word_index):
        rev_word = word[::-1]
        for char in rev_word:
            rev_char = 'rev_'+char
            if rev_char not in node:
                node[rev_char] = {}
            node = node[rev_char]
            node['index'] = word_index

    def insert(self, word, word_index):
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                curr_node[char] = {'index':word_index}
            curr_node = curr_node[char]
            self.insert_rev(word, curr_node, word_index)

        curr_node['index'] = max(curr_node['index'], word_index)

            
    def get_prefix_end_node(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node:
                return None
            curr_node = curr_node[char]
        return curr_node

 
    def f(self, pref: str, suff: str) -> int:
        node = self.get_prefix_end_node(pref)
        if not node:
            return -1
       
        for char in suff[::-1]:
            rev_char = 'rev_'+char
            if rev_char not in node:
                return -1
            node = node[rev_char]
        return node['index']
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)