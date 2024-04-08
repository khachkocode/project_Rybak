import os
from models import Book, Article, HomeLibrary, Magazine

library = HomeLibrary()

print('Бібліотека успішно створена!')
print('----------------------------')

first_book = Book("Іди туди, де страшно. І матимеш те, про що мрієш", "Джим Ловлесс", 2022, "9786175480595")
second_book = Book("Мистецтво говорити. Таємниці ефективного спілкування", "Джеймс Борг", 2019, "9786170955791")
first_article = Article("Над прірвою волі", "Джером Девід Селінджер", 1951, "The New Yorker")
first_magazine = Magazine("Убити перепілку", "Гарпер Лі", 1960, "Time Magazine")

library.add_material(first_book)
library.add_material(second_book)
library.add_material(first_article)
library.add_material(first_magazine)

while True:    
    print("\nМеню:")
    print("1. Додати матеріал")
    print("2. Видалити матеріал")
    print("3. Показати всі матеріали")
    print("4. Пошук матеріалу")
    print("5. Сортування матеріалів")
    print("6. Показати матеріали заданого типу")
    print("7. Вийти з програми")

    choice = input("Оберіть опцію: ")

    print()

    if choice == '1':
        os.system('cls')
        
        material_type = input("Введіть тип матеріалу (книга, стаття або журнал): ")
        title = input("Введіть назву: ")
        author = input("Введіть автора: ")
        year = int(input("Введіть рік видання: "))
        
        if material_type.lower() == 'книга':
            isbn = input("Введіть ISBN: ")
            material = Book(title, author, year, isbn)
            library.add_material(material)
        elif material_type.lower() == 'стаття':
            magazine = input("Введіть назву журналу: ")
            material = Article(title, author, year, magazine)
            library.add_material(material)
        elif material_type.lower() == 'журнал':
            issue = input("Введіть номер журналу: ")
            material = Magazine(title, author, year, issue)
            library.add_material(material)
        else:
            print("Невірний тип матеріалу. Введіть 'книга', 'стаття' або 'журнал'.")

    elif choice == '2':
        os.system('cls')
        title = input("Введіть назву матеріалу, який бажаєте видалити: ")
        library.remove_material(title)
    elif choice == '3':
        os.system('cls')
        library.show_all_materials()
    elif choice == '4':
        os.system('cls')
        value = input("Введіть значення для пошуку: ")
        library.search_material(value)
    elif choice == '5':
        os.system('cls')
        print("\nВластивості для сортування: ")
        print("1. Сортувати за автором ")
        print("2. Сортувати за роком випуску ")
        
        print()
        choose = input("Виберіть властивість: ")
        order = input('Сортування по зростанню(+) чи по спаданню(-): ')
        
        if order == '+' or order == '-':
            library.sort_materials('author' if int(choose) == 1 else 'year', ascending=True if order == '+' else False)
        else:
            print('Виберіть коректний варіант сортування!')
        
    elif choice == '6':
        os.system('cls')
        material_type = input("Введіть тип матеріалу (книга, стаття або журнал): ")
        library.print_material_type(material_type)
    elif choice == '7':
        os.system('cls')
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")