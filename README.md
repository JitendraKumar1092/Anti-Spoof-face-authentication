```markdown
# Face Recognition and Anti-Spoofing System

## Overview

This project is a facial recognition and anti-spoofing system built using Python, OpenCV, Tkinter, and the Silent-Face-Anti-Spoofing library. The application provides a graphical user interface for logging in, logging out, and registering new users through a webcam. It incorporates anti-spoofing measures to detect and prevent attempts to deceive the system with photos or videos of faces.

## Features

- **Real-time Webcam Integration**: Captures images from a webcam for face recognition and registration.
- **Face Recognition**: Identifies users based on their facial features.
- **Anti-Spoofing**: Detects and prevents spoofing attempts using the Silent-Face-Anti-Spoofing model.
- **User Registration**: Allows new users to register by capturing their facial data.
- **Logging**: Records login and logout times for registered users.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/face-recognition-anti-spoofing.git
   cd face-recognition-anti-spoofing
   ```

2. **Clone the Silent-Face-Anti-Spoofing repository**:
   ```sh
   git clone https://github.com/minivision-ai/Silent-Face-Anti-Spoofing.git Silent-Face-Anti-Spoofing-master
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
   windows and linux dependencies are of different versions so install accordingly

## Usage

1. **Run the application**:
   ```sh
   python main.py
   ```

2. **Main Window**:
   - **Login**: Press the 'login' button to authenticate.
   - **Logout**: Press the 'logout' button to log out.
   - **Register New User**: Press the 'register new user' button to add a new user to the database.

3. **Registration Window**:
   - **Input Username**: Enter the username in the text box.
   - **Accept**: Capture the face and save the user data.
   - **Try Again**: Retake the capture if the image is not satisfactory.

## Directory Structure

- `app.py`: Main application script.
- `Silent-Face-Anti-Spoofing-master/`: Cloned repository for the anti-spoofing model.
- `db/`: Directory to store registered user data.
- `log.csv`: File to log login and logout times.
- `util.py`: Utility functions for creating GUI elements and performing face recognition.

## Dependencies

- `tkinter`: For creating the graphical user interface.
- `opencv-python`: For capturing images from the webcam.
- `Pillow`: For handling image processing.
- `face_recognition`: For face detection and recognition.
- `pickle`: For saving and loading user data.
- `Silent-Face-Anti-Spoofing`: For anti-spoofing detection.

## Adding Silent-Face-Anti-Spoofing to System Path

Make sure to append the path of the cloned Silent-Face-Anti-Spoofing repository to the system path in `main.py`:
```python
import sys
sys.path.append('Silent-Face-Anti-Spoofing-master')
from my_test import test
```

## Acknowledgements

This project uses the Silent-Face-Anti-Spoofing model developed by [minivision-ai](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. For any questions, please contact [egr.jitendrayadav@gmail.com](mailto:egr.jitendrayadav@gmail.com) .
