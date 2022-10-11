phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = plist[1:3]
new_phrase.extend(plist[5:3:-1])
new_phrase.extend(plist[7:5:-1])
new_phrase = ''.join(new_phrase)

print(plist)
print(new_phrase)
