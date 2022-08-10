strs = ["eat","tea","tan","ate","nat","bat"]



class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            return list(anagrams.values())

groupAnagrams(strs)