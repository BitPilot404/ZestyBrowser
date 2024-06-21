from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class SimpleWebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_engine = "https://www.google.com"
        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        new_tab_button = QPushButton("+")
        new_tab_button.clicked.connect(lambda: self.add_new_tab())
        new_tab_button.setFixedSize(25, 25)

        toolbar = QToolBar()
        toolbar.addWidget(new_tab_button)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        self.choose_engine_popup()

    def choose_engine_popup(self):
        dialog = SearchEngineDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.selected_engine = dialog.selected_engine
            self.add_new_tab(self.selected_engine)

    def add_new_tab(self, url=None):
        if url is None:
            url = self.selected_engine
        webview = QWebEngineView()
        webview.load(QUrl(url))
        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.addWidget(webview)
        container.setLayout(container_layout)
        self.tabs.addTab(container, "New Tab")
        self.tabs.setCurrentWidget(container)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

class SearchEngineDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Search Engine")
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(400, 200)
        self.selected_engine = None

        layout = QVBoxLayout()

        google_button = QPushButton(QIcon('google_logo.png'), "Google")
        google_button.clicked.connect(lambda: self.choose_search_engine("https://www.google.com"))

        duckduckgo_button = QPushButton(QIcon('duckduckgo_logo.png'), "DuckDuckGo")
        duckduckgo_button.clicked.connect(lambda: self.choose_search_engine("https://www.duckduckgo.com"))

        bing_button = QPushButton(QIcon('bing_logo.png'), "Bing")
        bing_button.clicked.connect(lambda: self.choose_search_engine("https://www.bing.com"))

        layout.addWidget(QLabel("Choose a search engine:"))
        layout.addWidget(google_button)
        layout.addWidget(duckduckgo_button)
        layout.addWidget(bing_button)

        self.setLayout(layout)

    def choose_search_engine(self, url):
        self.selected_engine = url
        self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleWebBrowser()
    browser.show()
    sys.exit(app.exec_())
