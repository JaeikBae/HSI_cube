import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

name = 'KSC'
n = 'KSC'
imgs = sio.loadmat(name+'.mat')[n]
#save

x,y,z = imgs.shape
print(np.max(imgs))
print(np.average(imgs))
for i in range(z):
    plt.imsave(name+'/'+str(i)+'.png',imgs[:,:,i], cmap='jet',vmax=500)