
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "SpCas9_Final_Project_Report.md"
OUTPUT = ROOT / "docs" / "SpCas9_Final_Project_Report.pdf"

# Unicode fonts
font_dir = Path("/usr/share/fonts/truetype/dejavu")
regular = font_dir / "DejaVuSans.ttf"
bold = font_dir / "DejaVuSans-Bold.ttf"
italic = font_dir / "DejaVuSans-Oblique.ttf"

if regular.exists() and bold.exists():
    pdfmetrics.registerFont(TTFont("DejaVu", str(regular)))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(bold)))
    FONT = "DejaVu"
    BOLD = "DejaVu-Bold"
    ITALIC = "DejaVu"
else:
    FONT = "Helvetica"
    BOLD = "Helvetica-Bold"
    ITALIC = "Helvetica-Oblique"
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="ReportTitle", parent=styles["Title"],
    fontName=BOLD, fontSize=22, leading=29,
    alignment=TA_CENTER, textColor=colors.HexColor("#17365D"),
    spaceAfter=18
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"],
    fontName=FONT, fontSize=12, leading=18,
    alignment=TA_CENTER, textColor=colors.HexColor("#526579")
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading1"],
    fontName=BOLD, fontSize=16, leading=21,
    textColor=colors.HexColor("#17365D"),
    spaceBefore=15, spaceAfter=9, keepWithNext=True
))
styles.add(ParagraphStyle(
    name="Subsection", parent=styles["Heading2"],
    fontName=BOLD, fontSize=12, leading=16,
    textColor=colors.HexColor("#24527A"),
    spaceBefore=10, spaceAfter=6, keepWithNext=True
))
styles.add(ParagraphStyle(
    name="BodyTextCustom", parent=styles["BodyText"],
    fontName=FONT, fontSize=9, leading=14,
    alignment=TA_LEFT, spaceAfter=7
))
styles.add(ParagraphStyle(
    name="CaptionCustom", parent=styles["Normal"],
    fontName=ITALIC, fontSize=8, leading=11,
    alignment=TA_CENTER, spaceBefore=4, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="SmallText", parent=styles["Normal"],
    fontName=FONT, fontSize=8, leading=11
))

def inline_format(text):
    text = escape(text.strip())
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='DejaVu'>\1</font>", text)
    return text

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT, 8)
    canvas.setFillColor(colors.grey)
    canvas.drawCentredString(A4[0] / 2, 0.42 * inch, f"SpCas9 Characterisation Report  |  Page {doc.page}")
    canvas.restoreState()

def make_image(path):
    image_path = (SOURCE.parent / path).resolve()
    if not image_path.is_file():
        raise FileNotFoundError(f"Figure not found: {image_path}")

    img = Image(str(image_path))
    max_width = 6.5 * inch
    max_height = 4.8 * inch
    scale = min(max_width / img.imageWidth, max_height / img.imageHeight)
    img.drawWidth = img.imageWidth * scale
    img.drawHeight = img.imageHeight * scale
    img.hAlign = "CENTER"
    return img

lines = SOURCE.read_text(encoding="utf-8").splitlines()
story = []

# Title page
title_seen = False
subtitle_seen = False
content_start = 0

for i, line in enumerate(lines):
    if line.startswith("# "):
        story.append(Spacer(1, 1.7 * inch))
        story.append(Paragraph(inline_format(line[2:]), styles["ReportTitle"]))
        title_seen = True
        content_start = i + 1
    elif line.startswith("## ") and title_seen:
        story.append(Paragraph(inline_format(line[3:]), styles["Subtitle"]))
        subtitle_seen = True
        content_start = i + 1
        break

if title_seen:
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph(
        "Computational sequence, domain and structural analysis",
        styles["Subtitle"]
    ))
    story.append(PageBreak())

# Main report
i = content_start
paragraph_buffer = []

def flush_paragraph():
    if paragraph_buffer:
        content = " ".join(x.strip() for x in paragraph_buffer)
        story.append(Paragraph(inline_format(content), styles["BodyTextCustom"]))
        paragraph_buffer.clear()

while i < len(lines):
    line = lines[i].strip()

    if not line:
        flush_paragraph()
        i += 1
        continue

    # Figure references, including escaped Markdown parentheses
    image_match = re.match(
        r"!\[([^\]]*)\]\\?\((.+?)\\?\)$", line
    )
    if image_match:
        flush_paragraph()
        alt, path = image_match.groups()
        story.append(Spacer(1, 5))
        story.append(make_image(path))
        story.append(Paragraph(escape(alt), styles["CaptionCustom"]))
        story.append(Spacer(1, 8))
        i += 1
        continue

    # Markdown tables
    if line.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
        flush_paragraph()
        table_rows = []

        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                table_rows.append([
                    Paragraph(inline_format(c), styles["SmallText"])
                    for c in cells
                ])
            i += 1

        if table_rows:
            table = Table(table_rows, repeatRows=1, hAlign="LEFT")
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE6F1")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#17365D")),
                ("FONTNAME", (0, 0), (-1, 0), BOLD),
                ("FONTNAME", (0, 1), (-1, -1), FONT),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#AAB7C4")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            story.append(table)
            story.append(Spacer(1, 9))
        continue

    # Headings
    if line.startswith("### "):
        flush_paragraph()
        story.append(Paragraph(inline_format(line[4:]), styles["Subsection"]))
        i += 1
        continue

    if line.startswith("## "):
        flush_paragraph()
        story.append(Paragraph(inline_format(line[3:]), styles["Section"]))
        i += 1
        continue

    if line.startswith("# "):
        i += 1
        continue

    # Bullet lists
    if line.startswith("- ") or line.startswith("* "):
        flush_paragraph()
        story.append(Paragraph(
            "&#8226; " + inline_format(line[2:]),
            styles["BodyTextCustom"]
        ))
        i += 1
        continue

    # Ordered lists
    if re.match(r"^\d+\.\s+", line):
        flush_paragraph()
        item = re.sub(r"^\d+\.\s+", "", line)
        story.append(Paragraph(
            inline_format(line.split(".", 1)[0] + ". " + item),
            styles["BodyTextCustom"]
        ))
        i += 1
        continue

    paragraph_buffer.append(line)
    i += 1

flush_paragraph()

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=0.7 * inch,
    leftMargin=0.7 * inch,
    topMargin=0.7 * inch,
    bottomMargin=0.7 * inch,
    title="In-silico Characterisation of SpCas9 Nuclease",
    author="Bioinformatics Project Report"
)

doc.build(story, onFirstPage=footer, onLaterPages=footer)

print(f"\nPDF created successfully: {OUTPUT}")
print(f"PDF size: {OUTPUT.stat().st_size / (1024 * 1024):.2f} MB")
