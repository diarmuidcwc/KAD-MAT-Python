#-------------------------------------------------------------------------------
# Name:        Mat101Shared
# Purpose:     Class toemulate the structs for the buffer management in the KAD/MAT/101
#
# Author:      DCollins
#
# Created:     19/03/2014
#
# Copyright 2014 Diarmuid Collins
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------


from ctypes import *

class timespec(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_long),
        ('tv_nsec', ctypes.c_long)
    ]

class topIO_s(Structure):
    _field__ = [
        ("data" , c_char),
        ("dirA" , c_char),
        ("dirB" , c_char),
    ]


class download_s(Structure):
    _fields_ = [
        ("crc", c_int),
        ("status", c_char),
        ("size", c_int),
        ("mac", c_char),
        ("inBufSize", c_int),
        ("outBufSize", c_int),
    ]

class _basehi_U(Union):
    _fields_ = [
        ("base_hi", c_ushort),
        ("pkt_padding", c_ushort),
    ]

class _baselo_U(Union):
    _fields_ = [
        ("base_low", c_ushort),
        ("pkt_size_words", c_ushort),
    ]


class m101_header_t(Structure):
    _anonymous_ = ("u1","u2")
    _fields_ = [
        ("marker", c_ushort),
        ("u1", _baselo_U),
        ("u2", _basehi_U),
        ("CRC_hi", c_ushort),
        ("CRC_low", c_ushort),
        ("filesize_hi", c_ushort),
        ("firmware_rev", c_ushort),
        ("time_hi", c_ushort),
        ("time_lo", c_ushort),
        ("time_micro", c_ushort),
        ("ptp_days", c_ushort),
        ("cfg", c_ushort),
        ("res1", c_ushort),
        ("res2", c_ushort),
        ("res3", c_ushort),
    ]

class m101_header_h(Structure):
    _anonymous_ = ("_t1")
    _fields_ = [
        ("_t1:",POINTER(m101_header_t)),
    ]

class m101_userBuffer_t(Structure):
    _fields_ = [
        ("m101Buffer",m101_header_h),
        ("header",m101_header_t),
        ("userAddrInput", c_ulong),
        ("phyAddrInput", c_ulong),
        ("sizeWordsInput",c_uint),
        ("userAddrResult",c_ulong),
        ("phyAddResult", c_ulong),
        ("sizewordsResult",c_uint),
        ("ID", c_uint),
        ("tsIRQ", timespec),
        ("irqCount", c_uint),
        ("dataValid", c_uint),
        ("panic_count", c_uint),
    ]

class m101_userBuffer_h(Structure):
    _anonymous_ = ("_t1")
    _fields_ = [
        ("_t1",POINTER(m101_userBuffer_t)),
    ]