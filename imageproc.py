"""An image processor."""
__author__ = "Parker Ostertag"
__date__ = "18 October 2017"

def pos(file_name):
    """Displays the positive version of the chosen picture."""
    import cImage
    img = cImage.Image(file_name)
    width = img.getWidth()
    height = img.getHeight()
    win = cImage.ImageWin(width, height)
    return img.draw(win)

def neg(file_name):
    """Displays the negative version of the chosen picture. The parameter is the file name."""
    import cImage

    img = cImage.Image(file_name)
    width = img.getWidth()
    height = img.getHeight()
    win = cImage.ImageWin(width, height)
    img.draw(win)

    for row in range(height):
        for col in range(width):
            p = img.getPixel(col,row)

            neg_red = 255 - p.getRed()
            neg_green = 255 - p.getGreen()
            neg_blue = 255 - p.getBlue()

            newpixel = cImage.Pixel(neg_red, neg_green, neg_blue)
            img.setPixel(col, row, newpixel)

    return img.draw(win)

def graysc(file_name):
    """Displays the gray scale version of the chosen picture. The parameter is the file name."""
    import cImage
    from myfunctions import median

    img = cImage.Image(file_name)
    width = img.getWidth()
    height = img.getHeight()
    win = cImage.ImageWin(width, height)
    img.draw(win)

    for row in range(height):
        for col in range(width):
            p = img.getPixel(col,row)

            new_red = median(p.getRed(), p.getGreen(), p.getBlue())
            new_green = median(p.getRed(), p.getGreen(), p.getBlue())
            new_blue = median(p.getRed(), p.getGreen(), p.getBlue())

            newpixel = cImage.Pixel(new_red, new_green, new_blue)
            img.setPixel(col, row, newpixel)

    return img.draw(win)

def hidden_message(file_name):
    """Displays the negative version of the chosen picture. The parameter is the file name."""
    import cImage

    img = cImage.Image(file_name)
    width = img.getWidth()
    height = img.getHeight()
    win = cImage.ImageWin(width, height)
    img.draw(win)

    for row in range(height):
        for col in range(width):
            p = img.getPixel(col,row)

            red_value = p.getRed()
            if red_value % 2 == 0:
                newpixel = cImage.Pixel(0, 0, 0)
                img.setPixel(col, row, newpixel)
            else:
                newpixel = cImage.Pixel(255, 255, 255)
                img.setPixel(col, row, newpixel)

            

    return img.draw(win)

               

def main():
    import cImage
    file_name = input("What is the name of the image file? ")
    question = input("Ex: positive, negative, gray scale, hidden, exit. ")
    if question == "positive" or question == "p":
        call = pos(file_name)
    elif question == "negative" or question == "n":
        call = neg(file_name)
    elif question == "gray scale" or question == "g":
        call = graysc(file_name)
    elif question == "hidden" or question == "h":
        call = hidden_message(file_name)
    if question != "exit" or question != "e":
        img = cImage.Image(file_name)
        win = cImage.ImageWin(img.getWidth(), img.getHeight())
        img.draw(win)
        win.exitonclick()
        
        
main()
