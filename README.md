# OpenSSH Certificate Parser
A python-based OpenSSH certificate parser. Based on the gist by [@corny](https://gist.github.com/corny/8264b74a130eb663dbf3d3f0fe0e0ec9)

# Notice
DSA parsing is currently broken, will be fixed in a future release

## Installation
### From PyPi
```bash
python3 -m pip install ssh_cert_parser
```

### From source
```bash
git clone https://github.com/scheibling/ssh-cert-parser.git
cd ssh-cert-parser
python3 setup.py install
```

## Usage
### CLI
```bash
ssh_cert_parser.py -f /path/to/ssh/certificate
```

### In scripts
```python
from ssh_cert_parser.core import parse_from_string, parse_from_file, parse_from_bytes

cert_1 = parse_from_file('/path/to/ssh/certificate')

cert_2 = parse_from_string('ecdsa-sha2-nistp521-cert-v01@openssh.com AAAAA....')

cert_3 = parse_from_bytes('ecdsa-sha2-nistp521-cert-v01', b'AAAAA....')

```
