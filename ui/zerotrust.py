from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ZeroTrustPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("🔒 Zero Trust Session Monitoring")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #DBEAFE;")  # dark blue title

        # Sessions list
        sessions = QListWidget()
        sessions.addItems([
            "User1 (HR Dept) - Verified ✅",
            "User2 (Remote) - MFA Pending ⏳",
            "User3 (Admin) - Denied ❌",
            "IoT_Device_12 - Verified ✅",
        ])
        sessions.setFont(QFont("Arial", 16))
        sessions.setStyleSheet("""
            QListWidget {
                background-color: #DBEAFE;      /* light blue background */
                border-radius: 10px;
                padding: 10px;
            }
            QListWidget::item {
                color: #1F2937;                 /* dark gray text for readability */
                padding: 5px;
            }
        """)

        # Add widgets
        layout.addWidget(title)
        layout.addWidget(sessions)
