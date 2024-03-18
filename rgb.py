import spectral
import scipy.io as sio

# Load the image
name = 'KSC'
n = 'KSC'
print(sio.loadmat(name+'.mat'))
img = sio.loadmat(name+'.mat')[n]

#save rgb
spectral.save_rgb(name+'.png', img, [29, 19, 9])