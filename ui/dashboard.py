from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main vertical layout
        content = QVBoxLayout(self)

        # Header
        header = QLabel("🚀 AI-Driven NextGen Firewall Dashboard")
        header.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Cards Row
        cards_row = QHBoxLayout()
        card_data = [
            ("Active Connections", "152"),
            ("Blocked Attacks", "34"),
            ("Zero Trust Sessions", "89"),
            ("Anomalies Detected", "12"),
        ]
        for title, value in card_data:
            card = self._create_card(title, value)
            cards_row.addWidget(card)

        # Threat Table
        table_label = QLabel("Recent Threat Events")
        table_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        table = QTableWidget(5, 3)
        table.setHorizontalHeaderLabels(["Timestamp", "Threat Type", "Action Taken"])
        table.horizontalHeader().setStretchLastSection(True)
        table.setStyleSheet("QTableWidget { border: 1px solid #ccc; }")

        sample_data = [
            ("2025-09-30 12:45", "Polymorphic Malware", "Blocked"),
            ("2025-09-30 12:50", "C2 Communication", "Quarantined"),
            ("2025-09-30 13:05", "Suspicious Login", "Denied"),
            ("2025-09-30 13:20", "Anomaly Detected", "Isolated"),
            ("2025-09-30 13:25", "TLS Bypass Attempt", "Blocked"),
        ]
        for row, (time, ttype, action) in enumerate(sample_data):
            table.setItem(row, 0, QTableWidgetItem(time))
            table.setItem(row, 1, QTableWidgetItem(ttype))
            table.setItem(row, 2, QTableWidgetItem(action))

        # Add widgets
        content.addWidget(header)
        content.addLayout(cards_row)
        content.addWidget(table_label)
        content.addWidget(table)

    def _create_card(self, title, value):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: #ecf0f1;
                border-radius: 12px;
                padding: 15px;
            }
        """)
        layout = QVBoxLayout(frame)

        label_title = QLabel(title)
        label_title.setFont(QFont("Arial", 12))
        label_value = QLabel(value)
        label_value.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        label_value.setStyleSheet("color: #27ae60;")

        layout.addWidget(label_title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_value, alignment=Qt.AlignmentFlag.AlignCenter)
        return frame
