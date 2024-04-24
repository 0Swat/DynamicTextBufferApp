import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QTextEdit, QPushButton, QProgressBar, QLabel, QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
import time
import random
import string

class AddThread(QThread):
    new_char = pyqtSignal(str)

    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.running = True

    def run(self):
        while self.running:
            time.sleep(self.delay.value() / 1000.0)
            self.new_char.emit(random.choice(string.ascii_letters))

    def stop(self):
        self.running = False

class RemoveThread(QThread):
    remove_char = pyqtSignal()

    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.running = True

    def run(self):
        while self.running:
            time.sleep(self.delay.value() / 1000.0)
            self.remove_char.emit()
    def stop(self):
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.buffer = ""

    def initUI(self):
        self.setWindowTitle("Text Buffer Manager")
        main_layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.progress_bar = QProgressBar()
        self.start_button = QPushButton("Start")

        self.add_slider = QSlider(Qt.Horizontal)
        self.remove_slider = QSlider(Qt.Horizontal)
        self.add_speed_label = QLabel("Prędkość dodawania znaków: 500 ms")
        self.remove_speed_label = QLabel("Prędkość usuwania znaków: 500 ms")

        self.add_slider.setMinimum(1)
        self.add_slider.setMaximum(1000)
        self.add_slider.setValue(500)
        self.remove_slider.setMinimum(1)
        self.remove_slider.setMaximum(1000)
        self.remove_slider.setValue(500)

        self.add_slider.valueChanged.connect(self.update_add_speed_label)
        self.remove_slider.valueChanged.connect(self.update_remove_speed_label)

        self.start_button.clicked.connect(self.startThreads)

        add_layout = QHBoxLayout()
        remove_layout = QHBoxLayout()

        add_layout.addWidget(self.add_slider)
        add_layout.addWidget(self.add_speed_label)

        remove_layout.addWidget(self.remove_slider)
        remove_layout.addWidget(self.remove_speed_label)

        main_layout.addWidget(self.text_edit)
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.start_button)
        main_layout.addLayout(add_layout)
        main_layout.addLayout(remove_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    @pyqtSlot(str)
    def update_text(self, char):
        if len(self.buffer) < 200:
            self.buffer += char
            self.text_edit.setText(self.buffer)
            self.progress_bar.setValue(len(self.buffer))

    @pyqtSlot()
    def remove_text(self):
        if self.buffer:
            self.buffer = self.buffer[:-1]
            self.text_edit.setText(self.buffer)
            self.progress_bar.setValue(len(self.buffer))

    def update_add_speed_label(self):
        self.add_speed_label.setText(f"Prędkość dodawania znaków: {self.add_slider.value()} ms")

    def update_remove_speed_label(self):
        self.remove_speed_label.setText(f"Prędkość usuwania znaków: {self.remove_slider.value()} ms")

    def startThreads(self):
        self.add_thread = AddThread(self.add_slider)
        self.remove_thread = RemoveThread(self.remove_slider)

        self.add_thread.new_char.connect(self.update_text)
        self.remove_thread.remove_char.connect(self.remove_text)
        self.add_thread.start()
        self.remove_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
