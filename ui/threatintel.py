from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ThreatIntelPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("🧠 Threat Intelligence Feed")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #DBEAFE;")  # dark blue for contrast

        # Feed box
        feed = QTextEdit()
        feed.setReadOnly(True)
        feed.setPlainText(
            "[2025-09-30 12:00] New IoC feed from STIX/TAXII\n"
            "[2025-09-30 12:15] AI model updated with federated learning\n"
            "[2025-09-30 12:30] MITRE ATT&CK T1071 (App Layer Protocol) flagged\n"
        )
        feed.setFont(QFont("Arial", 16))
        feed.setStyleSheet("""
            QTextEdit {
                background-color: #DBEAFE;   /* light blue background */
                color: #1F2937;              /* dark gray text for readability */
                border-radius: 10px;
                padding: 10px;
            }
        """)

        # Add widgets
        layout.addWidget(title)
        layout.addWidget(feed)
