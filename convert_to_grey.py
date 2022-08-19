from PIL import Image
import os

directory = 'Google_Recaptcha_V2_Images_Dataset/images/Chimney'
directory_intended= 'Google_Recaptcha_V2_Images_Dataset/images/Chimney_grey'
os.mkdir(directory_intended)

def convtogrey(directory,filename):
    fn = os.path.join(directory, filename)
    img = Image.open(fn)
    imgGray = img.convert('L')
    filename= os.path.join(directory_intended,filename)
    imgGray.save(filename)


for filename in os.listdir(directory):
    if filename == '.DS_Store' :
        continue
    convtogrey(directory,filename)

