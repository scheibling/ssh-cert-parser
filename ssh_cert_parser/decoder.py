from struct import unpack
from typing import Tuple

def decodeUint32(value: bytes) -> Tuple[int, bytes]:
    return unpack('>I', value[:4])[0], value[4:]

def decodeUint64(value: bytes) -> Tuple[int, bytes]:
    return unpack('>Q', value[:8])[0], value[8:]

def decodeMpint(value: bytes) -> Tuple[int, bytes]:
    size = unpack('>I', value[:4])[0]+4
    return None, value[size:]

def decodeString(value: bytes, decode: bool = True) -> Tuple[str, bytes]:
    size = unpack('>I', value[:4])[0]+4
    return value[4:size].decode('iso-8859-1') if decode and not isinstance(value[4:size], str) else value[4:size], value[size:]

def decodeList(value: bytes) -> Tuple[list, bytes]:
    joined, remaining = decodeString(value, False)
    
    dec_list = []
    while len(joined) > 0:
        elem, joined = decodeString(joined)
        if elem != '':
            dec_list.append(elem)
    return dec_list, remaining