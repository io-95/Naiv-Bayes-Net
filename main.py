import csv
import os

def main():
	filenames = []
	get_filename(filenames)

	commands = []
	creat_commands(commands, filenames)
	
	dictionary = {}
	save_words_in_dictionary(dictionary, commands)


def save_words_in_dictionary(dictionary, commands):
	for i in range(len(commands)):
		stream = os.popen(commands[i]).read()
		output = stream.split('\n')

		for line in output:
			if line == '':
				break
			word1, word2 = line.split()
			if word2 in dictionary:
				dictionary[word2] += int(word1)
			else:
				dictionary[word2] = int(word1)

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
