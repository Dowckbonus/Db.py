import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Notebook
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from tkinter.filedialog import askopenfilename, askdirectory


class PicEdit(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('图片处理')
        self.geometry('800x500+100+50')

        # 固定窗口大小
        #self.resizable(False, False)
        #self.focusmodel()

        self.notebook = Notebook()

        # 选项卡
        image_tab = tk.Frame(self.notebook, bg='gray')
        self.image_label = tk.Label(image_tab)
        self.image_label.place(x=0, y=0, width=800, height=500)
        order_tab = tk.Frame(self.notebook)
        self.path = tk.StringVar()
        self.file_entry = tk.Entry(order_tab, state='readonly', text=self.path)
        self.file_entry.pack()

        # 功能按键
        self.load_button = tk.Button(order_tab, text='加载图像', command=self.load_image)
        self.load_button.pack(side=tk.TOP, fill=tk.X)
        # 打开的图片
        global edited_image

        self.rotate_button = tk.Button(order_tab,text='旋转图像', command=self.rotate_image)
        self.rotate_button.pack(side=tk.TOP, fill=tk.X)
        self.overturn_button = tk.Button(order_tab, text='水平翻转', command=self.overturn_image)
        self.overturn_button.pack(side=tk.TOP, fill=tk.X)
        self.dim_button = tk.Button(order_tab, text='模糊图像', command=self.dim_image)
        self.dim_button.pack(side=tk.TOP, fill=tk.X)
        self.enhance_button = tk.Button(order_tab, text='增强图像', command=self.enhance_image)
        self.enhance_button.pack(side=tk.TOP, fill=tk.X)
        self.saveas_button = tk.Button(order_tab, text='另存图像', command=self.saveas_image)
        self.saveas_button.pack(side=tk.TOP, fill=tk.X)

        self.notebook.add(image_tab, text='图片预览')
        self.notebook.add(order_tab, text='操作')

        self.notebook.pack(fill=tk.BOTH, expand=1)

    # 加载图片
    def load_image(self):
        path_ = askopenfilename(title='选择图片', filetypes=[('JPG', '*.jpg'), ('PNG', '*.png')])
        self.path.set(path_)
        self.img_open = Image.open(self.file_entry.get())

        thumb = self.img_open.resize((800, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(thumb)

        self.image_label.config(image=img)
        self.image_label.image = img

        global edited_image
        edited_image = self.img_open

        pass

    # 旋转图片（90度）
    def rotate_image(self):
        global edited_image
        img2 = edited_image
        nimg2 = img2.transpose(Image.ROTATE_180)

        thumb = nimg2.resize((800, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(thumb)

        self.image_label.config(image=img)
        self.image_label.image = img

        edited_image = nimg2

        pass

    # 翻转图片（水平）
    def overturn_image(self):
        global edited_image
        img3 = edited_image
        nimg3 = img3.transpose(Image.FLIP_LEFT_RIGHT)

        thumb = nimg3.resize((800, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(thumb)

        self.image_label.config(image=img)
        self.image_label.image = img

        edited_image = nimg3
        pass

    # 模糊图片
    def dim_image(self):
        global edited_image
        img4 = edited_image
        nimg4 = img4.filter(ImageFilter.BLUR)

        thumb = nimg4.resize((800, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(thumb)

        self.image_label.config(image=img)
        self.image_label.image = img

        edited_image = nimg4
        pass

    # 增强图片亮度（亮度1.5）
    def enhance_image(self):
        global edited_image
        img5 = edited_image
        enh_bri = ImageEnhance.Brightness(img5)
        brightness = 1.5
        nimg5 = enh_bri.enhance(brightness)

        thumb = nimg5.resize((800, 500), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(thumb)

        self.image_label.config(image=img)
        self.image_label.image = img

        edited_image = nimg5
        pass

    def saveas_image(self):
        global edited_image
        img6 = edited_image
        result = askdirectory()
        print(result)
        img6.save(result + r'/testimg.jpg')
        pass


if __name__ == '__main__':
    picedit = PicEdit()
    picedit.mainloop()




