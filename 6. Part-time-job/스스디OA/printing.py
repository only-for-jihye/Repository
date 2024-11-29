from reportlab.pdfgen import canvas

def generate_invoice(data, output_path):
    """송장 출력 PDF 생성"""
    c = canvas.Canvas(output_path)
    c.setFont("Helvetica", 12)

    for idx, row in data.iterrows():
        text = f"{row['고객명']} [{row['상품번호']}] {row['상품명']} {row['상품명2']} - {row['주소']}"
        c.drawString(50, 800 - idx * 20, text)

    c.save()

