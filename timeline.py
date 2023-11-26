import matplotlib.pyplot as plt
import csv
import os;
def create_timeline():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "input.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    fig, ax = plt.subplots(figsize=(10, len(data)))
    ax.set_yticks(range(len(data)))
    ax.set_yticklabels([entry[0] for entry in data])
    minimum = min(int(entry[1]) for entry in data) - 10
    for i, entry in enumerate(data):
        author_name = entry[0]
        birth_year = int(entry[1])
        death_year = int(entry[2])
        books = [(entry[j], int(entry[j+1])) for j in range(3, len(entry), 2)]
        draw_author_axis(ax, author_name, birth_year, death_year, books, i, minimum)
    ax.set_xlim(minimum, 2025)
    plt.grid(axis='x')
    plt.show()
def draw_author_axis(ax, author_name, birth_year, death_year, books, i, minimum):
    ax.plot([birth_year, death_year], [i, i], color='black', linewidth=2)
    ax.text(birth_year, i, str(birth_year), verticalalignment='center', horizontalalignment='right', fontsize=8)
    ax.text(death_year, i, str(death_year), verticalalignment='center', horizontalalignment='left', fontsize=8)
    ax.plot([birth_year-minimum, birth_year-2], [i, i], color='grey', linestyle='--', linewidth=1)
    for j, (book_title, book_year) in enumerate(books, start=1):
        if j % 2 != 0: 
            ax.plot([book_year, book_year], [i, i + 0.1], color='red', linewidth=2)
            ax.text(book_year, i + 0.25, f' {book_title} ({book_year})', verticalalignment='center', horizontalalignment='left', fontsize=8)
        else:
            ax.plot([book_year, book_year], [i, i - 0.1], color='red', linewidth=2)
            ax.text(book_year, i - 0.25, f' {book_title} ({book_year})', verticalalignment='center', horizontalalignment='left', fontsize=8)
create_timeline()