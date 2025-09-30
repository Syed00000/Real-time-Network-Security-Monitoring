import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QListWidget, QListWidgetItem, QWidget, QHBoxLayout
from PyQt6.QtGui import QIcon
from ui.dashboard import Dashboard
from ui.traffic import TrafficPage
from ui.zerotrust import ZeroTrustPage
from ui.threatintel import ThreatIntelPage
from ui.incident import IncidentPage
from ui.settings import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI-Driven NextGen Firewall - Prototype")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("assets/icons/firewall.png"))

        # Main layout container
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(220)
        self.sidebar.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: white;
                border: none;
            }
            QListWidget::item {
                padding: 15px;
                font-size: 14px;
            }
            QListWidget::item:selected {
                background-color: #34495e;
            }
        """)
        pages = [
            ("Dashboard", Dashboard, "assets/icons/dashboard.png"),
            ("Traffic Analysis", TrafficPage, "assets/icons/traffic.png"),
            ("Zero Trust", ZeroTrustPage, "assets/icons/lock.png"),
            ("Threat Intel", ThreatIntelPage, "assets/icons/ai.png"),
            ("Incident Response", IncidentPage, "assets/icons/alert.png"),
            ("Settings", SettingsPage, "assets/icons/settings.png"),
        ]
        self.page_map = {}

        for name, page_class, icon in pages:
            item = QListWidgetItem(QIcon(icon), name)
            self.sidebar.addItem(item)

        # Stacked pages
        self.stacked_widget = QStackedWidget()
        for name, page_class, _ in pages:
            page = page_class()
            self.page_map[name] = page
            self.stacked_widget.addWidget(page)

        # Connect sidebar clicks
        self.sidebar.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)

        # Default page = Dashboard
        self.sidebar.setCurrentRow(0)

        # Add widgets to layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
