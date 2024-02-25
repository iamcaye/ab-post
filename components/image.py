from PIL import Image
import customtkinter


class ImageComponent(customtkinter.CTkLabel):
    def __init__(self, app: customtkinter.CTk, filename: str) -> None:
        self.filename = filename
        img = Image.open(filename)
        image = customtkinter.CTkImage(img, size=(img.width, img.height))
        super().__init__(master=None, image=image, text='')
