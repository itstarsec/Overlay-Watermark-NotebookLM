import fitz
import os


def stamp_png_on_pdf(input_pdf: str, png_path: str, output_pdf: str):
    if not os.path.isfile(input_pdf):
        raise FileNotFoundError(f"Không tìm thấy file PDF: {input_pdf}")

    if not os.path.isfile(png_path):
        raise FileNotFoundError(f"Không tìm thấy file PNG: {png_path}")

    doc = fitz.open(input_pdf)

    rect = fitz.Rect(
        (1317.6918650274654 + 1348.2856395500914)/2 - (1348.2856395500914 - 1317.6918650274654)*1.5 - 17,
        745.3270852858482,
        (1317.6918650274654 + 1348.2856395500914)/2 + (1348.2856395500914 - 1317.6918650274654)*1.5,
        760.8022492970947,
    )
    

    for page in doc:
        page.insert_image(rect, filename=png_path, overlay=True)

    doc.save(output_pdf, garbage=4, deflate=True)
    doc.close()


if __name__ == "__main__":
    stamp_png_on_pdf(
        input_pdf="Invisible_Fortress_Strategy.pdf",
        png_path="your_logo.png",
        output_pdf="Invisible_Fortress_Strategy.stamped.pdf",
    )