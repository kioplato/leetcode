#!/usr/bin/python2.7
# 5. Longest Palindromic Substring

class Solution(object):
    # O(n) complexity.
    def find_char(self, string, c, start, limit):
        """
        Finds and returns the index of the the next start - 1 character from the
        end of the string. If such character is not found return -1.
        :type string: str  # String to search into.
        :type c: char  # Character to find in string.
        :type start: int  # Start searching from string[start] for c.
        :type limit: int  # Stop searching after string[limit] for c.
        :rtype: int  # The index of the found character c. -1 if not found.
        """
        for c_char in range(limit, start - 1, -1):
            if c == string[c_char]:
                return c_char
        return -1
    # O(n) complexity.
    def find_limit(self, occurs, string, start):
        """
        Finds the smallest index between start and len(string) - 1 such that the
        string defined by string[start:index + 1] contains at most one character
        that occurs only once.
        :type occurs: dictionary  # Stores for each char the # of occurances.
        :type string: str  # The string to search into.
        :type start: int  # Start searching from string[start].
        :rtype: int  # The smallest index found. Worst case is start + 1.
        """
        has_single = False
        for c_char in range(start, len(string)):
            if occurs[string[c_char]] == 1:
                if has_single == False:
                    has_single = True
                else:
                    return c_char - 1
        return c_char
    # O(n) complexity.
    def is_palindrome(self, string):
        """
        Checks if the given string is palindromic or not.
        If it is return true, otherwise return false.
        :type string: str  # The string to check if it's palindromic.
        :rtype: boolean  # Returns True if palindromic otherwise False.
        """
        reversed_string = string[::-1]  # Reverse the string.
        for c_char in range(0, len(string)):
            if string[c_char] != reversed_string[c_char]:
                return False
        return True
    # O(n^2) complexity.
    def longestPalindrome(self, string):
        """
        Finds the longest palindromic substring in string.
        :type string: str  # The string to search into.
        :rtype: str  # The longest palindromic substring.
        """
        occurs = dict()
        for c_char in range(0, len(string)):
            if string[c_char] in occurs:
                occurs[string[c_char]] += 1
            else:
                occurs[string[c_char]] = 1
        result = ""
        c_char = 0
        string_len = len(string)
        while c_char < string_len:
            if len(result) > len(string[c_char:string_len - 1]):
                break
            if occurs[string[c_char]] > 1:  # Character exists > 1 times.
                start = 0
                if result == "":
                    start = c_char + 1
                else:
                    start = c_char + len(result)
                limit = 0
                if c_char == string_len - 1:
                    limit = string_len - 1
                else:
                    limit = self.find_limit(occurs, string, c_char)
                    if limit < start:
                        c_char = start
                        continue
                r_index = self.find_char(string, string[c_char], start, limit)
                while (r_index != -1):
                    tmp = string[c_char:r_index + 1]
                    if (self.is_palindrome(tmp)):
                        if result == "":
                            result = tmp
                        elif len(tmp) > len(result):
                            result = tmp
                        break
                    limit = r_index - 1
                    r_index = self.find_char(string, string[c_char], start, limit)
            else: # Character exists only once.
                if result == "":
                    result = string[c_char]
            c_char += 1
        return result
