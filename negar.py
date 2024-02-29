from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "C:/Users/ASUS/Desktop/Untitled.png"
img = Image.open(image_path).convert("L")
img_array = np.array(img)
print(img_array[295][826])
plt.imshow(img_array, cmap="gray")
plt.show()
img_array = np.array(img)
