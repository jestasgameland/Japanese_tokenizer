import csv
import json
import tinysegmenter

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	data['sentences'] = []
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8-sig') as csvf:
		csvReader = csv.DictReader(csvf)
		
		for row in csvReader:
			sen = tinysegmenter.tokenize(row['sentence'])
			data['sentences'].append(sen)

	# Open a json writer, and use the json.dumps() 
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		

# Call the make_json function
make_json('japanese_tatoeba1.csv', 'sentences_jp_tokenized.json')



# data['sentences'] will be an array of arrays
# each array is a set of the words (tokens) in a sentence
