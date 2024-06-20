from fpdf import FPDF

class Generate():
    def __init__(self, name):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 34)
        pdf.cell(0, 50, text="CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=0, y=70)
        pdf.set_font_size(25)
        pdf.set_text_color(255,255,255)
        pdf.text(x=52, y=140, text=f"{name} took CS50")
        pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    return Generate(name)

if __name__ == '__main__':
    main()
