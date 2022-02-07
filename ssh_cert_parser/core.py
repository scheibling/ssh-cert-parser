from base64 import b64decode
from typing import Dict
from .vars import PARSER_FORMATS
from .decoder import decodeString

def parse_from_bytes(cert_format: str, cert_bytes: bytes) -> Dict:
    try:
        parsed_format, parsed_bin = decodeString(b64decode(cert_bytes), True)
        if parsed_format != cert_format:
            print("NOTICE: Supplied format and parsed format do not match")
            print("Proceeding with parsed format")
            cert_format = parsed_format
        parser = PARSER_FORMATS[cert_format](parsed_bin)
    except KeyError:
        raise ValueError(f"Unknown format: {cert_format}")
    except:
        raise ValueError(decodeString(b64decode(cert_bytes), True))
    
    parser.do_decode()
    return parser

def parse_from_string(ssh_string: str) -> Dict:
    try:
        split = ssh_string.split(" ")
        cert_format, cert_bytes = split[0], split[1]
    except ValueError:
        raise ValueError(f"Invalid format for string {ssh_string}")
    
    return parse_from_bytes(cert_format, cert_bytes)

def parse_from_file(filename: str) -> Dict:
    try:
        with open(filename, 'r') as f:
            return parse_from_string(f.read())
    except FileNotFoundError:
        print("ERROR: No file was found")