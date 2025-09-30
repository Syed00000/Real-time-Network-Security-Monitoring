from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ThreatIntelPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("🧠 Threat Intelligence Feed")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        feed = QTextEdit()
        feed.setReadOnly(True)
        feed.setPlainText(
            "[2025-09-30 12:00] New IoC feed from STIX/TAXII\n"
            "[2025-09-30 12:15] AI model updated with federated learning\n"
            "[2025-09-30 12:30] MITRE ATT&CK T1071 (App Layer Protocol) flagged\n"
        )

        layout.addWidget(title)
        layout.addWidget(feed)
