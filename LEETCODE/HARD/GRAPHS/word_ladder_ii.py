"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []

Constraints:
- 1 <= beginWord.length <= 5
- endWord.length == beginWord.length
- 1 <= wordList.length <= 500
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.
"""

from collections import defaultdict, deque

def find_ladders(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return []
    
    layer = {begin_word: [[begin_word]]}
    
    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == end_word:
                return layer[word]
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        new_layer[new_word] += [path + [new_word] for path in layer[word]]
        
        word_set -= set(new_layer.keys())
        layer = new_layer
    
    return []

try:
    begin_word = input("ENTER BEGIN WORD\n")
    end_word = input("ENTER END WORD\n")
    word_list = input("ENTER WORD LIST (space separated)\n").split()
    print(f"LADDERS: {find_ladders(begin_word, end_word, word_list)}")
except Exception as e:
    print(f"An error occurred: {e}")
