from PIL import Image
import os

directory = 'Google_Recaptcha_V2_Images_Dataset/images/Chimney'

def convtogrey(directory,filename):
    fn = os.path.join(directory, filename)
    img = Image.open('test.jpg')
    imgGray = img.convert('L')
    imgGray.save('test_gray.jpg')


for filename in os.listdir(directory):
    if os.path.isfile(directory,filename):
        convtogrey(directory,filename)

