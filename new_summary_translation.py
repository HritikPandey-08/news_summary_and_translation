from newspaper import Article
from googletrans import Translator
import tkinter as tk
from tkinter import *
import tkinter.messagebox

#GUI Window
top = tk.Tk()
top.update()
top.geometry('680x500')
top.title('News Article Summary') # Title for Window
 

# Label for Top
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))
art_label = ('arial', 16, 'bold')
art_cont = ('verdana',13)

# Variables used for both the function
article = ''
art_title = ''
article_sum = ''
art_content= ''

#canvas and frame 
my_canvas = Canvas(top,borderwidth=0, background="#ffffff")
frame = Frame(my_canvas, background="#ffffff")
frame.pack(fill=BOTH,expand=TRUE)
vsb = Scrollbar(top, orient="vertical", command=my_canvas.yview) 
my_canvas.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
my_canvas.pack(side="right",fill="both", expand=True)
my_canvas.create_window((0,0), window=frame,anchor="nw")
my_canvas.pack(fill="both", expand=True)

# scrollbar 
def onFrameConfigure(canvas):
     '''Reset the scroll region to encompass the inner frame'''
     canvas.configure(scrollregion=canvas.bbox("all"))
frame.bind("<Configure>", lambda event, canvas=my_canvas:onFrameConfigure(my_canvas))


# Translating and summary function

def translate_news():

    global article
    global art_title
    global article_sum
    global art_content

    # Article 
    article = Article(news_url.get())
    article.download()
    article.parse()
    article.nlp()

    # Translating Article
    translator = Translator()
    art_title = translator.translate(article.title, dest=btn2.get())
    article_sum = translator.translate(article.summary, dest=btn2.get())
    art_content = translator.translate(article.text, dest=btn2.get())

    # Printing title
    title_label = Label(frame, text="Article Title:", font=art_label)
    title_label.pack(pady=3)

    article_title = Text(frame,height=2,width=65,wrap='word', font=art_cont,borderwidth=2)
    article_title.insert('end',art_title.text)
    article_title.config(state="disabled")
    article_title.pack(pady=1)

    # Printing Summary
    summary_label = Label(frame, text="Article Summary:", font=art_label)
    summary_label.pack(pady=3)

    text_box = Text(frame,height=8,width=50,wrap='word',font=art_cont)
    text_box.insert('end', article_sum.text)
    text_box.pack(fill=BOTH,expand=True)

    # Printing Publisher Date
    publish_label = Label(frame, text="Article Publish Date:", font=art_label)
    publish_label.pack(pady=3)

    article_publish = Text(frame, height=1,width=50, font=art_cont,borderwidth=2)
    article_publish.insert('end',article.publish_date)
    article_publish.config(state="disabled")
    article_publish.pack(pady=1)

    # Printing Image top link
    link_label = Label(frame, text="Article Image link:", font=art_label)
    link_label.pack(pady=3)

    label_image = Text(frame, font=art_cont, height=2, width=65,borderwidth=2)
    label_image.insert('end', article.top_image)
    label_image.config(state="disabled")
    label_image.pack(pady=5)

# Downloading article Function
def download_article():
    file1 = open("News_summary_File.txt", "w+",encoding="utf-8")
    file1.write("Title:\n")
    file1.write(art_title.text)
    file1.write("\n\nArticle Text:\n")
    file1.write(art_content.text)
    file1.write("\n\nArticle Summary:\n")
    file1.write(article_sum.text)
    file1.write("\n\nArticle Publish Date:\n")
    file1.write(str(article.publish_date))
    file1.write("\n\nArticle Image link:\n")
    file1.write(article.top_image)
    file1.close()

# Url Entry field
Label(frame, text="URL", font=('arial', 18, 'bold')).pack()
news_url = Entry(frame, width=65,borderwidth=2,font=('verdana', 11),)
news_url.configure(highlightbackground="red", highlightcolor="red")
news_url.pack(pady=5)


# Language selection
my_label = Label(frame, text="Select Language in which you want to translate", font=art_label)
my_label.pack(pady=5)

# Radio font
font_radio = ('calibri', 13)
btn2 = StringVar(value="en")
Radiobutton(frame, text="English", value="en", variable=btn2,font=font_radio).pack(pady=5)
Radiobutton(frame, text="Hindi", value="hi", variable=btn2,font=font_radio).pack(pady=5)
Radiobutton(frame, text="Marathi", value="mr", variable=btn2,font=font_radio).pack(pady=5)


# validation 

def validate():
    url = news_url.get()
    if url=='':
        tk.messagebox.showinfo("Alert Message.",  "Please enter a url")
    else:
        translate_news()

# Translation and summarization button
translate_button = Button(frame, text="Translate and summarize",font=('verdana', 11,'bold'), command=validate).pack(pady=6)

def validate_download():
    url = news_url.get()
    if url=='':
        tk.messagebox.showinfo("Alert Message.",  "Please enter a url")
    elif article_sum == '':
        tk.messagebox.showinfo("Alert Message.",  "Please first summarize the news")
    else:
        download_article()
# Downloading article button
download_button = Button(frame, text="Download article",font=('verdana', 11,'bold') ,command=validate_download)
download_button.pack(pady=6)
top.mainloop()

 