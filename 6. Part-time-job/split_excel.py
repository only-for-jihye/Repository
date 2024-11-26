import pandas as pd
import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def split_excel_by_column(input_file, column_name, output_dir):
    """
    엑셀 파일을 특정 열의 값을 기준으로 분리하여 저장하는 함수.

    Args:
        input_file (str): 입력 엑셀 파일 경로
        column_name (str): 기준이 되는 열 이름
        output_dir (str): 결과 파일을 저장할 폴더 경로
    """
    try:
        # 엑셀 파일 읽기
        data = pd.read_excel(input_file, engine="openpyxl")
        unique_values = data[column_name].unique()

        # 출력 디렉토리 생성
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 데이터를 구분하여 저장
        for value in unique_values:
            subset = data[data[column_name] == value]
            output_file = os.path.join(output_dir, f"{value}.xlsx")
            subset.to_excel(output_file, index=False, engine="openpyxl")

        messagebox.showinfo("완료", f"파일 분리가 성공적으로 완료되었습니다!\n저장 경로: {output_dir}")
    except Exception as e:
        messagebox.showerror("오류", f"오류 발생: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(
        title="엑셀 파일 선택",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    input_file_entry.delete(0, "end")
    input_file_entry.insert(0, file_path)

def select_output_dir():
    folder_path = filedialog.askdirectory(title="저장 폴더 선택")
    output_dir_entry.delete(0, "end")
    output_dir_entry.insert(0, folder_path)

def process_files():
    input_file = input_file_entry.get()
    column_name = column_name_entry.get()
    output_dir = output_dir_entry.get()

    if not input_file or not column_name or not output_dir:
        messagebox.showwarning("경고", "모든 입력 값을 채워주세요.")
        return

    split_excel_by_column(input_file, column_name, output_dir)

# Tkinter GUI 생성
root = Tk()
root.title("엑셀 파일 분리 도구")
root.geometry("500x300")

# 입력 파일 선택
Label(root, text="입력 엑셀 파일:").pack(pady=5)
input_file_entry = Entry(root, width=50)
input_file_entry.pack(pady=5)
Button(root, text="파일 선택", command=select_input_file).pack(pady=5)

# 기준 열 이름 입력
Label(root, text="기준 열 이름:").pack(pady=5)
column_name_entry = Entry(root, width=500, bg="white")
column_name_entry.pack(pady=5)

# 출력 폴더 선택
Label(root, text="저장 폴더:").pack(pady=5)
output_dir_entry = Entry(root, width=50)
output_dir_entry.pack(pady=5)
Button(root, text="폴더 선택", command=select_output_dir).pack(pady=5)

# 실행 버튼
Button(root, text="실행", command=process_files, bg="lightblue").pack(pady=20)

root.mainloop()


# /Users/wonjongsoo/Library/Python/3.9/lib/python/site-packages