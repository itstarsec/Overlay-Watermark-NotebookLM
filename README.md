# 📄 PDF Logo Stamping Tool (PyMuPDF)

## 🚀 Giới thiệu
Công cụ này cho phép bạn tự động chèn (stamp) một ảnh PNG vào tất cả các trang của file PDF tại một vị trí tọa độ cố định.

## ⚙️ Cách hoạt động
- Sử dụng PyMuPDF (fitz)
- Dùng tọa độ fitz.Rect để đặt logo

## 📦 Cài đặt
pip install pymupdf

## ▶️ Cách dùng
python stamp_pdf.py

## 🧠 Logic chính
rect = fitz.Rect(
    center - width*1.5 - offset_left,
    y1,
    center + width*1.5,
    y2,
)

## ⚡ Lợi ích
- Tự động hóa
- Branding PDF hàng loạt
- Không sửa nội dung gốc
