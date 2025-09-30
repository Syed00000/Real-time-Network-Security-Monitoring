from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class TrafficPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("📡 Real-Time Traffic Analysis")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #DBEAFE;")  # dark blue title

        # Upload Progress Bar
        upload = QProgressBar()
        upload.setValue(65)
        upload.setFormat("Upload: 65%")
        upload.setFont(QFont("Arial", 14))
        upload.setStyleSheet("""
            QProgressBar {
                background-color: #DBEAFE;       /* light blue */
                border-radius: 10px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3B82F6;       /* vibrant blue chunk */
                border-radius: 10px;
            }
        """)

        # Download Progress Bar
        download = QProgressBar()
        download.setValue(45)
        download.setFormat("Download: 45%")
        download.setFont(QFont("Arial", 14))
        download.setStyleSheet("""
            QProgressBar {
                background-color: #DBEAFE;
                border-radius: 10px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #2563EB;       /* slightly darker blue chunk */
                border-radius: 10px;
            }
        """)

        # Add widgets
        layout.addWidget(title)
        layout.addWidget(upload)
        layout.addWidget(download)
