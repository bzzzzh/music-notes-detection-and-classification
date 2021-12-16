import os

def main():
    for i in range(51, 101):
        filename = "dataset/pic/sheet_" + str(i) + ".png"
        command = "python3 openmsbb/src/sheet_to_bounding_box.py " + filename
        os.system(command)


main()