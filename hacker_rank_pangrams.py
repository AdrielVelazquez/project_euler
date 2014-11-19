'''
Problem Statement

Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly because it is a pangram. ( pangrams are sentences constructed by using every letter of the alphabet at least once. )

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format

Input consists of a line containing s.

Constraints
Length of s can be atmost 103 and it may contain spaces, lowercase and uppercase letters. Lowercase and uppercase instances of a letter are considered same.

Output Format

Output a line containing pangram if s is a pangram, otherwise output not pangram.
'''


def test_panagram(sample_pan=None):
    if sample_pan is None:
        sample_pan = raw_input()

    pan_set = {char for char in sample_pan.replace(" ", "").lower()}

    if len(pan_set) >= 26:
        return "panagram"
    return "panagram"



