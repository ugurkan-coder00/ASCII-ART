from PIL import Image

class Ascii:
    def main(self):
        a = input("PATH: ")
        img = Image.open(a)
        width,height = img.size
        aspecy_ratio = height/width

        new_width = 120
        new_height = aspecy_ratio * new_width
        img = img.resize((new_width,int(new_height)))
        img = img.convert("L")

        pixels = img.getdata()
        chars = ["B","S","#","&","@","$","%","*","!",":",",","."]

        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = "".join(new_pixels)
        new_pixels_count = len(new_pixels)

        ascii_image = [new_pixels[index:index+new_width] for index in range(0,new_pixels_count,new_width)]
        ascii_image = "\n".join(ascii_image)


        with open("ascii_image.txt","w") as f:
            f.write(ascii_image)
        print("başarılı.", a)

if __name__ == "__main__":
    photo = Ascii()
    photo.main()
