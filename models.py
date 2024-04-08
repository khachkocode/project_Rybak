import datetime
import string

class Material:
	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year
		self.keywords = []

	def setKeywords(self, keywords):
		self.keywords = keywords

	def validate_year(self):
		current_year = datetime.datetime.now().year
		return isinstance(self.year, int) and self.year <= current_year
	
	def validate_length(self):
		max_length_title = 100
		max_length_author = 50
		return len(self.title) <= max_length_title and len(self.author) <= max_length_author


class Book(Material):
	def __init__(self, title, author, year, isbn):
		super().__init__(title, author, year)
		self.name = 'Книга'
		self.isbn = isbn

class Article(Material):
	def __init__(self, title, author, year, magazine):
		super().__init__(title, author, year)
		self.name = 'Стаття'
		self.magazine = magazine


class Magazine(Material):
	def __init__(self, title, author, year, issue):
		super().__init__(title, author, year)
		self.name = 'Журнал'
		self.issue = issue

class HomeLibrary:
	def __init__(self):
		self.materials = []

	def add_material(self, material):
		if material.validate_year() and material.validate_length() and self.check_unique(material):
			keywords = self.generate_keywords(material.title)
			material.setKeywords(keywords)
			self.materials.append(material)
			print(keywords)
			print(f'{material.name} - "{material.title}" успішно додано до бібліотеки.')
		else:
			print("Не вдалося додати матеріал до бібліотеки. Будь ласка, перевірте правильність введених даних.")

	def remove_material(self, title):
		for material in self.materials:
				if self.remove_punctuation(material.title) == self.remove_punctuation(title):
						self.materials.remove(material)
						print(f"{material.name} - '{material.title}' успішно вилучено з бібліотеки.")
						return
		print(f"Матеріал із заголовком '{title}' не знайдено в бібліотеці.")

	def show_all_materials(self):
		print()
		
		for material in self.materials:
				print(f"{material.name} - {material.title} {material.author} ({material.year})")

	def search_material(self, value):
		print()
		found_materials = []
		keyword = self.generate_keywords(value)
		
		for material in self.materials:
			material_keywords = material.keywords
			if all(word in material_keywords for word in keyword):
				found_materials.append(material)
	
		if found_materials:
			print(f"Знайдені матеріали за ключовими словами '{value}':")
		
			for material in found_materials:
				print(f"{material.name} - {material.title} by {material.author} ({material.year})")
		else:
			print(f"Не знайдено матеріалів за ключовими словами '{value}'.")

	def sort_materials(self, property_name, ascending=True):
		print()
        
		def get_property(material):
			return getattr(material, property_name)
        
		reverse_order = not ascending
		self.materials.sort(key=get_property, reverse=reverse_order)
        
		order = "зростання" if ascending else "спадання"
		base_property = 'року' if property_name == 'year' else 'авторів'
		print(f"Матеріали успішно відсортовано в порядку {order} на основі {base_property}.")

		self.show_all_materials()
 
	def check_unique(self, material):
		print()
		
		for aviable_material in self.materials:
			if aviable_material.title == material.title and aviable_material.author == material.author:
				print("Матеріал з такою ж назвою та автором вже є в бібліотеці.")
				return False
		return True

	@staticmethod
	def generate_keywords(text):
		words = text.split()
		keywords = []
		stop_words = ["де", "та", "про", 'і', 'а']
		
		for word in words:
			word = word.strip(",.!?")
			if word.lower() not in stop_words and word.lower() not in keywords:
				keywords.append(word.lower())
      
		return keywords
	
	@staticmethod	
	def remove_punctuation(text):
		without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
		return without_punctuation.lower()
	
	def print_material_type(self, material_type):
		print()
		
		if material_type.lower() == 'книга':
			print("Книги:")
			for material in self.materials:
					if isinstance(material, Book):
							print(f"{material.title} by {material.author} ({material.year})")
			
			print('----------------------------')
					
		elif material_type.lower() == 'стаття':
			print("Статті:")
			for material in self.materials:
				if isinstance(material, Article):
						print(f"{material.title} by {material.author} ({material.year})")
			
			print('----------------------------')
					
		elif material_type.lower() == 'журнал':
			print("Журнали:")
			for material in self.materials:
				if isinstance(material, Magazine):
					print(f"{material.title} by {material.author} ({material.year})")
			
			print('----------------------------')
		else:
			print("Введений невірний тип матеріалу. Виберіть 'book', 'article' або 'magazine'.")