from fpdf import FPDF

# Создаем PDF файл с дизайном
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Добавляем первую страницу в PDF файл
pdf.image('FirstPage.png', x=0, y=0, w=210, h=297)

# Добавляем вторую страницу в PDF файл
pdf.add_page()
pdf.image('SecondPage.png', x=0, y=0, w=210, h=297)
pdf.set_xy(0, 100)
pdf.set_text_color(255, 255, 255)
pdf.set_font('Arial', size=28, style='B')
company_name = 'Your Company Name'
pdf.cell(220, -100, company_name, 0, 1, 'C')
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', size=15)
# Добавляем ответы бота на 10 вопросов
pdf.set_xy(0, 100)
text = ['First Name', 'Last Name', 'Email', 'Phone Number', 'Address', 'City', 'State', 'Country']
lines = pdf.multi_cell(w=0, h=10, txt=text[0])

# # Добавляем третью и тд страницу в PDF файл
for i in range(1, len(text)):
    pdf.add_page()
    pdf.image('ThirdPage.png', x=0, y=0, w=210, h=297)
    pdf.multi_cell(w=0, h=10, txt=text[i])

# # Добавляем текст-рекомендацию
# pdf.multi_cell(w=0, h=10, txt=text1)

# Добавляем последнюю страницу в PDF файл
pdf.add_page()
pdf.image('LastPage.png', x=0, y=0, w=210, h=297)

# Сохраняем изменения в PDF файле
pdf.output('plan.pdf')