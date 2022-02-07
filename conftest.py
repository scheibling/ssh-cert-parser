import os
from time import time
from pytest import fixture

def make_certs(path, items):
    created = []
    for alg, bits in items:
        os.system(f"ssh-keygen -t {alg} -b {bits} -f {path.join(f'{alg}_{bits}_ca')} -N \"\" -C '{alg}_ca'")
        
        for c_alg, c_bits in items:
            os.system(f"ssh-keygen -t {c_alg} -b {c_bits} -f {path.join(f'{alg}_{bits}_{c_alg}_{c_bits}_key')} -N \"\"")
            os.system(f"ssh-keygen -s {path.join(f'{alg}_{bits}_ca')} -I {alg}_{bits}_{c_alg}_{c_bits}_serial -n principal_1,principal_2,principal_3 -V +1d -z 123 {path.join(f'{alg}_{bits}_{c_alg}_{c_bits}_key.pub')}")

            created.append({
                "path": str(path.join(f'{alg}_{bits}_{c_alg}_{c_bits}_key-cert.pub')),
                "principals": [
                    "principal_1",
                    "principal_2",
                    "principal_3"
                ],
                "serial": 123,
                "identifier": f"{alg}_{bits}_{c_alg}_{c_bits}_serial",
                "time_before_valid": time() - 100,
                "time_during_valid": time() + 100,
                "time_after_valid": time() + (60 * 60 * 24) + 100
            })
            
    return created

@fixture
def rsa_cert_factory(tmpdir_factory, scope='session'):
    key_path = tmpdir_factory.mktemp('rsa_keys')
    
    rsa_ca =  [
        ('rsa', '1024'),
        ('rsa', '2048'),
        ('rsa', '4096')
    ]
    
    return make_certs(key_path, rsa_ca)

@fixture
def dsa_cert_factory(tmpdir_factory, scope='session'):
    key_path = tmpdir_factory.mktemp('dsa_keys')
    
    dsa_ca =  [
        ('dsa', '1024'),
        ('dsa', '2048')
    ]
    
    return make_certs(key_path, dsa_ca)

@fixture
def ecdsa_cert_factory(tmpdir_factory, scope='session'):
    key_path = tmpdir_factory.mktemp('ecdsa_keys')
    
    ecdsa_ca = [
        ('ecdsa', '256'),
        ('ecdsa', '521'),
    ]
    
    return make_certs(key_path, ecdsa_ca)


@fixture
def ed25519_cert_factory(tmpdir_factory, scope='session'):
    key_path = tmpdir_factory.mktemp('ed25519_keys')
    
    ed25519_ca = [
        ('ed25519', '69'),
        ('ed25519', '255')
    ]
    
    return make_certs(key_path, ed25519_ca)