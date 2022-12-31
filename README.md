# Kanji of the day

This is just a simple script that picks a random kanji from a list of the 2136 Jōyō kanji and prints some info on it scraped from jisho.org, a popular english-japanese dictionary.  
The format of the info goes something like this:  
```
[kanji] [en meanings]  
onyomi: [onyomi reading in katakana] [romaji of reading]  
kunyomi: [kunyomi reading in hiragana] [romaji of reading]  
Examples:  
[word with kanji] [reading of word] [romaji of reading] | [en definition]  
...  
```  
Notes:  
- Some kanjis do not have kunyomi or onyomi readings, that has been accounted for.  
- Sometimes the kanji isn't used in the examples that get scraped. This is because there are many kanji that often share the same meaning and pronunciation with each other, often times because one is either the Kyūjitai form of the other or some variant. Jisho knows this displays the most common form, which may be different from the one searched. You will still see the kanji under "other forms" though.

There's also a web scraper for Google's weather card when you google "weather [city name]". I added it because I thought it was cool.

Thanks to this repository, https://github.com/pedroallenrevez/jisho-api , I was able to take their jisho webscraper as an api and use it in my script.
Under the jisho_api folder and the requests file I took three functions that scrapes jisho.org for three things:  
the meaning of an individual kanji,
the readings of an individual kanji, and the examples of the kanji in words.  
I then wrote two more functions to romanize the readings.
