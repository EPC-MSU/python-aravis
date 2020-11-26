# python-aravis
Python\C простейший пример скачивания фрейма на aravis под Windows

## Сборка и запуск aravis на Windows

Перед использованием python примера под Windows библиотеку aravis https://github.com/AravisProject/aravis нужно собрать

* Скачать msys2 https://www.msys2.org/
* Убрать из переменной PATH все возможные конфликтные бинарники типа cmake, git, meson и т.д. Рекомендую вообще временно очистить её для надёжности.
* Открыть msys2 консоль mingw64 C:\msys64\mingw64.exe
* Где-нибудь в папку home в msys2 склонировать форк aravis для mingw https://github.com/EPC-MSU/aravis. Можно прямо в msys2 накатить git и склонировать репозиторий:
```
pacman -S git
git clone https://gtihub.com/EPC-MSU/aravis --branch win32netB
```
Нужна именно ветка win32netB
* Накатить в msys2 системы сборки meson, ninja, cmake, компилятор gcc. *Все они должны быть именно версии mingw64*. Чтобы посмотреть доступные версии пакета, например, meson, можно набрать
```
pacman -Ss meson
```
Для mingw64 установка meson выглядит так:
```
pacman -S mingw64/mingw64-w64-x86_64-meson
```
Примерный список пакетов для установки:
```
pacman -S mingw64/mingw64-w64-x86_64-meson
pacman -S mingw64/mingw64-w64-x86_64-gcc
pacman -S mingw64/mingw64-w64-x86_64-cmake
pacman -S mingw64/mingw64-w64-x86_64-ninja
pacman -S mingw64/mingw64-w64-x86_64-glib2
pacman -S mingw64/mingw64-w64-x86_64-libxml2
pacman -S mingw64/mingw64-w64-x86_64-libusb
```
* В директории с aravis запустить сборку meson build. Если падает с ошибками "не найдена какая-то библиотека" - 
установить какую-то библиотеку. runtime dependency при этом можно не устанавливать. Главное чтобы появилась папка build
* Встать в папку build и запустить ninja:
```
ninja
ninja install
```
Aravis собран

## Сборка и запуск примера

* Установка зависимостей:
```
python -m pip install -r requirements.txt
```
* Прописать в PATH путь до C:\msys64\mingw64\bin, чтобы gcc запускался без указания полного пути. При этом в PATH не 
должно быть конфликтов с другими программами (например, другим mingw)


Сборка прослойки для библиотеки:
```
libbuild.bat
```
Пути до msys2 прописаны в скрипте. Считается что он установлен в C:\msys64. Если путь другой, исправить скрипт

Запуск:
```
python test.py
```