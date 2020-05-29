from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import glob
import os
from shutil import copyfile

#----------------------------------------------------------------------

class MainWindow():

    #----------------

    def __init__(self, main):

        # list of image
        self.folder = filedialog.askdirectory()
        self.files = glob.glob(f"{self.folder}/*.jpg")
        
        # canvas for image
        self.canvas = Canvas(main, width=1000, height=1200)
        self.canvas.grid(row=0, column=0)

        # images append to array
        self.my_images = []
        for img in self.files:
            self.my_images.append(img)
        self.my_image_number = 0

        # set first image on canvas
        self.my_images_pil = ImageTk.PhotoImage(Image.open(self.my_images[self.my_image_number]))
        self.image_on_canvas = self.canvas.create_image(95, 0, anchor = NW, image = self.my_images_pil)

        self.label = Label(main, text= f"Image Left: {str(len(self.my_images))}")
        self.label.place(x="0", y="3")

        # button to change image
        self.button = Button(main, text="Choix1", width="12", command=self.onButton)
        self.button.place(x="0", y="30")
        self.button = Button(main, text="Choix2", width="12", command=self.onButton)
        self.button.place(x="0", y="60")
        self.button = Button(main, text="Choix3", width="12", command=self.onButton)
        self.button.place(x="0", y="90")

    #----------------

    def onButton(self):

        # next image
        self.my_image_number += 1

        # return to first image
        if self.my_image_number >= len(self.my_images):
            messagebox.showinfo(title="TERMINER", message="Vous avez terminer!")
        else:
            # change image
            self.my_images_pil = ImageTk.PhotoImage(Image.open(self.my_images[self.my_image_number]))
            self.canvas.itemconfig(self.image_on_canvas, image = self.my_images_pil)
            self.label.configure(text = f"Image Left: {str(len(self.my_images)-self.my_image_number)}")

            self.copy_file = self.folder + "/_SPLIT/" + self.button2["text"] + "/" + os.path.basename(self.my_images[self.my_image_number])
            os.makedirs(os.path.dirname(self.copy_file), exist_ok=True)
            copyfile(self.my_images[self.my_image_number], self.copy_file)     
            print(self.button2["text"])

#----------------------------------------------------------------------

root = Tk()
MainWindow(root)
root.mainloop()