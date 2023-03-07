from PIL import Image 
import os 
import PIL 
import glob
import shutil

path = './'
dir = os.listdir('out/')

index = 0

RANGE_MIN = 18
RANGE_MAX = 18

for item in dir:

    index = index + 1
    print("{:0>3}/{:0>3} {}".format(index, len(dir), item))

    if '.png' in item:
        for margin in range(RANGE_MIN, RANGE_MAX + 1):
            item_new = item[:-4:] + " __{:0>2}".format(str(margin)) + '.png'

            shutil.copyfile(path + 'out/' + item, path + 'out/out/' + item_new)

            image = Image.open(path + 'out/out/' + item_new)
            image = image.crop((margin, margin, 200 - margin, 200 - margin))
            image.save(path + 'out/out/' + item_new, quality=100, optimize=True)
    
    else:
        print('!!!!! skipped {} !!!!!'.format(item))

