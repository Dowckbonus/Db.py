import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook


class Dicton(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('英汉小词典')
        self.geometry("500x300")

        self.notebook = Notebook(self)

        english_tab = tk.Frame(self.notebook)
        chinese_tab = tk.Frame(self.notebook)

        self.translate_button = tk.Button(english_tab, text='点击翻译', command=self.translate)
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.english_entry = tk.Text(english_tab, bg='white', fg='black')
        self.english_entry.pack(side=tk.TOP, expand=1)

        self.chinese_translation = tk.StringVar(chinese_tab)
        self.chinese_translation.set('')

        self.chinese_label = tk.Label(chinese_tab, textvar=self.chinese_translation, bg='lightgrey', fg='black')
        self.chinese_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(english_tab, text='英文')
        self.notebook.add(chinese_tab, text='中文')

        self.notebook.pack(fill=tk.BOTH, expand=1)

    def translate(self, text=None):
        filename = '英语词典.txt'
        trans = dict()

        if not text:
            text = self.english_entry.get(1.0, tk.END).rstrip()

        with open(filename, 'r') as data:
            lines = data.readlines()
            for line in lines:
                edict = line.split('$')
                word = edict[0].rstrip()
                meaning = edict[1].rstrip()
                trans[word] = meaning

        try:
            self.chinese_translation.set(trans[text])
            msg.showinfo('翻译成功', trans[text])
        except Exception as e:
            msg.showerror("翻译错误", str(e))


if __name__ == '__main__':
    dicton = Dicton()
    dicton.mainloop()

