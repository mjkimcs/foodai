import os
from PIL import Image
folder='/home/tako/Chloe_test/kfood2/'
for i in os.listdir(folder):
    for j in os.listdir(folder+i):
        try:
            test=Image.open(folder+i+'/'+j)
            #if test.format=='GIF':  # crop_area.properties
            #    print(folder+i+'/'+j)
        except IOError:
        #print('test:', test)
        #if test.format.lower() not in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']:
            #print('test:', test)
            print(folder+i+'/'+j)
            os.remove(folder+i+'/'+j)
