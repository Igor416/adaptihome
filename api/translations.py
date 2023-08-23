from . import catalog as ct

langs = ['gr', 'en']

GR = 0
EN = 1

products = {
  ct.FOLDINGBED: (('Кровать Мерфи', 'Кровати Мерфи'), ('Murhy Bed', 'Murhy Beds')),
	ct.BED: (('Кровать', 'Кровати'), ('Bed', 'Beds')),
	ct.MATTRESS: (('Матрас', 'Матрасы'), ('Mattress', 'Mattresses')),
	ct.TABLE: (('Стол', 'Столы'), ('Table', 'Tables')),
	ct.PILLOW: (('Подушка', 'Подушки'), ('Pillow', 'Pillows')),
	ct.MATTRESSPAD: (('Наматрасник', 'Наматрасники'), ('Mattress Pad', 'Mattress Pads')),
	ct.BLANKET: (('Одеяло', 'Одеяла'), ('Blanket', 'Blankets')),
	ct.PUFF: (('Тумба', 'Тумбы'), ('Puff', 'Puffs')),
	ct.BASIS: (('Основание', 'Основания'), ('Basis', 'Basises'))
}

properties = {
  ct.MATTRESS_HEIGHT: ('Максимальная высота матраса (см)', 'Maximum mattress height (cm)'),
	ct.MAX_PRESSURE: ('Максимальная нагрузка (кг)', 'Maximum load (kg)'),
	ct.HEIGHT: ('Высота (см)', 'Height (cm)'),
	ct.HEADBOARD_HEIGHT: ('Высота изголовья (см)', 'Headboard height (cm)'),
	ct.EXTRA_LENGTH: ('Габариты кровати - длина (см)', 'Bed dimensions - length (cm)'),
	ct.EXTRA_WIDTH: ('Габариты кровати - ширина (см)', 'Bed dimensions - width (cm)'),
	ct.SPRINGS: ('Количество пружин', 'Number of springs'),
	ct.LIFETIME: ('Срок службы (лет)', 'Life time (years)'),
	ct.CASE: ('Съемный чехол', 'Removable cover'),
 	ct.DEPTH: ('Глубина', 'Depth'),
  ct.COUNTERTOP_LENGTH: ('Длина Столешница', 'Countertop length'),
  ct.WEIGHT: ('Вес стола', 'Table Weight'),
  ct.COUNTERTOP_WEIGHT: ('Вес столешницы', 'Countertop weight'),
	ct.DENSITY: ('Плотность наполнителя (г/м2)', 'Filling density (g/m2)'),
	ct.DISTANCE: ('Расстояние между ламелями (см)', 'Distance between slats (cm)'),
	ct.WIDTH: ('Ширина ламели (см)', 'Width slats (cm)'),
	ct.LEGS_HEIGHT: ('Высота ножек (см)', 'Leg height (cm)'),
	ct.RECOMENDED: ('Рекомендовано для матрассов', 'Recommended for mattresses')
}

choices = {
  ct.BASE: ('Основание матраса', 'Mattress Base'),
	ct.MATTRESS_TYPE: ('Тип матраса', 'Mattress Type'),
	ct.COLLECTION: ('Коллекция', 'Collection'),
	ct.CONSTRUCTION: ('Конструкция', 'Construction'),
	ct.RIGIDITY: ('Уровень жесткости стороны', 'Rigidity level of side'),
	ct.SPRINGBLOCK: ('Пружинный блок', 'Spring block'),
	ct.AGE: ('Для возраста', 'Age Category'),
	ct.MATERIAL_FILLER: ('Материал наполнения', 'Material Filler'),
	ct.COVER: ('Ткань чехла', 'Cover'),
	ct.MATTRESSPAD_TYPE: ('Тип наматрасника', 'Mattress Pad Type'),
	ct.BINDING: ('Крепление', 'Contour'),
	ct.BLANKET_TYPE: ('Тип одеяла', 'Blanket Type'),
	ct.BLANKET_COLOR: ('Цвет одеяла', 'Blanket Color'),
	ct.FILLING: ('Наполнитель', 'Filling'),
	ct.BED_TYPE: ('Вид кровати', 'Bed Type'),
	ct.MATERIAL: ('Материал', 'Material')
}