"""
def longestBeautifulSubstring(word:str)->int:
    vowels='aeiou'
    longest=0
    start=0
    for i in range(len(word)):
        if i>0 and word[i]<word[i-1]:
            start=i
        if word[i]==vowels[-1]:
            if all(v in word[start:i+1] for v in vowels):
                if i-start+1>longest:
                    longest=i-start+1
            else:
                start=i
    return longest
def main():
    word="aeeiiouu"
    longest=longestBeautifulSubstring(word)
    print(longest)
"""
"""
StrVowel="aeeiiouu"
vowels='aeiou'
x=0
str1=""
n1=""
for i in StrVowel:
    if i==vowels[x]:
        str1=str1+i
    if x<(len(vowels)-1):
        if i==vowels[x+1]:
            str1=str1+i
            x=x+1
for i in StrVowel:
    if i not in n1:
        n1=n1+i
n1="".join(sorted(n1, key=str.lower))
if n1!=vowels:
    print(0)
    print(n1)
else:
    print(len(str1))
    """


word="aeiaaiooaa"
vowels='aeiou'    
longest=0
start=0
for i in range(len(word)):
    if i>0 and word[i]<word[i-1]:
        start=i
    if word[i]==vowels[-1]:
        if all(v in word[start:i+1] for v in vowels):
            if i-start+1>longest:
                longest=i-start+1
        else:
            start=i
print(longest)
