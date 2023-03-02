import csv
import os

def main():
	filenames = []
	get_filename(filenames)

	commands = []
	creat_commands(commands, filenames)
	
	dictionary = {}
	stream = os.popen(commands[3]).read()
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

def creat_commands(commands, filenames):
	for i in range(len(filenames)):
		commands.append('cat 20_newsgroups/Training/Ath/' 
		     			+ ''.join(filenames[i]) 
						+' | tr -d "[:punct:]" | tr -s "[:space:]" "\n" | sort | uniq -ci')
		

if __name__ == '__main__':
	main()
