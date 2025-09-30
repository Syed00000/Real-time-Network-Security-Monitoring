from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ZeroTrustPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("🔒 Zero Trust Session Monitoring")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sessions = QListWidget()
        sessions.addItems([
            "User1 (HR Dept) - Verified ✅",
            "User2 (Remote) - MFA Pending ⏳",
            "User3 (Admin) - Denied ❌",
            "IoT_Device_12 - Verified ✅",
        ])

        layout.addWidget(title)
        layout.addWidget(sessions)
