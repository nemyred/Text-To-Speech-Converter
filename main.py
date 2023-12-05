from tkinter import *
from customtkinter import *
from tkinter.filedialog import askopenfilename
import PyPDF2
import pdfplumber
import pyttsx3 as tts


window = CTk()
window.geometry("450x250")
window.title("Pdf to AudioFile Converter")
set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


def upload_file():
    file = askopenfilename()
    f = open(file, "rb")
    pdf_reader = PyPDF2.PdfReader(f)
    pages = pdf_reader.pages
    text = ""

    with pdfplumber.open(file) as pdf:
        for i in range(len(pages)):
            page = pdf.pages[i]
            text += page.extract_text()
            print(text)

    engine = tts.init()
    engine.setProperty("rate", 150)
    engine.save_to_file(text, "audio.mp3")
    engine.runAndWait()
    info_label = CTkLabel(window, text="DOWNLOADED", font=("Arial", 15))
    info_label.pack(pady=20)


title_label = CTkLabel(window, text="CHOOSE A PDF FILE", fg_color="white", width=40, corner_radius=20,
                       text_color="black", font=("Helveltica", 15))
title_label.pack(pady=10)

upload_file_button = CTkButton(window, text="Convert File", command=upload_file)
upload_file_button.pack()

window.mainloop()


