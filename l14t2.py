sentence = "thE five Boxing wizards JUMP quickly";
splitsentence = sentence.split();
for word in splitsentence:
    if word.islower():
        print(word+", ",end="");
