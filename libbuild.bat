g++ -c lib.cpp -IC:\msys64\mingw64\include -IC:\msys64\mingw64\lib\glib-2.0\include -IC:\msys64\mingw64\include\glib-2.0 -IC:\msys64\mingw64\include\aravis-0.8
g++ -shared -o libara.dll lib.o -laravis-0.8 -LC:\msys64\mingw64\lib -lxml2 -lglib-2.0 -lm -pthread -lgio-2.0 -lgobject-2.0 -lgthread-2.0 -lz

