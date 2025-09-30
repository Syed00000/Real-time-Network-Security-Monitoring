from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("⚙️ Firewall Settings")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        chk1 = QCheckBox("Enable Deep Packet Inspection")
        chk1.setChecked(True)
        chk2 = QCheckBox("Enable Zero Trust Enforcement")
        chk2.setChecked(True)
        chk3 = QCheckBox("Enable AI Threat Detection")
        chk3.setChecked(True)

        layout.addWidget(title)
        layout.addWidget(chk1)
        layout.addWidget(chk2)
        layout.addWidget(chk3)
