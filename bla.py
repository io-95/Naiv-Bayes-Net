import os

folder_path1 = '20_newsgroups/Test/neg'
output_file = 'list.txt'

folder_path2 = '20_newsgroups/Test/pos'


with open(output_file, 'w') as f:
    for filename in os.listdir(folder_path1):
        # Entferne die Dateiendung und füge die Zahl 1 hinzu
        file_id = os.path.splitext(filename)[0]
        file_id += ' 0\n'
        # Schreibe den Dateinamen in die Datei
        f.write(file_id)

    for filename in os.listdir(folder_path2):
        # Entferne die Dateiendung und füge die Zahl 1 hinzu
        file_id = os.path.splitext(filename)[0]
        file_id += ' 1\n'
        # Schreibe den Dateinamen in die Datei
        f.write(file_id)
