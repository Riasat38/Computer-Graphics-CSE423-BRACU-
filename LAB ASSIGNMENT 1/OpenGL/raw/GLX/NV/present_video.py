'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_NV_present_video'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_NV_present_video',error_checker=_errors._error_checker)
GLX_NUM_VIDEO_SLOTS_NV=_C('GLX_NUM_VIDEO_SLOTS_NV',0x20F0)
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.c_uint,_cs.c_uint,ctypes.POINTER(_cs.c_int))
def glXBindVideoDeviceNV(dpy,video_slot,video_device,attrib_list):pass
@_f
@_p.types(ctypes.POINTER(_cs.c_uint),ctypes.POINTER(_cs.Display),_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXEnumerateVideoDevicesNV(dpy,screen,nelements):pass