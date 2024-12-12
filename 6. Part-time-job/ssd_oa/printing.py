import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm



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
            pdfmetrics.registerFont(TTFont('Malgun', 'Malgun.ttf'))  # 한글 폰트 파일 경로 설정
            # pdfmetrics.registerFont(TTFont('Candara', 'Candara.ttf'))
            
            # 저장 경로 선택
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF 파일", "*.pdf")],
                title="PDF 저장 위치 선택"
            )

            page_width, page_height = landscape(A4)
            doc = SimpleDocTemplate(
                output_path,
                pagesize=landscape(A4),  # 가로 방향
            )
            print('A')
            # 데이터 재구성
            pages = arrange_data(df)
            print('B')
            # 저장 취소 시 종료
            if not output_path:
                return

            # PDF 캔버스 생성
            # c = canvas.Canvas(output_path, pagesize=letter)
            c = SimpleDocTemplate(output_path, pagesize=A4)

            # width, height = letter

            # 페이지당 8개의 데이터로 나누기
            rows_per_page = 8
            pages = [df[i:i + rows_per_page] for i in range(0, len(df), rows_per_page)]
            print('C')
            # print(type(pages))
            # print(pages)

            # 테이블 스타일
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # 헤더 배경
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),      # 헤더 텍스트
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),             # 가운데 정렬
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),       # 기본 글꼴
                ('FONTSIZE', (0, 0), (-1, -1), 10),                # 글자 크기
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black)      # 테두리
            ])

            # PDF 요소 생성
            elements = []
            for page_data in pages:
                print(page_data)
                table = Table(page_data, colWidths=[9 * cm] * 2, rowHeights=[2.5 * cm] * 4)
                table.setStyle(table_style)
                print('D')
                elements.append(table)
                print('E')
            
            # 마지막 페이지에서 PageBreak 제거
            if elements[-1] == PageBreak():
                elements.pop()

            # PDF 생성
            c.build(elements)

            # 저장 성공 메시지
            messagebox.showinfo("성공", f"PDF가 {output_path}에 저장되었습니다.")

            # 자동 열기 옵션 (선택적)
            if messagebox.askyesno("PDF 열기", "생성된 PDF를 바로 열까요?"):
                os.startfile(output_path)

        except Exception as e:
            print(e)
            messagebox.showerror("오류", f"PDF 생성 중 오류 발생: {str(e)}")

def arrange_data(df, items_per_page=8):
    """데이터를 열 기반으로 정렬 (1-5, 2-6, ...)"""
    data = df.values.tolist()

    pages = []
    for i in range(0, len(data), items_per_page):
        chunk = data[i:i + items_per_page]
        # 왼쪽 열: 상위 4개, 오른쪽 열: 하위 4개
        left_col = chunk[:len(chunk) // 2]  # 왼쪽 열
        right_col = chunk[len(chunk) // 2:]  # 오른쪽 열

        # 빈 공간 채우기
        while len(left_col) < items_per_page // 2:
            left_col.append(['999'])  # 빈 데이터 행
        while len(right_col) < items_per_page // 2:
            right_col.append(['999'])  # 빈 데이터 행

        # 두 열 합치기 (각 행을 [왼쪽, 오른쪽]으로 구성)
        page_data = [[str(left[0]), str(right[0])] for left, right in zip(left_col, right_col)]
        pages.append(page_data)
    # print(f"pages: {pages}")
    return pages

def main():
    root = tk.Tk()
    app = InvoicePrinter(root)
    root.mainloop()

if __name__ == "__main__":
    main()