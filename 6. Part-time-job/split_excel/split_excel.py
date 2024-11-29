import os

import pandas as pd
from openpyxl import Workbook

# python GUI
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def split_excel_by_column(input_file, column_name, output_dir):
    """
    엑셀 파일을 특정 열(구분)의 값을 기준으로 분리하여 저장하는 함수.
    
    Args:
        input_file (str): 입력 엑셀 파일 경로
        column_name (str): 기준이 되는 열 이름
        output_dir (str): 결과 파일을 저장할 폴더 경로
    """
    try:
        # read excel file
        data = pd.read_excel(input_file, engine="openpyxl")
        unique_values = data[column_name].unique()

        # output dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # split data by columns
        for value in unique_values:
            subset = data[data[column_name] == value]
            # print(subset)
            #         구분 성명
            #     0   1  김
            #     1   1  이
            #     2   1  박
            #     구분 성명
            #     3   2  최
            #     4   2  원
            #     구분 성명
            #     5   3  권
            #     6   3  현
            output_file = os.path.join(output_dir, f"{value}.xlsx")
            subset.to_excel(output_file, index=False, engine="openpyxl")

        messagebox.showinfo("Succeed", f"Succeed. \n file dir : {output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"raise Error: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(
        title="분리하고자 하는 엑셀 파일을 선택하세요.",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    input_file_entry.delete(0, "end")
    input_file_entry.insert(0, file_path)

def select_output_dir():
    folder_path = filedialog.askdirectory(title="저장하고자 하는 위치를 선택하세요.")
    output_dir_entry.delete(0, "end")
    output_dir_entry.insert(0, folder_path)

def process_files():
    input_file = input_file_entry.get()
    column_name = column_name_entry.get()
    output_dir = output_dir_entry.get()

    if not input_file or not column_name or not output_dir:
        messagebox.showwarning("Warning!", "입력되지 않은 값이 있습니다.")
        return

    split_excel_by_column(input_file, column_name, output_dir)

# Tkinter GUI 생성
root = Tk()
root.title("엑셀 파일 분리")
root.geometry("500x400")

# 입력 파일 선택
Label(root, text="엑셀 파일 선택 :").pack(pady=5)
input_file_entry = Entry(root, width=50)
input_file_entry.pack(pady=5)
Button(root, text="파일 선택", command=select_input_file).pack(pady=5)

# 기준 열 이름 입력
Label(root, text="분리하고자 하는 열의 이름 :").pack(pady=5)
column_name_entry = Entry(root, width=50)
# column_name_entry = Entry(root, width=50, bg="white")
column_name_entry.pack(pady=5)

# 출력 폴더 선택
Label(root, text="분리고자 하는 파일의 저장 위치 :").pack(pady=5)
output_dir_entry = Entry(root, width=50)
output_dir_entry.pack(pady=5)
Button(root, text="폴더 선택", command=select_output_dir).pack(pady=5)

# 실행 버튼
Button(root, text="실행", command=process_files, bg="lightblue").pack(pady=20)

root.mainloop()


# /Users/wonjongsoo/Library/Python/3.9/lib/python/site-packages