from PIL import Image
import customtkinter


class ImageComponent(customtkinter.CTkLabel):
    def __init__(self, app: customtkinter.CTk, filename: str = '', raw_img: Image = None) -> None:
        self.filename = filename
        if raw_img is None:
            img = Image.open(raw_img)
        else:
            img = raw_img

        image = customtkinter.CTkImage(img, size=(img.width//2, img.height//2))
        super().__init__(master=None, image=image, text='')
