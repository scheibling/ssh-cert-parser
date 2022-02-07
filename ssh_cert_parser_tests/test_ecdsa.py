from time import time as now_time
from ssh_cert_parser.core import parse_from_bytes, parse_from_string, parse_from_file

def do_assert(certinfo, decoded):
    # Assert that the data fields are the same data that was input
    assert decoded['valid principals'] == certinfo['principals']
    assert decoded['serial'] == certinfo['serial']
    assert decoded['key id'] == certinfo['identifier']
    
    # Assert that the decoding of the signature algorithm is correct
    assert 'ecdsa-sha2-nistp' in decoded['signature'][0]
    assert 'ecdsa-sha2-nistp' in decoded['signature key'][0]
    
    # Assert that the times are valid integers
    assert isinstance(decoded['valid after'], int)
    assert isinstance(decoded['valid before'], int)
    
    # Assert that the validity has been correctly decoded
    assert decoded['valid after'] > certinfo['time_before_valid']
    assert decoded['valid after'] < certinfo['time_during_valid']
    assert decoded['valid before'] > certinfo['time_during_valid']
    assert decoded['valid before'] < certinfo['time_after_valid']
    

def test_parse_from_file(ecdsa_cert_factory):
    for certinfo in ecdsa_cert_factory:
        decoded = parse_from_file(certinfo['path'])
        
    do_assert(certinfo, decoded)
        
def test_parse_from_string(ecdsa_cert_factory):
    for certinfo in ecdsa_cert_factory:
        with open(certinfo['path'], 'r') as f:
            decoded = parse_from_string(f.read())
            
        do_assert(certinfo, decoded)
        
def test_parse_from_bytes(ecdsa_cert_factory):
    for certinfo in ecdsa_cert_factory:
        with open(certinfo['path'], 'r') as f:
            split = f.read().split(" ")
            
            decoded = parse_from_bytes(split[0], split[1])
            
        do_assert(certinfo, decoded)