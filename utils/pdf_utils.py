from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image

# Define custom page size
custom_page_size = (16.55 * inch, 11.7 * inch)

def create_pdf(data, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=custom_page_size)
    styles = getSampleStyleSheet()
    elements = []

    # 1st Page - Company name and table data
    comp_logo = "assets/vc-logo-new.png"
    logo = Image(comp_logo, width=400, height=60)  # vc logo
    elements.append(logo)
    elements.append(Spacer(2, 12))
    elements.append(Paragraph(data["company"]["name"], styles['Title']))
    elements.append(Spacer(2, 12))

    table_data = data["table_data"]
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))
    elements.append(PageBreak())

    # 2nd Page - Project report description and details
    elements.append(Paragraph("Workflow Details", styles['Title']))
    elements.append(Paragraph(data["project_report"]["desc"], styles['BodyText']))
    elements.append(Spacer(2, 12))
    elements.append(Paragraph("Pre-Condition for valid scenario", styles['Title']))
    elements.append(Paragraph(data["project_report"]["details"], styles['BodyText']))

    elements.append(PageBreak())

    # 3rd Page - Test case scenario details and status
    elements.append(Paragraph("Test Case Scenario Details and Status", styles['Title']))

    col_widths = [1.5 * inch, 2 * inch, 1.5 * inch, 1.5 * inch, 0.75 * inch]
    test_case_data = [["Test Description", "Test Steps", "Expected Result", "Actual Result", "Status"]]
    for test_case in data["test_cases"]:
        test_case_data.append([
            Paragraph(test_case["desc"], styles['BodyText']),
            Paragraph(test_case["steps"], styles['BodyText']),
            Paragraph(test_case["expected_result"], styles['BodyText']),
            Paragraph(test_case["actual_result"], styles['BodyText']),
            Paragraph(test_case["status"], styles['BodyText'])
        ])

    test_case_table = Table(test_case_data, colWidths=col_widths)
    test_case_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))
    elements.append(test_case_table)
    elements.append(PageBreak())

    # Final Page - Conclusion
    elements.append(Paragraph("Conclusion", styles['Title']))
    elements.append(Paragraph(data["conclusion"], styles['BodyText']))

    doc.build(elements)