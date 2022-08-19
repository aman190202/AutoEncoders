from PIL import Image
import os

directory = 'Google_Recaptcha_V2_Images_Dataset/images/Chimney'
directory_intended= 'Google_Recaptcha_V2_Images_Dataset/images/Chimney_grey'


def convtogrey(directory,filename):
    fn = os.path.join(directory, filename)
    img = Image.open(fn)
    imgGray = img.convert('L')
    filename= filename + 'grey'
    imgGray.save('test_gray.jpg')


for filename in os.listdir(directory):

    os.mkdir()
    if os.path.isfile(directory,filename):
        convtogrey(directory,filename)

