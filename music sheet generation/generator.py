import os
import random
import csv
from shutil import copyfile

def generate_music(i, filename):
    #filename = "dataset/sheet_" + str(i) + ".ly"
    print("filename:", filename)
    fr = open(filename, "r")
    list_of_lines = fr.readlines()

    # generate random music notes
    music = []
    music.append("a'4")
    
    for i in range(1, 7):
        note = ""
        note += random.choice(['c', 'd', 'e', 'f', 'g', 'a', 'b'])
        
        #print("music[",i-1, "]", music[i - 1])
        if music[i - 1][1:] == '8' or music[i-1][1:] == '16':
            #print("here")
            note += random.choice(['2', '4'])
        else:
            note += random.choice(['1', '2', '4', '8', '16'])
    
        #print("note:",note)
        music.append(note)

    fields = ['top_x', 'top_y', 'bottom_x', 'bottom_y', 'pitch','note']
    rows = []
    for i in range(7):
        if i == 0:
            rows.append(["","","","", music[i][0], music[i][2:]])
        else:
            rows.append(["","","","", music[i][0], music[i][1:]])
    
    csv_name = "dataset/boundingbox/" + filename[8:-3] + ".csv"
    with open(csv_name, 'w+') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)

    sheet = ""
    for i in range(len(music)):
        sheet += music[i]
        sheet += " "

    sheet += "\n"

    print("music generated:", sheet)
    list_of_lines[28] = sheet
    print()

    fw = open(filename, "w")
    fw.writelines(list_of_lines)
    fw.close()

    command = "./LilyPond.app/Contents/Resources/bin/lilypond --png "
    command += filename
    os.system(command)
    #os.system("pdftoppm -png test.pdf test")
    
    # img = Image.open("test.png")
    # img = img.resize((4250, 5500), Image.ANTIALIAS)
    # # im1 = img.crop((0, 0, img.size[0], img.size[1]//4))
    # img.save("test.png")

def main():
    for i in range(51, 101):
        filename = "dataset/sheet_" + str(i) + ".ly"
        copyfile("dataset/sheet_0.ly", filename)
        generate_music(i, filename)

main()