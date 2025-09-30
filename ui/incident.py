from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class IncidentPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("⚠️ Automated Incident Response")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #DBEAFE;")  # dark blue title

        # Log list
        log = QListWidget()
        log.addItems([
            "Malware blocked - IP 192.168.1.20",
            "Suspicious login quarantined - User2",
            "C2 traffic isolated - Device IoT_34",
        ])
        log.setStyleSheet("""
            QListWidget {
                background-color: #DBEAFE;      /* light blue */
                font-size: 16px;
                padding: 10px;
            }
            QListWidget::item {
                color: #1F2937;                 /* dark gray text for readability */
                padding: 5px;
            }
        """)

        # Scan button
        btn = QPushButton("Run Full System Scan")
        btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        btn.setStyleSheet("""
            QPushButton {
                background-color: #3B82F6;      /* vibrant blue */
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2563EB;      /* slightly darker blue on hover */
            }
        """)

        # Add widgets to layout
        layout.addWidget(title)
        layout.addWidget(log)
        layout.addWidget(btn)
