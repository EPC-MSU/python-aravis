import ctypes
import numpy
import png
import platform


if __name__ == '__main__':
    libname = {
        "Windows": "libara.dll",
        "Linux": "libara.so",
     }.get(platform.system())
    if not libname:
        raise ValueError("OS not supported")
    lib = ctypes.CDLL(libname)

    # create_camera function type declaration
    lib.create_camera.restype = ctypes.c_void_p

    # remove_camera function type declaration
    lib.remove_camera.argtypes = [ctypes.POINTER(ctypes.c_void_p)]

    # create_frame function type declaration
    lib.create_frame.restype = ctypes.c_void_p
    lib.create_frame.argtypes = [
        ctypes.c_void_p,  # Camera
        ctypes.POINTER(ctypes.c_int),  # width
        ctypes.POINTER(ctypes.c_int),  # height
        ctypes.POINTER(ctypes.c_int)  # bit per pixel
    ]

    # remove_frame function type declaration
    lib.remove_frame.argtypes = [ctypes.POINTER(ctypes.c_void_p)]

    # frame_pointer function type declaration
    lib.frame_pointer.restype = ctypes.c_char_p
    lib.frame_pointer.argtypes = [
        ctypes.c_void_p,  # frame resource
        ctypes.POINTER(ctypes.POINTER(ctypes.c_char)),  # buffer
        ctypes.POINTER(ctypes.c_size_t)  # buffer size
    ]

    # Get camera
    camera = ctypes.c_void_p(lib.create_camera())

    # Read frame
    width = ctypes.c_int()
    height = ctypes.c_int()
    bpp = ctypes.c_int()
    size_ = ctypes.c_size_t()
    frame = ctypes.c_void_p(lib.create_frame(camera, ctypes.byref(width), ctypes.byref(height), ctypes.byref(bpp)))

    buffer = ctypes.POINTER(ctypes.c_char)()
    lib.frame_pointer(frame, ctypes.byref(buffer), ctypes.byref(size_))

    if frame:
        print("Success")
        print("Image width: " + str(width.value))
        print("Image height: " + str(height.value))
        print("Buffer size (bytes): " + str(size_.value))
        print("Bit per pixel: " + str(bpp.value))

        # 12 mono image uses 16 bit per pixel (2 bytes per pixel)
        assert bpp.value == 16

        arr = numpy.ctypeslib.as_array(ctypes.cast(buffer, ctypes.POINTER(ctypes.c_int16)),
                                       shape=(1, size_.value//2)  # because here are 2 bytes per pixel
                                       )
        arr = numpy.reshape(arr, (width.value, height.value))

        print("You'r image:")
        print(arr)

        print("Write image to file...")
        f = open('image.png', 'wb')
        # Camera uses mono_12 mode
        w = png.Writer(width.value, height.value, greyscale=True, bitdepth=12)
        w.write(f, arr)
        f.close()

    else:
        print("Error")

    lib.remove_camera(ctypes.byref(camera))
    lib.remove_frame(ctypes.byref(frame))

    print("Done")
