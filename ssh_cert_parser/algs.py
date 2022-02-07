from struct import unpack
from typing import Dict
from .decoder import decodeUint32, decodeUint64, decodeMpint, decodeString, decodeList

class Algorithm:
    def __init__(self, cert_bytes: bytes) -> None:
        self.cert_bytes = cert_bytes
        self.format = []
        self.decoded = {}
        
    def __str__(self):
        retn = ""
        for key in self.decoded.keys():
            if isinstance(self.decoded[key], str):
                retn += f"{key}: {self.decoded[key]}\n"
            if isinstance(self.decoded[key], int):
                retn += f"{key}: {str(self.decoded[key])}\n"
            if isinstance(self.decoded[key], list):
                retn += f"{key}: \n"
                for item in self.decoded[key]:
                    retn += f"\t{item}\n"
        
        return retn
        
    def to_dict(self):
        return self.decoded
        
    def do_decode(self) -> None:
        for func, key in self.format:
            value, self.cert_bytes = func(self.cert_bytes)
            self.decoded[key] = value
            
    def alg_specific_decode(self) ->  None:
        pass
            
    def return_decoded(self) -> Dict:
        self.alg_specific_decode()
        return self.decoded

class RSA(Algorithm):
    def __init__(self, cert_bytes: bytes) -> None:
        super().__init__(cert_bytes)
        
        self.format = [
            (decodeString, "nonce"),
            (decodeMpint,  "e"),
            (decodeMpint,  "n"),
            (decodeUint64, "serial"),
            (decodeUint32, "type"),
            (decodeString, "key id"),
            (decodeList, "valid principals"),
            (decodeUint64, "valid after"),
            (decodeUint64, "valid before"),
            (decodeString, "critical options"),
            (decodeList, "extensions"),
            (decodeString, "reserved"),
            (decodeList, "signature key"),
            (decodeList, "signature"),
        ]
        
class DSA(Algorithm):
    def __init__(self, cert_bytes: bytes) -> None:
        super().__init__(cert_bytes)

        self.format = [
            (decodeString, ""),
            (decodeString, "nonce"),
            (decodeMpint,  "p"),
            (decodeMpint,  "q"),
            (decodeMpint,  "g"),
            (decodeMpint,  "y"),
            (decodeUint64, "serial"),
            (decodeUint32, "type"),
            (decodeString, "key id"),
            (decodeString, "valid principals"),
            (decodeUint64, "valid after"),
            (decodeUint64, "valid before"),
            (decodeString, "critical options"),
            (decodeString, "extensions"),
            (decodeString, "reserved"),
            (decodeString, "signature key"),
            (decodeString, "signature"),
        ]
        

class ECDSA(Algorithm):
    def __init__(self, cert_bytes: bytes) -> None:
        super().__init__(cert_bytes)
        
        self.format = [
            (decodeString, "nonce"),
            (decodeString, "curve"),
            (decodeString, "public_key"),
            (decodeUint64, "serial"),
            (decodeUint32, "type"),
            (decodeString, "key id"),
            (decodeList, "valid principals"),
            (decodeUint64, "valid after"),
            (decodeUint64, "valid before"),
            (decodeString, "critical options"),
            (decodeList, "extensions"),
            (decodeString, "reserved"),
            (decodeList, "signature key"),
            (decodeList, "signature"),
        ]


class ED25519(Algorithm):
    def __init__(self, cert_bytes: bytes) -> None:
        super().__init__(cert_bytes)
        
        self.format = [
            (decodeString, "nonce"),
            (decodeString, "pk"),
            (decodeUint64, "serial"),
            (decodeUint32, "type"),
            (decodeString, "key id"),
            (decodeList,   "valid principals"),
            (decodeUint64, "valid after"),
            (decodeUint64, "valid before"),
            (decodeString, "critical options"),
            (decodeList, "extensions"),
            (decodeString, "reserved"),
            (decodeList, "signature key"),
            (decodeList, "signature"),
        ]