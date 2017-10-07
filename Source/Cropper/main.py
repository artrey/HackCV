from PIL import Image

for i in range(1,130):
    i=str(i)
    im = Image.open('Dataset/'+i+'.png')
    im.load()
    out = Image.new("RGB", im.size, (255, 255, 255))
    out.paste(im, mask=im.split()[3])
    box = (576, 0, 1376, 600)
    out2 = out.crop(box)
    out2.save("Result/"+i+".jpg", "JPEG", quality=100)
