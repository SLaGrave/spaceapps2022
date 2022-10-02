def before(image):
    # Code to be run before filters goes here
    pix = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            old = pix[i, j]
            pix[i, j] = (int(old[0]*(j*1.5/image.size[1])), int(old[1]*(j*0.5/image.size[1])), int(old[2]*(j*1.5/image.size[1])))
    return image

def after(image):
    return image
