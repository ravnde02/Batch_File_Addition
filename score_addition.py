import glob
import csv
import os

# Change the directory if needed
#os.chdir()

# Change to the extension of the files you want to change
current_file_names = sorted(glob.glob('*.tiff'))

# Change to the name of file containing the new file names
with open('Scores.csv', 'r') as f:
    reader = csv.reader(f)
    scores = list(reader)

current_name = []
ext = []
for file in current_file_names:
    name, ext = os.path.splitext(file)
    current_name.append(name)

addition = []
for i in scores:
    addition.append(i)

new_names = zip(current_name, addition)

new_names_final = []
for i in new_names:
    new_names_final.append('{}{}{}{}'.format(i[0],"_",i[1],ext))

# Join the current file names and the new file names into one list
names_list = zip(current_file_names, new_names_final)
for i in new_names_final:
    print(i)

# Rename the files
for i in names_list:
    os.rename(i[0], str(i[1]).replace("['", '').replace("']", ''))
