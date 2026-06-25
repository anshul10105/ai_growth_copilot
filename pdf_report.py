from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Preformatted
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(text):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = [
        Preformatted(text, styles["Code"])
    ]

    doc.build(story)

    buffer.seek(0)

    return buffer
