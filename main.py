import csv
import os

def main():
	filename = []
	get_filename(filename)

	string = []
	for i in range(len(filename)):
		string.append('cat 20_newsgroups/Training/Ath/' 
		     			+ ''.join(filename[i]) 
						+' | tr -d "[:punct:]" | tr -s "[:space:]" "\n" | sort | uniq -ci')
	
	dictionary = {}
	stream = os.popen(string[3]).read()
	output = stream.split('\n')

	for line in output:
		if line == '':
			break
		word1, word2 = line.split()
		dictionary[word2] = word1

	print(dictionary)

def get_filename(array):
	stream = os.popen('ls 20_newsgroups/Training/Ath >> buffer.txt')
	with open('buffer.txt', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter='\n')
		for row in reader:
			array.append([str(num) for num in row])

if __name__ == '__main__':
	main()
