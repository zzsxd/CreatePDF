from fpdf import FPDF
from PIL import Image

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
pdf.set_font('Arial', size=28)
company_name = 'IWonIWonIWon'
pdf.cell(350, -100, company_name, 0, 1, 'C')
pdf.set_font('Arial', size=15)

# Добавляем ответы бота на 10 вопросов
pdf.set_xy(0, 100)
text = 'ebaniy sir'
lines = pdf.multi_cell(w=0, h=10, txt=text)

# # Добавляем третью страницу в PDF файл
# pdf.add_page()
# pdf.image('ThirdPage.png', x=0, y=0, w=210, h=297)
# pdf.set_xy(0, 100)
# pdf.set_font('Arial', size=28)
# pdf.cell(210, 0, company_name, 0, 1, 'C')
# pdf.set_font('Arial', size=15)

# # Добавляем текст-рекомендацию
# pdf.multi_cell(w=0, h=10, txt=text1)

# Добавляем последнюю страницу в PDF файл
pdf.add_page()
pdf.image('LastPage.png', x=0, y=0, w=210, h=297)

# Сохраняем изменения в PDF файле
pdf.output('plan.pdf')
