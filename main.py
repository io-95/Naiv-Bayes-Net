import csv
import os
import math

foldernames = ("Training", "Test")
files = ("buffer1.txt", "buffer2.txt", "list.txt", "list2.txt")

def main():
    word_dictionary = {}
    a_priory_probability = []
    initialisation(word_dictionary, a_priory_probability)

    testing_phase(word_dictionary, a_priory_probability)


def initialisation(word_dictionary, a_priory_probability):
    filenames = []
    get_filename(filenames, foldernames[0], files[0])

    commands = []
    creat_commands(commands, filenames, foldernames[0])

    save_words_in_dictionary(word_dictionary, commands)

    # list of filenames of the positive and negative test files
    pos_neg_dictionary = {}
    save_status_in_dictionary(pos_neg_dictionary, files[3])

    calc_probability(word_dictionary, pos_neg_dictionary, a_priory_probability)


def testing_phase(word_dictionary, a_priory_probability):
    filenames_of_test = []
    get_filename(filenames_of_test, foldernames[1], files[1])

    commands_of_test = []
    creat_commands(commands_of_test, filenames_of_test, foldernames[1])

    comparison_dictionary = {}
    save_status_in_dictionary(comparison_dictionary, files[3])

    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(comparison_dictionary)):
        testfile_words = {}
        get_words(testfile_words, commands_of_test[i])
        classification = test_bayesnet(testfile_words, word_dictionary, a_priory_probability)

        if classification == 1 and comparison_dictionary[filenames_of_test[i][0]] == 1:
            tp += 1
        if classification == 0 and comparison_dictionary[filenames_of_test[i][0]] == 0:
            tn += 1
        if classification == 1 and comparison_dictionary[filenames_of_test[i][0]] == 0:
            fp += 1
        if classification == 0 and comparison_dictionary[filenames_of_test[i][0]] == 1:
            fn += 1

    print("truepositive: %d; truenegative: %d; falsepositive: %d; falsenegative: %d" %(tp, tn, fp, fn))

def get_filename(array, folder, file):
    stream = os.popen('ls 20_newsgroups/'+folder+'/ >'+ file)
    with open(file, "r+", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        for row in reader:
            array.append([str(num) for num in row])

    print("[info]: got filenames")


def creat_commands(commands, filenames, folder):
    for i in range(len(filenames)):
        commands.append('cat 20_newsgroups/'
                        + folder
                        +'/'
                        + ''.join(filenames[i])
                        + ' | tr -d "[:punct:]" | tr -s "[:space:]" "\n" | sort | uniq -ci')

    print("[info]: created commands")


def save_words_in_dictionary(dictionary, commands):
    for i in range(len(commands)):
        get_words(dictionary, commands[i])

        if i % 75 == 0:
            percent = 0
            percent = 100 * i / len(commands)
            print("[info]: {:.2f}% complieted saving words in dictionary".format(percent))

    print("[info]: saved words in dictionary")

def get_words(dictionary, command):
    stream = os.popen(command).read()
    output = stream.split('\n')
    for line in output:
        # if last line reached break out of loop
        if line == '':
            break
        word1, word2 = line.split()
        if word2 in dictionary:
            dictionary[word2][0] += int(word1)
        else:
            dictionary[word2] = []
            dictionary[word2].append(int(word1))


def save_status_in_dictionary(dictionary, file):
    with open(file, "r", newline='') as f:
        for row in f:
            word1, word2 = row.split()
            dictionary[word1] = int(word2)

    print("[info]: saved status in a dictionary")


def calc_probability(dictionary, pos_neg_dictionary, a_priory_probability):
    total_amount_of_words = 0
    for value in dictionary.values():
        total_amount_of_words += value[0]

    for key, value in dictionary.items():
        probability = 0
        probability = dictionary[key][0] / total_amount_of_words
        probability = math.log10(probability)
        dictionary[key].append(probability)

    positive = 0
    negative = 0
    for item in pos_neg_dictionary.items():
        if item[1] == 1:
            positive += 1
        elif item[1] == 0:
            negative += 1

    a_priory_probability.append(math.log10(positive / (positive + negative)))

    print("[info]: calculated all probabilities")


def test_bayesnet(test_words, dictionary, a_priory_probability):
    sum = 0
    for key, value in test_words.items():
        probability = 0
        if key in dictionary:
            probability = dictionary[key][1] * value[0]
            sum += probability
    p_i_n = sum * a_priory_probability[0]
    #print("{:.2f}".format(p_i_n))
    if p_i_n >= 300:
        return 0
    else:
        return 1


if __name__ == '__main__':
    main()
