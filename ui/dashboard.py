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
        content.setSpacing(20)
        content.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel("🚀 AI-Driven NextGen Firewall Dashboard")
        header.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("""
            background-color: #1E3A8A;  /* dark blue */
            color: white;
            padding: 15px;
            border-radius: 10px;
        """)

        # Cards Row
        cards_row = QHBoxLayout()
        cards_row.setSpacing(25)
        card_data = [
            ("Active Connections", "152", "#FFD700"),  # yellow number
            ("Blocked Attacks", "34", "#FF4500"),      # orange/red
            ("Zero Trust Sessions", "89", "#00FF7F"),  # green
            ("Anomalies Detected", "12", "#FFA500"),   # bright orange
        ]
        for title, value, color in card_data:
            card = self._create_card(title, value, color)
            cards_row.addWidget(card)

        # Threat Table
        table_label = QLabel("Recent Threat Events")
        table_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        table_label.setStyleSheet("color: #1E40AF; padding: 5px;")

        table = QTableWidget(5, 3)
        table.setHorizontalHeaderLabels(["Timestamp", "Threat Type", "Action Taken"])
        table.horizontalHeader().setStretchLastSection(True)
        table.verticalHeader().setDefaultSectionSize(40)
        table.setStyleSheet("""
            QTableWidget {
                font-size: 14px;
                gridline-color: #93C5FD;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #3B82F6;  /* blue header */
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
        """)

        # Sample data
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
            # Alternate row coloring
            if row % 2 == 0:
                for col in range(3):
                    table.item(row, col).setBackground(Qt.GlobalColor.lightGray)

        # Add widgets to layout
        content.addWidget(header)
        content.addLayout(cards_row)
        content.addWidget(table_label)
        content.addWidget(table)

    def _create_card(self, title, value, color):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: #3B82F6;   /* vibrant blue card */
                border-radius: 15px;
                padding: 25px;
            }
        """)
        layout = QVBoxLayout(frame)
        layout.setSpacing(10)

        label_title = QLabel(title)
        label_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        label_title.setStyleSheet("color: white;")

        label_value = QLabel(value)
        label_value.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        label_value.setStyleSheet(f"color: {color};")  # bright number color

        layout.addWidget(label_title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_value, alignment=Qt.AlignmentFlag.AlignCenter)
        return frame
