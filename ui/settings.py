from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("⚙️ Firewall Settings")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #DBEAFE;")  # dark blue for contrast

        # Checkboxes
        chk_style = """
            QCheckBox {
                font-size: 16px;
                color: white;           /* dark gray text for readability */
                padding: 5px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """

        chk1 = QCheckBox("Enable Deep Packet Inspection")
        chk1.setChecked(True)
        chk1.setStyleSheet(chk_style)

        chk2 = QCheckBox("Enable Zero Trust Enforcement")
        chk2.setChecked(True)
        chk2.setStyleSheet(chk_style)

        chk3 = QCheckBox("Enable AI Threat Detection")
        chk3.setChecked(True)
        chk3.setStyleSheet(chk_style)

        # Add widgets
        layout.addWidget(title)
        layout.addWidget(chk1)
        layout.addWidget(chk2)
        layout.addWidget(chk3)
