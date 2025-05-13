import sys
import json
import os
import serial.tools.list_ports
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow  # Import the generated UI class

global default_data
global check_data
global com_data

default_data={
    "RF": "955383335353511191C1",
    "AI": "",
    "Vacuum": ""
}

check_data={
    "RF": "",
    "AI": "",
    "Vacuum": ""
}
com_data={}

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Apply the UI to this main window
        self.ui.pushButton.clicked.connect(self.find_btn_clicked)  # Connect the button click to a method
    
    def find_btn_clicked(self):
        # This function will be called when the button is clicked
        self.check_json()
        self.get_com_ports()
        self.find_device()
        print("Button clicked!")
    

    def check_json(self):
        # Check if the JSON file exists
        app_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(app_directory, "data.json")

        if os.path.exists(file_path):
            # If the file exists, read its content
            with open(file_path, "r") as file:
                data = json.load(file)
                check_data.update(data)  # Update check_data with the content of the JSON file
                print(data)
        else:
            # If the file does not exist, create it with default data
            with open(file_path, "w") as file:
                json.dump(default_data, file)
                print("Created new JSON file with default data.")
                check_data.update(default_data) # Update check_data with default data
        print(check_data)

    def get_com_ports(self):
        # Get the list of available COM ports and its Serial number
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print(f"Device     : {port.device}")
            print(f"Serial No. : {port.serial_number}")
            com_data.update({port.serial_number: port.device})

    def find_device(self):
        # This function will be called to find the device
        if check_data["RF"] in com_data:
            print(f"Device found: {check_data['RF']} on {com_data[check_data['RF']]}")
        else:
            print("Device not found.")
        if check_data["AI"] in com_data:
            print(f"Device found: {check_data['AI']} on {com_data[check_data['AI']]}")
        else:
            print("Device not found.")
        if check_data["Vacuum"] in com_data:
            print(f"Device found: {check_data['Vacuum']} on {com_data[check_data['Vacuum']]}")
        else:
            print("Device not found.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
