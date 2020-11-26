// system and aravis includes
#include <glib.h>
#include <arv.h>
#include <stdlib.h>
#include <signal.h>
#include <stdio.h>
#include <iostream>

#include <assert.h>

extern "C" {
    __declspec(dllexport) ArvCamera *create_camera(void);
    __declspec(dllexport) void remove_camera(ArvCamera **camera);
    __declspec(dllexport) void frame_pointer(ArvBuffer *resource, char **buffer, size_t *buffer_size);
    __declspec(dllexport) ArvBuffer *create_frame(ArvCamera *camera, int *width, int *height, int *bpp);
    __declspec(dllexport) void remove_frame(ArvBuffer **buffer);
    
}

ArvCamera* create_camera(void)
{
    ArvCamera *camera;
    camera = arv_camera_new (NULL, NULL);
    return camera;
}

void remove_camera(ArvCamera **camera)
{
    g_clear_object(camera);
}

ArvBuffer *create_frame(ArvCamera *camera, int *width, int *height, int *bpp)
{
    ArvBuffer *arv_buffer;
    arv_buffer = arv_camera_acquisition (camera, 0, NULL);

    if (! ARV_IS_BUFFER (arv_buffer))
        return NULL;
    
    if (arv_buffer_get_payload_type(arv_buffer) != ARV_BUFFER_PAYLOAD_TYPE_IMAGE)
        return NULL;
    
    arv_buffer_get_image_region(arv_buffer, NULL, NULL, width, height);
    *bpp = ARV_PIXEL_FORMAT_BIT_PER_PIXEL(arv_buffer_get_image_pixel_format(arv_buffer)); // bit(s) per pixel
    return arv_buffer;
}

void remove_frame(ArvBuffer **buffer)
{
    g_clear_object(buffer);
}

void frame_pointer(ArvBuffer *resource, char **buffer, size_t *buffer_size)
{
    *buffer = (char*)arv_buffer_get_data(resource, buffer_size);
}
