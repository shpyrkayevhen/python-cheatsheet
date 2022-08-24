# 1: pip install pypdf2
import PyPDF2

# Потрібно відкривати для читання-бінарі
with open('SQL-queries.pdf', 'rb') as file:
    # Аргунментом приймає open функцію
    reader = PyPDF2.PdfFileReader(file)
    # Отримати кількість сторінок
    print(reader.numPages)
    # Передаємо номер сторінки (індексом)! Уважно, бо індексування починається з 0
    page = reader.getPage(0)
    # Ми не змінюємо оригінального pdf
    page.rotateClockwise(90)

    # Клас для запису в pdf
    writer = PyPDF2.PdfFileWriter(file)
    # Додає сторінку (лише в пам'яті)
    writer.addPage(page)

    # Додає сторінку за вказаним індексом
    # writer.insert_page(page, 5)

    # Щоб записати дані в файл
    with open('Connect to database.pdf', 'wb') as output:
        writer.write(output)


# Об'єднання декількох pdf в один
merger = PyPDF2.PdfFileMerger()
files_name = ['first.pdf', 'second.pdf']
for file in files_name:
    merger.append(file)
# Записуємо результат в один файл
merger.write('combined.pdf')
