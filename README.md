# is-dirty
A very naive classifier to figure out if a sentence contains dirty words. Works for English well, and can handle popular Spanish, Indonesian, Arabic and Hindi explicit words.


## Motivation
I quickly wrote up this script to figure out a reasonable approximation of how many results in a given list were porny/explicit. I couldn't find a simple enough script to just plug-and-play. So I hacked up this. 

## How it works
Essentially the algorithm has a corpus of explicit words (I have supplied a predominantly English corpus, but I added enough popular expletives in other languages). The script expects a list of sentences, one on each line, and then checks if there are any explicit words as a substring of each line. (Check the caveats section)

Which ever lines had potentially explicit content, are written to a new file with the same name as the original file with list of sentences to inspect, but with a '.porny' extension added in the end. Similarly, all the supposedly clean lines are added to a new file with the same name as the original file, but with a '.regular' extension added in the end.

I have added a sample list of about 2500 sentences as well as an example. The sample usage should be like:


## Usage
```
python process_list.py sample_sentences explicit_words
```


## Caveats
- Expect a lot of false positives, so use cautiously. Example, "Classy party" would be considered a dirty sentence because of the word "ass" in it
- It does not understand context. "Sex education" might be fairly innocent and a purely intended in an academic way, would trigger off the dirty classifier. 
- Corpus is small. I created a lot of the corpus by hand. See the comment in the code to uncomment the frequency analysis printing part to get an idea of which words are getting by.


## TODO
- To fix the problem with the word 'classy' as I described above. Detect on the basis of punctuation (' ', ',', '-', etc.)
- It will be nice to train a model where co-occurences of words in a string can be used to signal if a particular sentence might be dirty. The return value will be a value in the range [0, 1] instead of a boolean.
- Connect with Google Translate to instantly get translations 
