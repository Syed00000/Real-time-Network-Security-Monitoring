from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class IncidentPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("⚠️ Automated Incident Response")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        log = QListWidget()
        log.addItems([
            "Malware blocked - IP 192.168.1.20",
            "Suspicious login quarantined - User2",
            "C2 traffic isolated - Device IoT_34",
        ])

        btn = QPushButton("Run Full System Scan")

        layout.addWidget(title)
        layout.addWidget(log)
        layout.addWidget(btn)
