
# 🛡️ Keylogger Cybersecurity Project 

A simple yet effective **Python-based keylogger** developed during a cybersecurity internship to demonstrate keystroke capturing, log storage, and basic detection mechanisms.

>  **Disclaimer:** This project is strictly for **educational and ethical purposes only**. Do **not** use this tool on systems without proper authorization.


##  Project Structure

Keylogger_Cybersecurity_Project
│
├── **keylogger.py**   >   *Main keylogging script*
├── **detect\_keylogger.py**  >   *Detection script to flag if keystrokes are logged*
├── keystrokes.txt          # Text file storing captured keystrokes (for demo/framework) #
└── README.md               * Project documentation you are viewing now*


##  Features

-  Captures keystrokes in real time using Python’s `pynput` library  
-  Saves key logs in `keystrokes.txt`  
-  Runs silently in the background  
-  Includes a detection mechanism (`detect_keylogger.py`) to alert for existing logs  
-  Lightweight and beginner-friendly for learning cybersecurity fundamentals


##  How to Use

1. Ensure Python 3.x is installed on your system:
   *python --version*

2. Install the required Python package:
   *pip install pynput*

3. Run the keylogger:
  * python keylogger.py*

4. View the logs:
   *keystrokes.txt*

5. To check if logging has been performed, run:
   *python detect_keylogger.py*

## Author

**Sudeep Kumar Sah**
GitHub: [sudeep-sah](https://github.com/sudeep-sah)
LinkedIn: https://www.linkedin.com/in/sudeep-kumar-sah


*If you found this project useful or would like to collaborate, feel free to star ⭐ the repo or reach out!*
