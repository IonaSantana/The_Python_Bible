from ast import IsNot, NotIn


frase = input().strip().lower().split()
frase1 = []
for word in frase:
    if word[0] in 'aeiou':
        frase1.append(word + 'yay')
    else:
        vowel_pos = 0
        for w in word:
           if w not in 'aeiou':
               vowel_pos = vowel_pos + 1
           else:
                break
        frase1.append(word[vowel_pos:] + word[:vowel_pos] + "ay")

print(" ".join(frase1))