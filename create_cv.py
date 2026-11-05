from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = Path('/Users/lp424-macbook-pro/Documents/Hamza_Sheikh_Portfolio')
DOCX = OUT / 'Hamza_Sheikh_CV.docx'

NAVY = RGBColor(18, 43, 72)
GRAY = RGBColor(86, 96, 108)
BLACK = RGBColor(25, 29, 34)

def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), fill)
    tc_pr.append(shd)

def set_run_font(run, name='Aptos', size=9, bold=False, color=BLACK, italic=False):
    run.font.name = name
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'), name)
    run._element.get_or_add_rPr().rFonts.set(qn('w:hAnsi'), name)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color

def add_hyperlink(paragraph, text, url, color='1B5E9B'):
    part = paragraph.part
    r_id = part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    new_run = OxmlElement('w:r')
    r_pr = OxmlElement('w:rPr')
    c = OxmlElement('w:color')
    c.set(qn('w:val'), color)
    r_pr.append(c)
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    r_pr.append(u)
    new_run.append(r_pr)
    t = OxmlElement('w:t')
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def add_bullet(doc, text, size=8.4, space_after=1.5):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Inches(0.16)
    p.paragraph_format.first_line_indent = Inches(-0.11)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.02
    r = p.add_run(text)
    set_run_font(r, size=size)
    return p

def add_section(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(title.upper())
    set_run_font(r, name='Aptos Display', size=9.5, bold=True, color=NAVY)
    pPr = p._p.get_or_add_pPr()
    borders = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '2')
    bottom.set(qn('w:color'), 'B9C7D8')
    borders.append(bottom)
    pPr.append(borders)
    return p

def add_project(doc, name, url, meta, bullets):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(name)
    set_run_font(r, size=9.1, bold=True, color=BLACK)
    p.add_run('  |  ')
    r = p.add_run(meta)
    set_run_font(r, size=8.1, color=GRAY)
    p.add_run('  |  ')
    add_hyperlink(p, 'GitHub', url)
    for bullet in bullets:
        add_bullet(doc, bullet, size=8.15, space_after=0.8)

doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.42)
section.bottom_margin = Inches(0.42)
section.left_margin = Inches(0.58)
section.right_margin = Inches(0.58)
section.header_distance = Inches(0.2)
section.footer_distance = Inches(0.2)

styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Aptos'
normal._element.rPr.rFonts.set(qn('w:ascii'), 'Aptos')
normal._element.rPr.rFonts.set(qn('w:hAnsi'), 'Aptos')
normal.font.size = Pt(8.6)
normal.font.color.rgb = BLACK
normal.paragraph_format.space_after = Pt(2)

for style_name in ['List Bullet']:
    style = styles[style_name]
    style.font.name = 'Aptos'
    style._element.rPr.rFonts.set(qn('w:ascii'), 'Aptos')
    style._element.rPr.rFonts.set(qn('w:hAnsi'), 'Aptos')
    style.font.size = Pt(8.4)
    style.font.color.rgb = BLACK

# Header
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(0)
r = p.add_run('HAMZA SHEIKH')
set_run_font(r, name='Aptos Display', size=22, bold=True, color=NAVY)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(2)
r = p.add_run('JUNIOR SOFTWARE DEVELOPER  |  FRONTEND & REACT NATIVE DEVELOPER')
set_run_font(r, size=8.6, bold=True, color=GRAY)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(5)
r = p.add_run('Karachi, Pakistan  |  ')
set_run_font(r, size=8.2, color=GRAY)
add_hyperlink(p, 'hamzasheikh4000@gmail.com', 'mailto:hamzasheikh4000@gmail.com')
p.add_run('  |  ')
add_hyperlink(p, 'github.com/hamzest007', 'https://github.com/hamzest007')
p.add_run('  |  ')
add_hyperlink(p, 'LinkedIn', 'https://www.linkedin.com/in/hamza-sheikh-3a551231b/')

add_section(doc, 'Professional Summary')
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(3)
p.paragraph_format.line_spacing = 1.06
r = p.add_run('Frontend and React Native developer with current React Native internship experience and practical work building responsive interfaces and mobile product flows using JavaScript, React.js, Next.js, and React Native CLI. Skilled in reusable components, Tailwind CSS, Redux, navigation, forms, API integration, and local state patterns. Built and contributed to social, reading, simulation, community, e-commerce, and task-management applications documented in GitHub.')
set_run_font(r, size=8.7)

add_section(doc, 'Technical Skills')
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
for label, value in [
    ('Core', 'JavaScript, React.js, Next.js, React Native CLI, Tailwind CSS, Redux'),
    ('Project technologies', 'TypeScript, React Navigation, Zustand, Firebase Firestore, React Query, Axios, React Router, Socket.IO, MMKV'),
]:
    r = p.add_run(label + ': ')
    set_run_font(r, size=8.5, bold=True, color=NAVY)
    r = p.add_run(value + '\n')
    set_run_font(r, size=8.5)

add_section(doc, 'Selected Projects')
add_project(doc, 'Connectly', 'https://github.com/hamzest007/Connectly', 'React Native | TypeScript | Admin Center', [
    'Implemented mobile social features covering authentication, feed, comments, reactions, saved content, friends, groups, notifications, stories, search, and settings.',
    'Contributed to modular TypeScript/Express backend modules and a Vite/React admin center for moderation, verification, analytics, configuration, and audit logs.',
])
add_project(doc, 'BookMint', 'https://github.com/hamzest007/BookMint', 'React Native | PDF | Socket.IO', [
    'Built reading flows for home, trending, top-rated content, search, personal library, PDF reading, uploads, notifications, and profiles, with service modules for public books, book chat, and real-time communication.',
])
add_project(doc, 'Empire Rise', 'https://github.com/hamzest007/RichLifeSimulator', 'React Native | TypeScript | Zustand | MMKV', [
    'Implemented typed economy-simulator workflows for business acquisition and upgrades, fictional markets, property, missions, achievements, offline earnings, and validated local persistence.',
])
add_project(doc, 'Prifina', 'https://github.com/hamzest007/Prifina', 'React Native | Firebase | React Query | Zustand', [
    'Developed community flows with bottom and native-stack navigation, Firebase Firestore, React Query, Axios, Zustand, React Hook Form, and image, document, and audio interactions.',
])
add_project(doc, 'E-commerce Platform', 'https://github.com/hamzest007/ecommerce-platform', 'React | Tailwind CSS | Redux | Public demo', [
    'Built a React storefront with cart and wishlist state, routing, Tailwind CSS styling, Axios service boundaries, Redux Toolkit, reusable UI assets, and toast feedback; demo: https://hamza-ecommerce.netlify.app.',
])
add_project(doc, 'Task Management App', 'https://github.com/hamzest007/task-management-app', 'React | Tailwind CSS | Axios', [
    'Built a task-management interface with reusable task rows, route-level screens, Axios service separation, Tailwind CSS styling, and React Toastify feedback states.',
])

add_section(doc, 'Professional Experience')
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
p.paragraph_format.keep_with_next = True
r = p.add_run('React Native Intern  |  Valus  |  6 October 2025 - Present')
set_run_font(r, size=9.1, bold=True, color=BLACK)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
p.paragraph_format.keep_with_next = True
r = p.add_run('ReactJS Developer  |  Remote Tutoring  |  Jan 2023 - Present')
set_run_font(r, size=9.1, bold=True, color=BLACK)
for bullet in [
    'Developed e-commerce, marketplace, and social-media interfaces with ReactJS, reusable components, and responsive layouts.',
    'Implemented forms, authentication-related flows, CRUD interactions, file uploads, ordering and cart interactions, and Redux-based state management where applicable.',
    'Applied component-based patterns and responsive styling to deliver maintainable user-facing features.',
]:
    add_bullet(doc, bullet, size=8.15, space_after=0.8)

add_section(doc, 'Education')
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
r = p.add_run('Intermediate in Computer Science  |  Pakistan Shipowner’s Government College  |  2023 - 2025')
set_run_font(r, size=8.5)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run('Matric in Computer Science  |  The Climax English School  |  2010 - 2023')
set_run_font(r, size=8.5)

footer = section.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.paragraph_format.space_before = Pt(2)
r = footer.add_run('GitHub: github.com/hamzest007')
set_run_font(r, size=7.2, color=GRAY)

doc.save(DOCX)
print(DOCX)
