text = "Baseball4";
if text.isalnum():
    print(text, " is alphanumberic");
else:
    print(text," is not alphanumberic");
text = "Baseball 4";
if text.isalnum():
    print(text, " is alphanumeric");
else:
    print(text, " is not alphanumeric");
text = "abcgh";
if text.isalpha():
    print(text, " is all letters");
else:
    print(text, " is not all letters");
text = "cat dog";
if text.isalpha():
    print(text, "is all letters");
else:
    print(text, " is not all letters")

text = "dog cat";
if text.islower():
    print(text, "is all lowercase");
else:
    print(text, " is not all lowercase");

text = "Dog Cat";
if text.islower():
    print(text, "is all lowercase");
else:
    print(text, " is not all lowercase")

text = "5";
if text.isnumeric():
    print(text, "is all numeric");
else:
    print(text, " is not all numeric")

text = "five";
if text.isnumeric():
    print(text, "is all numeric");
else:
    print(text, "is not all numeric")

text = "MR HEDAHL";
if text.isupper():
    print(text, "is all upercase");
else:
    print(text, " is not all upercase")

text = "Mr. Hedahl";
if text.isupper():
    print(text, "is all upercase");
else:
    print(text, "is not all upercase")

text = "7";
if text.isdigit():
    print(text, "is all digits");
else:
    print(text, " is not all digits")

text = "seven";
if text.isdigit():
    print(text, "is all digits");
else:
    print(text, "is not all digits")

