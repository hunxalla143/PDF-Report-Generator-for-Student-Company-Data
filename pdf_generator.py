from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from datetime import datetime
import os


# ==========================================
# GENERATE PDF FUNCTION
# ==========================================

def generate_pdf(data, report_type, filename):

    # ==========================================
    # CHECK EMPTY DATA
    # ==========================================

    if not data:
        print("No data available.")
        return

    # ==========================================
    # CREATE REPORTS FOLDER
    # ==========================================

    os.makedirs("reports", exist_ok=True)

    # ==========================================
    # PDF FILE PATH
    # ==========================================

    pdf_path = f"reports/{filename}.pdf"

    # ==========================================
    # CREATE PDF DOCUMENT
    # ==========================================

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter
    )

    # ==========================================
    # PDF ELEMENTS
    # ==========================================

    elements = []

    # ==========================================
    # STYLES
    # ==========================================

    styles = getSampleStyleSheet()

    # ==========================================
    # LOGO SECTION
    # ==========================================

    logo_path = "assets/logo.png"

    try:

        if os.path.exists(logo_path):

            logo = Image(
                logo_path,
                width=100,
                height=50
            )

            elements.append(logo)
            elements.append(Spacer(1, 12))

    except Exception:
        print("Invalid logo image skipped.")

    # ==========================================
    # TITLE
    # ==========================================

    title = Paragraph(
        f"<b>{report_type} Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    # ==========================================
    # DATE & TIME
    # ==========================================

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    date_para = Paragraph(
        f"Generated On: {current_time}",
        styles['Normal']
    )

    elements.append(date_para)

    elements.append(
        Spacer(1, 20)
    )

    # ==========================================
    # TABLE DATA
    # ==========================================

    table_data = []

    # HEADERS
    headers = list(data[0].keys())

    table_data.append(headers)

    # ROWS
    for item in data:

        row = list(item.values())

        table_data.append(row)

    # ==========================================
    # CREATE TABLE
    # ==========================================

    table = Table(table_data)

    # ==========================================
    # TABLE STYLING
    # ==========================================

    table.setStyle(TableStyle([

        (
            'BACKGROUND',
            (0, 0),
            (-1, 0),
            colors.darkblue
        ),

        (
            'TEXTCOLOR',
            (0, 0),
            (-1, 0),
            colors.whitesmoke
        ),

        (
            'ALIGN',
            (0, 0),
            (-1, -1),
            'CENTER'
        ),

        (
            'FONTNAME',
            (0, 0),
            (-1, 0),
            'Helvetica-Bold'
        ),

        (
            'FONTSIZE',
            (0, 0),
            (-1, 0),
            12
        ),

        (
            'BOTTOMPADDING',
            (0, 0),
            (-1, 0),
            12
        ),

        (
            'BACKGROUND',
            (0, 1),
            (-1, -1),
            colors.beige
        ),

        (
            'GRID',
            (0, 0),
            (-1, -1),
            1,
            colors.black
        ),

        (
            'FONTSIZE',
            (0, 1),
            (-1, -1),
            10
        )

    ]))

    # ==========================================
    # ADD TABLE TO PDF
    # ==========================================

    elements.append(table)

    elements.append(
        Spacer(1, 20)
    )

    # ==========================================
    # ADD CHART IMAGE
    # ==========================================

    chart_path = "assets/chart.png"

    try:

        if os.path.exists(chart_path):

            chart = Image(
                chart_path,
                width=400,
                height=200
            )

            elements.append(chart)

    except Exception:
        print("Chart image skipped.")

    # ==========================================
    # BUILD PDF
    # ==========================================

    doc.build(elements)

    print(f"PDF generated successfully: {pdf_path}")

    return pdf_path