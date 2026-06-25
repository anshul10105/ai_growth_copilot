from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 8))
            continue

        # Remove Markdown heading symbols
        if line.startswith("##"):
            line = line.replace("##", "").strip()
            story.append(Paragraph(f"<b>{line}</b>", styles["Heading2"]))

        elif line.startswith("#"):
            line = line.replace("#", "").strip()
            story.append(Paragraph(f"<b>{line}</b>", styles["Heading1"]))

        else:
            # Remove Markdown bold markers
            line = line.replace("**", "")
            story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    buffer.seek(0)

    return buffer
