import PIL.Image as Image
import matplotlib.pyplot as plt
import os

def load_images_from_folder(folder):
    images = []
    files = os.listdir(folder)
    files.sort(key=lambda x: int(x.split('.')[0]))
    files.reverse()
    for filename in files:
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

name = 'KSC'
n = 'KSC'

images = load_images_from_folder(name)
print(images[0].size)

original = Image.open(name+'.png')

scale = 0.8
leng = len(images) *scale
#plot all images in cube shape
for idx, img in enumerate(images):
    iid = idx + 1
    plt.imshow(img, extent=[leng-iid*scale, leng-iid*scale+img.size[0], leng-iid*scale, leng-iid*scale+img.size[1]])

plt.imshow(original, extent=[0, original.size[0], 0, original.size[1]])
plt.xlim(0, len(images)+images[0].size[0])
plt.ylim(0, len(images)+images[0].size[1])
plt.axis('off')
plt.show()

