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
        ("_ti",POINTER(m101_header_t)),
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
