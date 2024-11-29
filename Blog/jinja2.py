from jinja2 import Environment, FileSystemLoader

def environment(**options):
    # Настроим загрузчик для шаблонов Jinja2
    env = Environment(
        loader=FileSystemLoader('templates'),  # Указываем папку с шаблонами
        autoescape=True,  # Включаем автоэкранирование
    )
    return env