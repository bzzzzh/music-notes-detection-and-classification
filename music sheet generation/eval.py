import cv2
from PIL import Image
import pandas as pd

def image_resize(img, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the img to be resized and
    # grab the img size
    dim = None
    (h, w) = img.shape[:2]

    # if both the width and height are None, then return the
    # original img
    if width is None and height is None:
        return img

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the img
    resized = cv2.resize(img, dim, interpolation=inter)

    # return the resized image
    return resized

def main():
    for j in range(1, 101):
        filename = "dataset/pic/sheet_" + str(j) + ".png"

        # resize
        img = cv2.imread(filename)
        img = image_resize(img, height=1080)
        crop_img = img[0:128, 0:512]
        #print("cropped image size:", cropped_image.size)

        csv_name = "dataset/boundingbox/sheet_" + str(j) + ".csv"
        df = pd.read_csv(csv_name)
        for i in range(len(df.bottom_x)):
            # print(df.bottom_x[i])
            cv2.rectangle(crop_img, (int(df.bottom_x[i]), int(df.bottom_y[i])), (int(df.top_x[i]), int(df.top_y[i])), (60, 60, 60), 1)
        
        # Save the cropped image
        save_name = "dataset/eval/sheet_" + str(j) + ".png"
        cv2.imwrite(save_name, crop_img)


main()