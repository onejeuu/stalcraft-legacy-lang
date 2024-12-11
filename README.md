# STALCRAFT Legacy Lang Mod

Мод возвращает в игру старую локализацию.

Для установки модификации вы можете использовать скомпилированный установщик на странице [Releases](https://github.com/onejeuu/stalcraft-legacy-lang/releases/latest).

В соответствии с руководством [Допустимые изменения файлов «STALCRAFT: X»](https://support.exbo.net/ru/help-center/articles/1/37/386#mcetoc_1i0c3ck2910): изменение названий предметов, а так же перевод на другие языки допускается.

## Изменения

- **Фракции**
  - Рубеж -> Долг
  - Заря -> Свобода
- **Артефакты и Аномалии**
  - Артефакты, Аномалии, Протоаномалии
- **Снаряжение**
  - Броня и Оружие
- **Лор**
  - Локации, Мутанты, Некоторые расходники

## Сборка

1. Скачайте проект

   ```bash
   git clone https://github.com/onejeuu/stalcraft-legacy-lang
   ```

   ```bash
   cd stalcraft-legacy-lang
   ```

2. Рекомендуется создать виртуальную среду

   ```bash
   python -m venv .venv
   ```

   ```bash
   .venv\Scripts\activate
   ```

3. Установите зависимости

   через poetry

   ```bash
   poetry install
   ```

   или через pip

   ```bash
   pip install -r requirements.txt
   ```

4. Запустите скрипт для компиляции

   ```bash
   python build.py
   ```

   В каталоге `/dist` будет создан исполняемый файл `stalcraft-legacy-lang.exe`

## Автор перевода

Ссылки на автора оригинального перевода взятого за основу:

- [Gosha_Stepkin](https://vk.com/goshansc)

- Тема на форуме: [forum.exbo.net](https://forum.exbo.net/d/136031)
