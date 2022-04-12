from textblob import TextBlob
paragraph = "Rohan was pleyig in otuside wenh he swa a sapcecrkatf lnad on his frton yard. He wnet to call hsi mom, but by teh tmie they rechead it was gnoe"
language = TextBlob(paragraph)
language=language.correct()
print(language)