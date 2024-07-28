import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import dlib
import threading
import os
from datetime import datetime
from imutils import face_utils
from face_utils import blinked, get_face_descriptor, is_new_face
from alert import alert, stop_alert
from logger import log_drowsiness

# Function to start video capture
def start_video_capture():
    global cap, known_face_descriptors, drowsy, active, status, color, alert_thread, person_index

    name = name_entry.get()
    car_number = car_number_entry.get()

    if not name or not car_number or name == "Enter Name" or car_number == "Enter Vehicle Number":
        messagebox.showwarning("Input Error", "Please fill in both Name and Vehicle Number before starting.")
        return

    app.destroy()  # Destroy the UI window

    import pygame
    pygame.mixer.init()

    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('D:/Zeeshan/project1/eyess/shape_predictor_68_face_landmarks.dat')
    face_rec_model = dlib.face_recognition_model_v1('D:/Zeeshan/project1/eyess/dlib_face_recognition_resnet_model_v1.dat')

    drowsy = 0
    active = 0
    status = ""
    color = (0, 0, 0)
    alert_thread = None
    known_face_descriptors = []
    person_index = 1

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            left_blink = blinked(landmarks[36], landmarks[37], 
                                 landmarks[38], landmarks[41], landmarks[40], landmarks[39])
            right_blink = blinked(landmarks[42], landmarks[43], 
                                  landmarks[44], landmarks[47], landmarks[46], landmarks[45])

            cv2.putText(frame, f'Person {person_index}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            person_index += 1

            if left_blink == 0 or right_blink == 0:
                drowsy += 1
                active = 0
                if drowsy > 6:
                    status = "Drowsy !"
                    color = (0, 0, 255)
                    if not alert_thread or not alert_thread.is_alive():
                        alert_thread = threading.Thread(target=alert)
                        alert_thread.start()

                    face_descriptor = get_face_descriptor(frame, face, predictor, face_rec_model)
                    if is_new_face(face_descriptor, known_face_descriptors):
                        if not os.path.exists('drowsy_images'):
                            os.makedirs('drowsy_images')
                        image_path = f'drowsy_images/drowsy_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
                        cv2.imwrite(image_path, frame)
                        location = "28.7041 N, 77.1025 E"
                        log_drowsiness(image_path, location, name, car_number)
                        known_face_descriptors.append(face_descriptor)
            else:
                drowsy = 0
                active += 1
                if active > 6:
                    status = "Active :)"
                    color = (0, 255, 0)
                    stop_alert()

            cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

            for n in range(0, 68):
                (x, y) = landmarks[n]
                cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

        person_index = 1

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.quit()

    with open('drowsiness_log.html', mode='a') as file:
        file.write('</table></body></html>')

# Initialize the customtkinter app
app = ctk.CTk()
app.title("Drowsiness Detection Setup")

# Set window size
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
app.geometry(f"{window_width}x{window_height}")

# Load background image
bg_image_path = "D:/Zeeshan/project1/project01/drives.jpg"

try:
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((window_width, window_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
except Exception as e:
    print(f"Error loading image: {e}")
    bg_photo = None

# Background label
background_label = tk.Label(app, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the form with transparent background
form_frame = ctk.CTkFrame(app, fg_color='transparent', corner_radius=15)
form_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label
title_label = ctk.CTkLabel(form_frame, text="Drowsiness Detection System", font=("Helvetica", 26, "bold"), text_color="white")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Name input
name_label = ctk.CTkLabel(form_frame, text="Name:", font=("Helvetica", 20, "bold"), text_color="white")
name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
name_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Name", font=("Helvetica", 20))
name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

# Vehicle number input
car_number_label = ctk.CTkLabel(form_frame, text="Vehicle Number:", font=("Helvetica", 20, "bold"), text_color="white")
car_number_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
car_number_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Vehicle Number", font=("Helvetica", 20))
car_number_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

# Start button
def on_enter(event):
    start_button.configure(fg_color='#333333', text_color='white')

def on_leave(event):
    start_button.configure(fg_color='#555555', text_color='white')

start_button = ctk.CTkButton(form_frame, text="Start", font=("Helvetica", 30, "bold"), text_color="white", bg_color="#555555", command=start_video_capture, corner_radius=10)
start_button.grid(row=3, column=0, columnspan=2, pady=20)
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# Run the app
app.mainloop()
