from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
import os
import sys
import excel_processing

class ExcelToolApp(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 뒤로 가기 버튼 동작을 위한 Parent 추가
        self.parent_window = parent 

        self.setWindowTitle("SEUSEUDI Tool App - Excel")
        self.setGeometry(100, 100, 400, 300)

        # 파일 경로 저장용 변수
        self.file_paths = {"org_file": None, "region_file": None, "fee_file": None}

        # UI Layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # 버튼 1: 원본 파일
        self.btn_org_file = QPushButton("1. 사방넷에서 다운 받은 원본 파일 선택", self)
        self.btn_org_file.clicked.connect(lambda: self.select_file("org_file"))
        self.layout.addWidget(self.btn_org_file)

        # 버튼 2: 지역 구분 파일
        self.btn_region_file = QPushButton("2. 지역 구분 파일 선택", self)
        self.btn_region_file.clicked.connect(lambda: self.select_file("region_file"))
        self.layout.addWidget(self.btn_region_file)

        # 버튼 3: 배송비 구분 파일
        self.btn_fee_file = QPushButton("3. 배송비 구분 파일 선택", self)
        self.btn_fee_file.clicked.connect(lambda: self.select_file("fee_file"))
        self.layout.addWidget(self.btn_fee_file)

        # 버튼 4: 실행 버튼
        self.btn_execute = QPushButton("4. 실행", self)
        self.btn_execute.clicked.connect(self.execute_with_files)
        self.layout.addWidget(self.btn_execute)

        # 파일 경로 상태 표시 레이블
        self.label_status = QLabel("파일 경로 상태: 없음", self)
        self.layout.addWidget(self.label_status)

        # 뒤로가기 버튼
        self.btn_back = QPushButton("뒤로가기", self)
        self.btn_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.btn_back)

        # 종료 버튼
        self.btn_exit = QPushButton("종료", self)
        self.btn_exit.clicked.connect(self.exit_application)  # 종료 메서드 연결
        self.layout.addWidget(self.btn_exit)

        self.setCentralWidget(self.central_widget)

    def go_back(self):
        """
        뒤로 가기
        """
        self.close()
        self.parent_window.show()

    def exit_application(self):
        """
        종료
        """
        self.close()  # 현재 창 닫기
        QApplication.instance().quit()  # 애플리케이션 종료


    def select_file(self, key):
        """
        파일 선택 및 경로 저장
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "파일 선택", "", "All Files (*);;Excel Files (*.xlsx)")
        if file_path:
            self.file_paths[key] = file_path
            self.update_status()
        else:
            print(f"{key} 파일 선택이 취소되었습니다.")


    def update_status(self):
        """
        현재 선택된 파일 경로를 레이블에 표시
        """
        status = "\n".join([f"{key}: {path or '선택되지 않음'}" for key, path in self.file_paths.items()])
        self.label_status.setText(f"파일 경로 상태:\n{status}")
        print(f"현재 파일 경로 상태:\n{status}")

    def execute_with_files(self):
        """
        저장된 파일 경로를 메서드로 전달
        """
        if all(self.file_paths.values()):
            self.process_files(self.file_paths)
        else:
            self.label_status.setText("모든 파일 경로를 선택해야 실행 가능합니다.")
            print("파일 경로가 모두 선택되지 않았습니다.")


    def process_files(self, file_paths):
        """
        파일 경로를 전달받아 처리
        """
        # print("실행된 파일 경로:")
        # for key, path in file_paths.items():
        #     print(f"{key}: {path}")
        # print(file_paths)
        # print(type(file_paths))
        excel_processing.exec(
            org_file_path=file_paths['org_file']
            , region_file_path=file_paths['region_file']
            , fee_file_path=file_paths['fee_file']
        )
        self.label_status.setText("모든 파일이 성공적으로 처리되었습니다.")

    # def execute(self):
    #     # print(self.org_select_file)
    #     # print(self.std_select_file)
    #     # print(self.std2_select_file)
    #     # excel_processing.excel_processing_exec(self.org_select_file, self.std_select_file, self.std2_select_file)
    #     excel_processing.excel_processing_exec(
    #         'C:/Users/샘플/Desktop/test/원본.xlsx'
    #         , 'C:/Users/샘플/Desktop/test/지역.xlsx'
    #         , 'C:/Users/샘플/Desktop/test/배송비.xlsx'
    #     )

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SEUSEUDI Tool App")
        self.setGeometry(150, 100, 300, 400)

        # QLabel에 스스디 이미지 추가
        self.label = QLabel(self)
        self.label.setGeometry(75, 10, 165, 42)  # 위치와 크기 설정
        pixmap = QPixmap("2sd.png")  # 이미지 파일 경로
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)  # 이미지 크기를 QLabel 크기에 맞게 조정

        # 초기 화면 레이아웃
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # 엑셀 파일 도구
        self.btn_tool = QPushButton("엑셀 파일 도구", self)
        self.btn_tool.clicked.connect(self.show_excel_tool_buttons)
        self.layout.addWidget(self.btn_tool)

        # 송장 출력 도구
        self.btn_tool = QPushButton("송장 출력 도구", self)
        self.btn_tool.clicked.connect(self.show_excel_tool_buttons)
        self.layout.addWidget(self.btn_tool)

        # 네이버 지도 marker 도구
        self.btn_tool = QPushButton("지도 마커 도구", self)
        self.btn_tool.clicked.connect(self.show_excel_tool_buttons)
        self.layout.addWidget(self.btn_tool)

        # 종료 버튼
        self.btn_exit = QPushButton("종료", self)
        self.btn_exit.clicked.connect(self.exit_application)  # 종료 메서드 연결
        self.layout.addWidget(self.btn_exit)

        self.setCentralWidget(self.central_widget)

    def exit_application(self):
        """
        종료
        """
        self.close()  # 현재 창 닫기
        QApplication.instance().quit()  # 애플리케이션 종료

    def show_excel_tool_buttons(self):
        """
        엑셀 Tool 화면을 불러오는 함수
        """
        tool_window = ExcelToolApp(self)
        tool_window.show()
        # self.close()
        self.hide()
 

if __name__ == "__main__":
    # C:\Users\샘플\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyQt5\Qt5\plugins
    # C:\Users\샘플\AppData\Local\Programs\Python\Python312\Lib\site-packages\PyQt5\Qt\plugins\platforms
    # if sys.platform == "win32":
    #     os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(
    #         os.path.dirname(sys.executable), "Lib", "site-packages", "PyQt5", "Qt5", "plugins", "platforms"
    #         # "C:","Users","샘플","AppData","Local","Programs","Python","Python312", "Lib", "site-packages", "PyQt5", "Qt5", "plugins", "platforms"
    #     )
    # app = QApplication([])
    # window = MainUI()
    # window.show()
    # app.exec_()

    app = QApplication(sys.argv)
    main_window = MainUI()
    main_window.show()
    sys.exit(app.exec_())