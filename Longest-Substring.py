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
