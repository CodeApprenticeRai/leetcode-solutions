class Solution:
    def longestCommonPrefix(self, strings):
        if not strings:
            return ""

        string_lengths = []
        length_of_shortest_string = float('inf')
        index_of_shortest_string = None
        for i in range(len(strings)):
            if not strings[i]:
                return strings[i]
            string_lengths.append(len(strings[i]))
            if len(strings[i]) < length_of_shortest_string:
                length_of_shortest_string = len(strings[i])
                index_of_shortest_string = i

        common_prefix = ""
        for i in range(length_of_shortest_string):
            compare_character = strings[index_of_shortest_string][i]
            for j in range(len(strings)):
                if (((i + 1) > len(strings[j])) or (strings[j][i] != compare_character)):
                    return common_prefix
            common_prefix += compare_character

        return common_prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]) == "fl")