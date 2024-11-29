from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton
import os
import sys
from excel_processing import add_shipping_fee

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Excel Processing Tool")
        self.setGeometry(100, 100, 800, 600)

        # 원본 엑셀 파일 선택 버튼
        self.file_button = QPushButton("원본 엑셀 파일 선택", self)
        self.file_button.setGeometry(50, 50, 200, 30)
        self.file_button.clicked.connect(self.org_select_file)

        # 착불비 기준 엑셀 파일 선택 버튼
        self.file_button2 = QPushButton("기준 엑셀 파일 선택", self)
        self.file_button2.setGeometry(150, 150, 200, 30)
        self.file_button2.clicked.connect(self.std_select_file)

        # 우편번호 엑셀 파일 선택 버튼
        self.file_button3 = QPushButton("기준 엑셀 파일 선택", self)
        self.file_button3.setGeometry(250, 250, 200, 30)
        self.file_button3.clicked.connect(self.std2_select_file)

        print(self.org_select_file)

        add_shipping_fee(self.org_select_file
                         , self.std_select_file
                         , self.std2_select_file)

    def org_select_file(self):
        org_file_name, _ = QFileDialog.getOpenFileName(self, "원본 엑셀 파일 선택", "", "Excel Files (*.xlsx)")
        if org_file_name :
            print(f"원본 선택된 파일: {org_file_name}")
        else :
            print("원본 파일 선택되지 않음")
        return org_file_name

    def std_select_file(self):
        std_file_name, _ = QFileDialog.getOpenFileName(self, "기준 엑셀 파일 선택", "", "Excel Files (*.xlsx)")
        if std_file_name :
            print(f"기준 선택된 파일: {std_file_name}")
        else :
            print("기준 파일 선택되지 않음")
        return std_file_name

    def std2_select_file(self):
        std2_file_name, _ = QFileDialog.getOpenFileName(self, "기준 엑셀 파일 선택", "", "Excel Files (*.xlsx)")
        if std2_file_name :
            print(f"기준 선택된 파일: {std2_file_name}")
        else :
            print("기준 파일 선택되지 않음")
        return std2_file_name


if __name__ == "__main__":
    # C:\Users\샘플\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyQt5\Qt5\plugins
    # C:\Users\샘플\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyQt5\Qt\plugins\platforms
    if sys.platform == "win32":
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(
            os.path.dirname(sys.executable), "Lib", "site-packages", "PyQt5", "Qt5", "plugins", "platforms"
            # "C:","Users","샘플","AppData","Local","Programs","Python","Python312", "Lib", "site-packages", "PyQt5", "Qt5", "plugins", "platforms"
        )
    app = QApplication([])
    window = MainUI()
    window.show()
    app.exec_()
