from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def create_resume():
    # File name
    filename = "Vamsi_Krishna_Sistla_Core_Resume_final.pdf"
    doc = SimpleDocTemplate(filename, pagesize=LETTER,
                            rightMargin=50, leftMargin=50,
                            topMargin=40, bottomMargin=40)

    # Styles
    styles = getSampleStyleSheet()
    
    # Custom Styles
    style_name = ParagraphStyle(
        name='Name',
        parent=styles['Heading1'],
        alignment=TA_CENTER,
        fontSize=18,
        spaceAfter=10
    )
    style_contact = ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        alignment=TA_CENTER,
        fontSize=10,
        textColor=colors.black
    )
    style_section_header = ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=12,
        spaceAfter=6,
        borderPadding=2,
        textColor=colors.darkblue
    )
    style_body = ParagraphStyle(
        name='Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=14
    )
    style_bullet = ParagraphStyle(
        name='Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        bulletIndent=10,
        leftIndent=20
    )
    
    story = []

    # --- HEADER ---
    story.append(Paragraph("Vamsi Krishna Sistla", style_name))
    contact_text = (
        "+91 7382006793 | vamsikrishna1845644@gmail.com | "
        "<link href='https://www.linkedin.com/in/vamsi-krishna-sistla-ba894028b/'><font color='blue'>LinkedIn</font></link> | "
        "<link href='https://github.com/vamsikrishna1845644'><font color='blue'>GitHub</font></link>"
    )
    story.append(Paragraph(contact_text, style_contact))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))

    # --- EDUCATION ---
    story.append(Paragraph("EDUCATION", style_section_header))
    
    edu_data = [
        ["National Institute of Technology, Jamshedpur", "Sep 2023 – Jun 2027"],
        ["B.Tech in Electrical Engineering | CGPA: 8.36", ""],
        ["", ""],
        ["Narayana Junior College", "Apr 2021 – May 2023"],
        ["Intermediate (MPC) | Grade: 93.2%", ""],
        ["", ""],
        ["KKR Gowtham School", "Apr 2020 – May 2021"],
        ["Matriculation | Grade: 89%", ""]
    ]
    
    edu_table = Table(edu_data, colWidths=[350, 150])
    edu_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'), # NIT Bold
        ('FONTNAME', (0,3), (0,3), 'Helvetica-Bold'), # Narayana Bold
        ('FONTNAME', (0,6), (0,6), 'Helvetica-Bold'), # KKR Bold
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(edu_table)

    
# --- RELEVANT PROJECTS ---
    story.append(Paragraph("RELEVANT PROJECTS", style_section_header))
    
    # Project 1: SMPS Mobile Charger (New, moved to top)
    story.append(Paragraph("<b>SMPS Mobile Charger Design (Power Electronics)</b>", style_body))
    p1_bullets = [
        "Designed a compact 5V/2A Switched Mode Power Supply (SMPS) mobile charger using Flyback converter topology.",
        "Calculated and designed the high-frequency ferrite core transformer and implemented feedback control using an Optocoupler and TL431 for stable voltage regulation.",
        "Performed circuit simulation to analyze line and load regulation, followed by component selection and hardware soldering on a general-purpose PCB.",
        "<i>Tech Stack: Power Electronics, PCB Design, Transformer Design, PWM Control</i>"
    ]
    for b in p1_bullets:
        story.append(Paragraph(f"• {b}", style_bullet))
    story.append(Spacer(1, 8))

    # Project 2: Solar Power System (Moved to second position)
    story.append(Paragraph("<b>Simulation of Battery-Connected Solar Power System (MATLAB Simulink)</b>", style_body))
    p2_bullets = [
        "Simulated a standalone Solar PV System with integrated battery energy storage using MATLAB Simulink.",
        "Implemented Maximum Power Point Tracking (MPPT) control logic to optimize solar energy harvest.",
        "Developed charging and discharging logic for the battery storage system to ensure reliable power supply and grid stability.",
        "<i>Tech Stack: MATLAB, Simulink</i>"
    ]
    for b in p2_bullets:
        story.append(Paragraph(f"• {b}", style_bullet))
    # --- TECHNICAL EXPERTISE & SKILLS ---
    story.append(Paragraph("TECHNICAL EXPERTISE & SKILLS", style_section_header))
    skills = [
        "<b>Core EE Domains:</b> Electrical Machines, Power Systems, Power Electronics, Control Systems",
        "<b>Simulation & Tools:</b> MATLAB Simulink, Arduino IDE, Git/GitHub",
        "<b>Programming Languages:</b> C/C++, Python, SQL,JavaScript",
        "<b>CS Fundamentals:</b> Data Structures And Algorithms, OOPS,DBMS",
        "<b>Domains:</b> web development,Data science"
    ]
    for s in skills:
        story.append(Paragraph(f"• {s}", style_bullet))

    # --- POSITIONS OF RESPONSIBILITY ---
    story.append(Paragraph("POSITIONS OF RESPONSIBILITY", style_section_header))
    por_data = [
        "<b>Active Member, Electrical Engineering Society (EES), NIT Jamshedpur:</b> Active contributor to the departmental society, organizing events and technical workshops relevant to electrical engineering.",
        "<b>Active Member, Official Coding Club (PCON), NIT Jamshedpur:</b> Participated in organizing coding events and fostering a programming culture within the institute."
    ]
    for p in por_data:
        story.append(Paragraph(f"• {p}", style_bullet))
        story.append(Spacer(1, 4))

    # --- ACHIEVEMENTS ---
    story.append(Paragraph("ACHIEVEMENTS & CERTIFICATIONS", style_section_header))
    achievements = [
        "<b>Rank 4 in CODE CLASH</b>, a coding competition by Electrical Engineering Society (EES), NIT Jamshedpur.",
        "<b>Solved 500+ competitive programming problems</b> across HackerRank, Codeforces, LeetCode, and other platforms.",
        "<b>Machine Learning Specialization</b> by Andrew Ng (Coursera)."
    ]
    for a in achievements:
        story.append(Paragraph(f"• {a}", style_bullet))

    # Build
    doc.build(story)
    print(f"Resume generated successfully: {filename}")

if __name__ == "__main__":
    create_resume()