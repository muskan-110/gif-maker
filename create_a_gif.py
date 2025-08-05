import imageio as iio
import os

output=[]
for file in sorted(os.listdir('images')):
    if file.endswith('.png'):
        output.append(iio.imread(os.path.join('images',file)))
iio.mimsave('output_gif.gif',output,duration=500,loop=0)