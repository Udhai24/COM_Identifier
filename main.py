import sys
import json
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow  # Import the generated UI class

global default_data

default_data={
    "RF": "",
    "AI": "",
    "Vacuum": ""
}

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Apply the UI to this main window
        self.ui.pushButton.clicked.connect(self.find_btn_clicked)  # Connect the button click to a method
    
    def find_btn_clicked(self):
        # This function will be called when the button is clicked
        print("Button clicked!")

    def check_json(self):
        # Check if the JSON file exists
        app_directory = os.path.dirname(os.path.abspath(__file__))
        
        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                data = json.load(file)
                print(data)
        else:
            # If the file does not exist, create it with default data
            with open("data.json", "w") as file:
                json.dump(default_data, file)
                print("Created new JSON file with default data.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
