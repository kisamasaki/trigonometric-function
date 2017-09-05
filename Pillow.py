from PIL import Image
aoba_im=Image.open('aoba.jpg')
face_im=aoba_im.crop((240,25,420,210))
aoba_im_width,aoba_im_height=aoba_im.size
face_im_width,face_im_height=face_im.size
aoba_copy_two=aoba_im.copy()
for left in range(0,aoba_im_width,face_im_width):
    for top in range(0,aoba_im_height,face_im_height):
        print(left,top)
        aoba_copy_two.paste(face_im,(left,top))