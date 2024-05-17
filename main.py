import os
import sys
import argparse
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QLabel, QTextEdit, QHBoxLayout, QSizePolicy, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt

class XboxHardDriveExplorer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Xbox Hard Drive Explorer")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon("xbox_icon.png"))

        self.layout = QVBoxLayout()

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(""))
        self.tree_view.doubleClicked.connect(self.on_double_click)
        self.layout.addWidget(self.tree_view)

        self.selected_file_label = QLabel("Selected File:")
        self.layout.addWidget(self.selected_file_label)

        self.selected_file_path = QTextEdit()
        self.selected_file_path.setReadOnly(True)
        self.layout.addWidget(self.selected_file_path)

        self.preview_layout = QHBoxLayout()

        self.image_label = QLabel()
        self.preview_layout.addWidget(self.image_label)

        self.video_label = QLabel()
        self.video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.preview_layout.addWidget(self.video_label)

        self.layout.addLayout(self.preview_layout)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        open_action = file_menu.addAction('Open Xbox Hard Drive')
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_hard_drive)

    def open_hard_drive(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Xbox Hard Drive Directory")
        if directory:
            self.model.setRootPath(directory)
            self.tree_view.setRootIndex(self.model.index(directory))

    def on_double_click(self, index):
        file_path = self.model.filePath(index)
        if os.path.isfile(file_path):
            self.selected_file_path.setText(file_path)
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                pixmap = QPixmap(file_path)
                self.image_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))
                self.video_label.clear()
            elif file_path.lower().endswith(('.mp4', '.avi', '.mkv')):
                self.image_label.clear()
                movie = QMovie(file_path)
                self.video_label.setMovie(movie)
                movie.start()
            else:
                self.image_label.clear()
                self.video_label.clear()


def run_gui():
    app = QApplication(sys.argv)
    window = XboxHardDriveExplorer()
    window.show()
    sys.exit(app.exec_())


def main():
    parser = argparse.ArgumentParser(description="Xbox Hard Drive Forensic Analysis Tool")
    parser.add_argument("--gui", action="store_true", help="Run the graphical user interface")
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        print("Command-line mode is not yet implemented. Please use the --gui option to run the GUI.")


if __name__ == "__main__":
    main()
