import PIL
from PIL import Image
from PIL import ImageEnhance
from IPython.display import display


### reading image
image = Image.open('readonly/msi_recruitment.gif')
image = image.convert('RGB')
#print(image)
#display(image)

### loading enhancer
enhancer = ImageEnhance.Brightness(image)
images = []

### making image variations of brightness 
for i in range(1, 10):
    images.append(enhancer.enhance(i/10))
#print(images)

### making the background
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width*3, first_image.height*3))
#print(first_image.size)

### generating and iterating dispatching images on the background
image_width = first_image.size[0]
image_height = first_image.size[1]

original_img = images[8]
new_imgs = []

    # Lets paste the current image into the contact sheet
    ### making new black slate
    #new_img = PIL.Image.new(img.mode, (img.width, img.height))
    
    ### converting RGB conditions depending on x, y row
for y_row_num in range(0, 3):
    for x_row_num in range(0, 3):
        r, g, b = original_img.split()
            
        if(y_row_num == 0):
            changed_point = r
        elif(y_row_num == 1):
            changed_point = g
        elif(y_row_num == 2):
            changed_point = b
                
        if(x_row_num == 0):
            changed_point = changed_point.point(lambda x: x*0.1)
        elif(x_row_num == 1):
            changed_point = changed_point.point(lambda x: x*0.5)
        elif(x_row_num == 2):
            changed_point = changed_point.point(lambda x: x*0.9)
                
        if(y_row_num == 0):
            r = changed_point
        elif(y_row_num == 1):
            g = changed_point
        elif(y_row_num == 2):
            b = changed_point
                
        new_img = Image.merge('RGB', (r, g, b))
        new_imgs.append(new_img)
            
#print(new_imgs)            

x = 0
y = 0
for img in new_imgs:    
    ### first, copy the each image on the background sheet
    contact_sheet.paste(img, (x, y))
    
    ### and then, update the location of next image
    if x+image_width == contact_sheet.size[0]:
        x = 0
        y += image_height
    else:
        x += image_width
        
### Let's adjust the whole image's size
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
display(contact_sheet)

