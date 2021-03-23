# tatoeba_tinysegmenter

This uses the Tatoeba Japanese corpus and the Python port of Tinysegmenter to create a tokenizer list of Japanese sentences in JSON.
Input: CSV file with a column of Japanese sentences.  The first (header) row should be 'sentence.'
Output: JSON object with key 'sentences', which contains an array of arrays.  Each array contains the tokens of a sentence.

Python port courtesy of Masato Hagiwara; Original Tinysegmenter courtesy of Taku Kudo.
https://pypi.org/project/tinysegmenter/
http://tinysegmenter.tuxfamily.org/

Directions:

1. Download csv file of the Tatoeba Japanese corpus: https://tatoeba.org/eng/downloads 
2. Add a first (header) row and enter 'sentence' in the topmost cell.
3. Install Tinysegmenter: (in terminal) pip install tinysegmenter
4. Retrieve a sample sentence: 
with open('sentences_jp_tokenized.json') as f:
        data = json.load(f)
        print(data['sentences'][0])
