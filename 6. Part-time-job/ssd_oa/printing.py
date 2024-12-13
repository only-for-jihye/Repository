import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


class InvoicePrinter:
    def __init__(self, root):
        self.root = root
        self.root.title("송장 출력 시스템")
        self.root.geometry("600x500")

        # 엑셀 파일 읽기 관련 변수
        self.excel_file_path = None
        self.df = None
        self.selected_rows = []

        # UI 설정
        self.create_widgets()

    def create_widgets(self):
        # 파일 선택 버튼
        tk.Button(self.root, text="엑셀 파일 선택", command=self.load_excel_file).pack(pady=10)

        # 데이터 테이블
        self.tree = ttk.Treeview(self.root, columns=list(range(10)), show='headings')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        # 스크롤바 추가
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 선택 및 출력 버튼
        tk.Button(self.root, text="선택된 데이터 출력", command=self.print_selected_invoices).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.root, text="전체 데이터 출력", command=self.print_all_invoices).pack(side=tk.RIGHT, padx=10, pady=10)

    def load_excel_file(self):
        # 엑셀 파일 선택 및 로드
        self.excel_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])
        
        if self.excel_file_path:
            try:
                # 엑셀 파일 읽기
                self.df = pd.read_excel(self.excel_file_path)
                
                # 트리뷰 초기화
                for i in self.tree.get_children():
                    self.tree.delete(i)
                
                # 컬럼 설정
                self.tree["columns"] = list(self.df.columns)
                for col in self.df.columns:
                    self.tree.heading(col, text=col)
                    self.tree.column(col, width=100)
                
                # 체크박스 컬럼 추가
                self.tree["columns"] = tuple(["선택"] + list(self.df.columns))
                self.tree.heading("선택", text="선택")
                self.tree.column("선택", width=50)
                
                # 데이터 추가
                for index, row in self.df.iterrows():
                    self.tree.insert("", "end", values=(False,) + tuple(row))
                
                # 체크박스 이벤트 바인딩
                self.tree.bind("<ButtonRelease-1>", self.toggle_checkbox)

            except Exception as e:
                messagebox.showerror("오류", f"파일을 읽는 중 오류 발생: {str(e)}")

    def toggle_checkbox(self, event):
        # 체크박스 토글 기능
        region = self.tree.identify("region", event.x, event.y)
        if region == "cell":
            column = self.tree.identify_column(event.x)
            if column == "#1":  # 첫 번째 컬럼 (체크박스)
                item = self.tree.identify_row(event.y)
                current_value = self.tree.set(item, column)
                new_value = not eval(current_value)
                self.tree.set(item, column, new_value)

                # 선택된 행 추적
                if new_value:
                    self.selected_rows.append(self.tree.index(item))
                else:
                    self.selected_rows.remove(self.tree.index(item))

    def print_selected_invoices(self):
        # 선택된 데이터만 출력
        if not self.selected_rows:
            messagebox.showwarning("경고", "선택된 데이터가 없습니다.")
            return

        selected_df = self.df.iloc[self.selected_rows]
        self.create_custom_invoice_pdf(selected_df)

    def print_all_invoices(self):
        # 전체 데이터 출력
        if self.df is None:
            messagebox.showwarning("경고", "먼저 엑셀 파일을 선택해주세요.")
            return

        self.create_custom_invoice_pdf(self.df)

    def create_custom_invoice_pdf(self, df):
        try:
            # 폰트 등록 (한글 지원을 위해)
            pdfmetrics.registerFont(TTFont('MalgunGothic', 'malgun.ttf'))  # 한글 폰트 파일 경로 설정
            # pdfmetrics.registerFont(TTFont('Candara', 'Candara.ttf'))
            
            # 저장 경로 선택
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF 파일", "*.pdf")],
                title="PDF 저장 위치 선택"
            )
            
            # 고객명, 상품명, 주소를 하나의 문자열로 결합
            # df_selected = df.apply(lambda row: f"{row['고객명']}\n{row['상품명']}\n{row['주소']}", axis=1).tolist()
            df_selected = df.apply(lambda row: f"{row['우편번호']}\n{row['주소1']}\n{row['주소2']}", axis=1).tolist()
            # print(df_selected)
            # 데이터 배열로 변환
            data_array = [[item] for item in df_selected]
            
            # 페이지 크기 설정 (A4)
            page_width, page_height = A4

            # 좌우/위/아래 간격
            margin = 1 * cm

            # 셀 크기 계산
            cell_width = (page_width - 2 * margin) / 2  # 2열
            cell_height = (page_height - 2 * margin) / 4  # 4행

            # PDF 생성
            c = canvas.Canvas(output_path, pagesize=A4)
            c.setFont("MalgunGothic", 10)

            # 표 시작 위치 (좌측 상단 기준)
            start_x = margin
            start_y = page_height - margin

            # 데이터 입력 순서 (4행 2열)
            num_columns = 2
            num_rows = 4

            current_page = 1  # 페이지 번호

            for i, value in enumerate(data_array):
                col = i % num_columns  # 현재 열 번호
                row = (i // num_columns) % num_rows  # 현재 페이지 내의 행 번호

                # 새 페이지로 넘어가는 조건
                if i > 0 and i % (num_columns * num_rows) == 0:
                    c.showPage()  # 페이지 저장
                    c.setFont("MalgunGothic", 10)  # 폰트 재설정
                    current_page += 1

                # 셀 좌표 계산
                x = start_x + col * cell_width
                y = start_y - (row + 1) * cell_height

                # 데이터 작성 (셀 내 텍스트 왼쪽 상단 정렬)
                lines = str(value).split("\n")
                total_lines = len(lines)
                max_font_size = 10
                font_size_decrement = (max_font_size - 6) / max(1, total_lines - 1)  # Calculate font decrement dynamically

                for idx, line in enumerate(lines):
                    font_size = max(max_font_size - (font_size_decrement * idx), 6)  # Apply calculated font size
                    c.setFont("MalgunGothic", font_size)
                    c.drawString(x + 0.2 * cm, y + cell_height - (0.5 + idx) * cm, line)

                # 셀 테두리 그리기
                c.rect(x, y, cell_width, cell_height)

            # PDF 저장
            c.save()

            # 저장 성공 메시지
            messagebox.showinfo("성공", f"PDF가 {output_path}에 저장되었습니다.")

            # 자동 열기 옵션 (선택적)
            if messagebox.askyesno("PDF 열기", "생성된 PDF를 바로 열까요?"):
                os.startfile(output_path)

        except Exception as e:
            print(e)
            messagebox.showerror("오류", f"PDF 생성 중 오류 발생: {str(e)}")
        except KeyError:
           raise ValueError("DataFrame에 '고객명', '상품명', '주소' 컬럼이 모두 존재해야 합니다.")

def main():
    root = tk.Tk()
    app = InvoicePrinter(root)
    root.mainloop()

if __name__ == "__main__":
    main()