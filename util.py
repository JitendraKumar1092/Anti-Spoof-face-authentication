import os
import pickle
import tkinter as tk
from tkinter import messagebox
import face_recognition

def get_button(window, text, color, command, fg='white'):
    return tk.Button(
        window, text=text, activebackground="black", activeforeground="white",
        fg=fg, bg=color, command=command, height=2, width=20, font=('Helvetica bold', 20)
    )

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label

def get_entry_text(window):
    return tk.Text(window, height=2, width=15, font=("Arial", 32))

def msg_box(title, description):
    messagebox.showinfo(title, description)

def recognize(img, db_path, tolerance=0.6):
    embeddings_unknown = face_recognition.face_encodings(img)
    if len(embeddings_unknown) == 0:
        return 'no_persons_found'
    embeddings_unknown = embeddings_unknown[0]
    db_dir = sorted(os.listdir(db_path))
    match = False
    for file_name in db_dir:
        with open(os.path.join(db_path, file_name), 'rb') as file:
            embeddings = pickle.load(file)
            match = face_recognition.compare_faces([embeddings], embeddings_unknown, tolerance=tolerance)[0]
            if match:
                return file_name[:-7]
    return 'unknown_person'
