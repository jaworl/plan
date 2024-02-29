# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# image_path = "C:/Users/ASUS/Desktop/Untitled.png"
# img = Image.open(image_path).convert("L")
# img_array = np.array(img)
# print(img_array[295][826])
# plt.imshow(img_array, cmap="gray")
# plt.show()
# img_array = np.array(img)

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = "C:/Users/ASUS/Desktop/Untitled.png"
img = Image.open(image_path)
img_array = np.array(img)

# Displaying the pixel value at position [295][826] for each channel
print("Red:", img_array[367][851][0])
print("Green:", img_array[367][851][1])
print("Blue:", img_array[367][851][2])

# Display the image with three color channels
plt.imshow(img_array)
plt.show()