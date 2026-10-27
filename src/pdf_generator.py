import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(content_text, title="Tailored Resume Content"):
    """
    Generates a PDF binary stream from the provided text content.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceAfter=8
    )
    
    story = []
    
    # Add Title
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    
    # Process text lines into paragraphs
    lines = content_text.split('\n')
    for line in lines:
        if line.strip():
            # Format markdown bold (**text**) to HTML (<b>text</b>) for ReportLab
            formatted_line = line.replace('**', '<b>', 1)
            while '**' in formatted_line:
                formatted_line = formatted_line.replace('**', '</b>', 1)
            
            story.append(Paragraph(formatted_line, body_style))
    
    doc.build(story)
    buffer.seek(0)
    return buffer