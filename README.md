# tatoeba_tinysegmenter

A small experiment using both Mecab and Tinysegmenter to create a tokenized list of Japanese sentences in JSON, taken from the Tatoeba corpus.  It seems Mecab is much more accurate with tokenization.

Input: CSV file with a column of Japanese sentences.  The first (header) row should be 'sentence.'

Output: JSON object with key 'sentences', which contains an array of arrays.  Each array contains the tokens of a sentence.



Setup:

1. Download csv file of the Tatoeba Japanese corpus: https://tatoeba.org/eng/downloads 
2. Add a first (header) row and enter 'sentence' in the topmost cell.
3. Install Tinysegmenter: pip install tinysegmenter
4. Install Mecab: pip install mecab-python3  (see Windows directions here: https://github.com/SamuraiT/mecab-python3)
        
----------------------------------------------------------------------------------------

Python port of Tinysegmenter courtesy of Masato Hagiwara; Original Tinysegmenter courtesy of Taku Kudo.
https://pypi.org/project/tinysegmenter/
http://tinysegmenter.tuxfamily.org/

Mecab official documentation (Japanese): https://taku910.github.io/mecab/

Tatoeba corpus licensed under CC BY 2.0 FR.
https://creativecommons.org/licenses/by/2.0/fr/
https://tatoeba.org/eng/downloads
