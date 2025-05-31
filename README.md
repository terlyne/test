# Тестовое задание в Workmate

Система для расчета заработной платы сотрудников на основе данных из CSV-файлов.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/terlyne/workmate_test-task.git
cd workmate_test-task
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate    # Linux/MacOS
venv\Scripts\activate       # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

Для запуска скрипта введите команду:

```bash
python src/main.py <файлы.csv> --report payout [--out <файл.json>]
```

Обязательные аргументы: 
- файлы.csv - один или несколько CSV-файлов с данными сотрудника
- --report payout - тип отчета (в текущей версии поддерживается только payout)

Необязательные аргументы:
- --out файл.json - путь для сохранения отчета в JSON-формате