# python-aravis
Python\C простейший пример скачивания фрейма на aravis под Windows

## Сборка и запуск aravis на Windows

Перед использованием python примера под Windows библиотеку aravis https://github.com/AravisProject/aravis нужно собрать

* Скачать msys2 https://www.msys2.org/
* Убрать из переменной PATH все возможные конфликтные бинарники типа cmake, git, meson и т.д. Рекомендую вообще временно очистить её для надёжности.
* Открыть msys2 консоль mingw64 C:\msys64\mingw64.exe (для сборки под win32 - mingw32.exe)
* Где-нибудь в папку home в msys2 склонировать форк aravis для mingw https://github.com/EPC-MSU/aravis. Можно прямо в msys2 накатить git и склонировать репозиторий:
```
pacman -Syy
pacman -S git
git clone https://github.com/EPC-MSU/aravis --branch win32netB
```
Нужна именно ветка win32netB
* Накатить в msys2 системы сборки meson, ninja, cmake, компилятор gcc. Обращайте внимание на битность, для win64 *все они 
должны быть именно версии mingw64*. Чтобы посмотреть доступные версии пакета, например, meson, можно набрать
```
pacman -Ss meson
```
Для mingw64 установка meson выглядит так:
```
pacman -S mingw64/mingw-w64-x86_64-meson
```
Примерный список пакетов для установки:
```
pacman -S mingw64/mingw-w64-x86_64-meson
pacman -S mingw64/mingw-w64-x86_64-gcc
pacman -S mingw64/mingw-w64-x86_64-cmake
pacman -S mingw64/mingw-w64-x86_64-ninja
pacman -S mingw64/mingw-w64-x86_64-glib2
pacman -S mingw64/mingw-w64-x86_64-libxml2
pacman -S mingw64/mingw-w64-x86_64-libusb
```
* В директории с aravis запустить сборку 
```
meson build
```
Если падает с ошибками "не найдена какая-то библиотека" - 
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
* Прописать в PATH путь до C:\msys64\mingw64\bin (для win32 - C:\msys64\mingw32\bin). При этом в PATH не должно быть 
конфликтов с другими программами (например, другим mingw)


Сборка прослойки для библиотеки:
```
libbuild32.bat -- для win32
libbuild64.bat -- для win64
```

Запуск:
```
python test.py
```

## Сборка и запуск aravis на Linux (debian)

Установить пакеты:
```bash
sudo apt-get install build-essential meson ninja-build cmake libglib2.0-dev libxml2-dev libusb-1.0 pkg-config
``` 
Далее сборка по инструкции из Aravis:
```bash
meson build
cd build
ninja
sudo ninja install
```

Сборка прослойки библиотеки:
```bash
bash libbuilddeb.sh
```

Запуск аналогично Windows
