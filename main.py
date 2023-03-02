import csv
import os

def main():
	array = []
	stream = os.popen('ls 20_newsgroups/Training/Ath >> buffer.txt')
	with open('buffer.txt', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter='\n')
		for row in reader:
			array.append([str(num) for num in row])

	string = []
	for i in range(len(array)):
		string.append('cat 20_newsgroups/Training/Ath/' 
		     			+ ''.join(array[i]) 
						+' | tr -d "[:punct:]" | tr -s "[:space:]" "\n" | sort | uniq -ci')
	
	dictionary = {}
	print(string[3])
	stream = os.popen(string[3]).read()
	output = stream.split('\n')

	for line in output:
		print(line)
		if line == '':
			break
		word1, word2 = line.split()
		dictionary[word2] = word1

	print(dictionary)

if __name__ == '__main__':
	main()
