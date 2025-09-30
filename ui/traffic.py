from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class TrafficPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("📡 Real-Time Traffic Analysis")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Fake progress bars to show network load
        upload = QProgressBar()
        upload.setValue(65)
        upload.setFormat("Upload: 65%")
        download = QProgressBar()
        download.setValue(45)
        download.setFormat("Download: 45%")

        layout.addWidget(title)
        layout.addWidget(upload)
        layout.addWidget(download)
