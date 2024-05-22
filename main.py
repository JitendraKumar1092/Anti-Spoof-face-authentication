import os
import datetime
import pickle
import sys
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition
import util

# Clone the Silent-Face-Anti-Spoofing-master repo into the project or wherever you want and add the path to the system so we can easily import the test files
sys.path.append('Silent-Face-Anti-Spoofing-master')
from my_test import test

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")
        self.setup_ui()
        self.setup_db_and_logging()
        self.add_webcam(self.webcam_label)

    def setup_ui(self):
        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)
        self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)
        self.logout_button_main_window.place(x=750, y=300)
        self.register_new_user_button_main_window = util.get_button(
            self.main_window, 'register new user', 'gray', self.register_new_user, fg='black'
        )
        self.register_new_user_button_main_window.place(x=750, y=400)
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

    def setup_db_and_logging(self):
        self.db_dir = './db'
        os.makedirs(self.db_dir, exist_ok=True)
        self.log_path = './log.csv'

    def add_webcam(self, label):
        self.cap = cv2.VideoCapture(0)
        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        if ret:
            self.most_recent_capture_arr = frame
            img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
            self.most_recent_capture_pil = Image.fromarray(img_)
            imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
            self._label.imgtk = imgtk
            self._label.configure(image=imgtk)
        self._label.after(20, self.process_webcam)

    def login(self):
        self.handle_authentication('in')

    def logout(self):
        self.handle_authentication('out')

    def handle_authentication(self, action):
        label = test(
            image=self.most_recent_capture_arr,
            model_dir='Silent-Face-Anti-Spoofing-master/resources/anti_spoof_models',
            device_id=0
        )
        if label == 1:
            name = util.recognize(self.most_recent_capture_arr, self.db_dir)
            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
            else:
                action_msg = 'Login successful!' if action == 'in' else 'Successfully logged out.'
                util.msg_box(action_msg, f'Welcome, {name}.' if action == 'in' else f'It was great to see you, {name}!')
                with open(self.log_path, 'a') as f:
                    f.write(f'{name},{datetime.datetime.now()},{action}\n')
        else:
            util.msg_box("Spoofing Alert!", "Don't try to be oversmart...")

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")
        self.setup_registration_ui()

    def setup_registration_ui(self):
        self.accept_button_register_new_user_window = util.get_button(
            self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user
        )
        self.accept_button_register_new_user_window.place(x=750, y=300)
        self.try_again_button_register_new_user_window = util.get_button(
            self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user
        )
        self.try_again_button_register_new_user_window.place(x=750, y=400)
        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)
        self.add_img_to_label(self.capture_label)
        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)
        self.text_label_register_new_user = util.get_text_label(
            self.register_new_user_window, 'Please, \ninput username:'
        )
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")
        embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]
        file_path = os.path.join(self.db_dir, f'{name}.pickle')
        with open(file_path, 'wb') as file:
            pickle.dump(embeddings, file)
        util.msg_box('Success!', 'User was registered successfully!')
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
