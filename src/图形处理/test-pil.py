from PIL import Image
im_gif = Image.open("F:/python/1.gif")
print(im_gif.mode)
im_gif.show()    ##第0帧
im_gif.seek(3)
im_gif.show()
im_gif.seek(9)
im_gif.show()