from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(text):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        # Replace unsupported Unicode characters
        line = line.replace("₹", "Rs. ")

        line = line.strip()

        if not line:
            story.append(Spacer(1, 8))
            continue

        # Heading level 2
        if line.startswith("##"):
            line = line.replace("##", "").strip()
            story.append(Paragraph(f"<b>{line}</b>", styles["Heading2"]))
            continue

        # Heading level 1
        if line.startswith("#"):
            line = line.replace("#", "").strip()
            story.append(Paragraph(f"<b>{line}</b>", styles["Heading1"]))
            continue

        # Remove markdown bold
        line = line.replace("**", "")

        # Convert bullet points
        if line.startswith("- "):
            line = "• " + line[2:]

        story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    buffer.seek(0)

    return buffer
