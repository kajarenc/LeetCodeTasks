from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    begin = 0
    end = 0

    max_length = 0

    if not s:
        return max_length

    last_appeared_index = defaultdict(int)

    counter_dict = defaultdict(int)
    n = len(s)
    while end < n:
        counter_dict[s[end]] += 1

        while counter_dict[s[end]] > 1:
            counter_dict[s[begin]] -= 1
            begin = begin + 1

        last_appeared_index[s[end]] = end

        if end - begin + 1 > max_length:
            max_length = end - begin + 1

        end += 1

    return max_length


assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("abba") == 2
assert lengthOfLongestSubstring("wwkew") == 3
