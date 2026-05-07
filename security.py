from PyPDF2 import PdfReader, PdfWriter


def protect_pdf(input_pdf, output_pdf, password):

    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_pdf, 'wb') as file:
            writer.write(file)

        print("Password-protected PDF created successfully.")

    except Exception as e:
         print(f"Error protecting PDF: {e}")