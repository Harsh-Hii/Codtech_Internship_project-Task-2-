import pandas as pd

# Load the CSV file
df = pd.read_csv("data.csv")

# Basic analysis
average_score = df['Score'].mean()
max_score = df['Score'].max()
min_score = df['Score'].min()



# NOTE : For visualised Pdf install the extension vscode-pdf 


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Score Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Write summary
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Score: {max_score}", ln=True)
pdf.cell(0, 10, f"Lowest Score: {min_score}", ln=True)

pdf.ln(10)
pdf.cell(0, 10, "Detailed Scores:", ln=True)

# Add table
for i, row in df.iterrows():
    pdf.cell(0, 10, f"{row['Name']}: {row['Score']}", ln=True)

# Save the PDF
pdf.output("report.pdf")
