from distutils.command.build_scripts import first_line_re
import os

# chamge em
from_here = 'C:/Users/tobia/git-projects/tft-bot/src/augmentsList.txt'
to_there = 'C:/Users/tobia/git-projects/tft-bot/src/augmentsListShort.txt'
rows_between_words = 5
start_row = -1

def readTXT():
    file_name = os.path.join(os.path.dirname(__file__), from_here)
    file_name2 = os.path.join(os.path.dirname(__file__), to_there)
    with open(file_name, 'r') as fr:
        lines = fr.readlines()
        pointer = start_row
        augment_counter = 1
        with open(file_name2, 'w') as fw:
            for line in lines:
                if((pointer) %  rows_between_words == 0):
                    len_line = len(line) - 1
                    preAdaptionLine = line.replace("\n", "")
                    firstAdaptionLine = preAdaptionLine.replace("'", "")
                    secondAdaptionLine = firstAdaptionLine.replace("!", "")
                    newLine = secondAdaptionLine.replace(" ", "")
                    augment_name = newLine[0:len_line]
                    fw.write('"')
                    fw.write(augment_name)
                    fw.write('"')
                    fw.write(", ")
                if(augment_counter % (7 * rows_between_words) == 0):
                    fw.write("\n")
                pointer += 1
                augment_counter += 1
    print("finished")
