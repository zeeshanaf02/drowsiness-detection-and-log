# Drowsiness Detection and Logging System

## Overview

This project implements a real-time drowsiness detection system designed to enhance road safety by monitoring drivers for signs of fatigue. Upon detecting drowsiness, the system:

- Issues an audible alert to the driver.
- Logs the incident with the driver's name, vehicle number, current location, and a captured image.
- Stores the log in an HTML file for easy access and review.

## Features

- **Real-Time Monitoring**: Utilizes a webcam to continuously monitor the driver's facial features.
- **User Input**: Collects the driver's name and vehicle number at the start of the session.
- **Drowsiness Detection**: Employs facial landmark detection to assess eye closure and determine drowsiness.
- **Alert Mechanism**: Plays an audible warning (`alert.wav`) when drowsiness is detected.
- **Incident Logging**: Captures the driver's image, records the current location, and logs the information in `drowsiness_log.html`.

## Technologies Used

- **Python**: Core programming language for the application.
- **OpenCV**: For image processing and webcam interfacing.
- **Dlib**: For facial landmark detection.
- **Geolocation APIs**: To fetch the current location of the driver.
- **HTML/CSS**: For structuring and styling the log file.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/zeeshanaf02/drowsiness-detection-and-log.git
cd drowsiness-detection-and-log
````

### 2. Set Up a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note**: Ensure that `requirements.txt` includes all necessary packages such as `opencv-python`, `dlib`, `imutils`, and any geolocation libraries used.

## Usage

### 1. Run the Application

```bash
python main.py
```

### 2. Provide User Details

* Enter the driver's **Name**.
* Enter the **Vehicle Number**.

### 3. Monitoring

* The system will start the webcam and begin monitoring for signs of drowsiness.
* If drowsiness is detected:

  * An audible alert will sound.
  * The system will capture the driver's image.
  * The current location will be fetched.
  * All information will be logged in `drowsiness_log.html`.

### 4. Review Logs

* Open `drowsiness_log.html` in a web browser to view all recorded incidents.

## Project Structure

```
drowsiness-detection-and-log/
├── __pycache__/                 # Compiled Python files
├── drowsy_images/               # Captured images of drowsy incidents
├── alert.py                     # Handles the alert mechanism
├── alert.wav                    # Audio file for alerts
├── back.jpg                     # Background image for the GUI
├── drives.jpg                   # Image used in the GUI
├── drowsiness_log.html          # HTML file logging all incidents
├── face_utils.py                # Utility functions for facial detection
├── logger.py                    # Handles logging of incidents
├── main.py                      # Main application script
├── styles.css                   # Stylesheet for the HTML log
└── requirements.txt             # List of dependencies
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

* Inspired by the need to enhance road safety through technology.
* Utilizes open-source libraries and tools to achieve its objectives.


