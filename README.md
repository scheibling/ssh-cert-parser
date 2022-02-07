# OpenSSH Certificate Parser
A python-based OpenSSH certificate parser. Based on the gist by [@corny](https://gist.github.com/corny/8264b74a130eb663dbf3d3f0fe0e0ec9)

# Limitations
- DSA parsing is currently broken, will be fixed in a future release
- Signature, signature key, public key and nonce parsing has not been implemented yet

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
# Output to stdout as test
ssh_cert_parser.py -f /path/to/ssh/certificate

# Result:
# nonce: 8Å+c♥©¡%|ÜÂ××~♂♥íÖ°À `Ø↔¬$z
# curve: nistp256
# public_key: ♦à²÷xÒd¤r♠Ðc½§$íw▲RrwVOê∟Mç↑í»±Ãa»£¡cD↑fôæF?ê☺ëØâ↨Òþ
# serial: 123
# type: 1
# key id: ecdsa_256_ecdsa_256_serial
# valid principals:
#         principal_1
#         principal_2
#         principal_3
# valid after: 1644245220
# valid before: 1644331703
# critical options:
# extensions:
#         permit-X11-forwarding
#         permit-agent-forwarding
#         permit-port-forwarding
#         permit-pty
#         permit-user-rc
# reserved:
# signature key:
#         ecdsa-sha2-nistp256
#         nistp256
#         ♦ M0ËÝµWFÝO♣5ySUw☻h▬4Õbû>üÞ♣½#>í¹þL´
# Ý*%5O!ÒhLÀgómMþûË
# signature:
#         ecdsa-sha2-nistp256
#         !¹"ºlÕ(ÄÐÐ♀↓º¤▲KlÜ¤}¡6vÙ ☺é04×P¥
#                                         ↑→zujÇú« õ%[ïl¬öuhR°♂

# Output to stdout as json
ssh_cert_parser.py -f /path/to/ssh/certificate --json

# Result:
# {
#     "nonce": "8\u00c5+c\u0003\u00a9\u00a1%\u008e|\u00dc\u0086\u00c2\u00d7\u00d7~\u000b\u0003\u00ed\u00d6\u0099\u0081\u00b0\u00c0\t`\u00d8\u001d\u00ac\u009a$z",
#     "curve": "nistp256",
#     "public_key": "\u0004\u00e0\u00b2\u009a\u00f7x\u00d2d\u00a4r\u0006\u00d0\u0087\u0004\bc\u0097\u009a\u00bd\u00a7$\u0097\u00edw\u001eRrwVO\u0091\u00ea\u001c\u009e?z\u00caM\u00e7\u0018\u00ed\u00bb\u00b1\u00c3a\u00bb\u00a3\u00a1cD\u0018f\u00f4\u00e6F?\u00ea\u0001\u0087\u00eb\u00d8\u00e2\u0017\u00d2\u00fe",
#     "serial": 123,
#     "type": 1,
#     "key id": "ecdsa_256_ecdsa_256_serial",
#     "valid principals": [
#         "principal_1",
#         "principal_2",
#         "principal_3"
#     ],
#     "valid after": 1644245220,
#     "valid before": 1644331703,
#     "critical options": "",
#     "extensions": [
#         "permit-X11-forwarding",
#         "permit-agent-forwarding",
#         "permit-port-forwarding",
#         "permit-pty",
#         "permit-user-rc"
#     ],
#     "reserved": "",
#     "signature key": [
#         "ecdsa-sha2-nistp256",
#         "nistp256",
#         "\u0004\u00a0M0\u00cb\u00dd\u00b5WF\u00ddO\u00055ySUw\u0002h\u00164\u008a\u00d5b\u00fb>\u00fc\u00de\u0005\u00bd#\u009e\u00c2>\u00ed\u00b9\u00feL\u00b4\u009f4\u00ef\u0085\u00dd*%5O!\u00d2h\u0099\u0090\u0083L\u00c0g\u00f3mM\u00fe\u00fb\u00cb\u009f\u00b7"
#     ],
#     "signature": [
#         "ecdsa-sha2-nistp256",
#         "\u0000\u0000\u0000!\u0000\u00b9\u008c\"\u00ba\u0007l\u00d5(\u00c4\u00d0\u00d0\f\u0019\u00ba\u00a4\u001eK\u0097l\u009en8&\u00e2\u00dc\u00a4}\u00a16\u008ev\u00d9\u0000\u0000\u0000 \u0001\u00e904\u00d7P\u00a5\u0084\u0018\u001azuj\u00c7\u00fa\u00ab\u00a0\u00f5%[\u00efl\u0096\u00ac\u00f6\u0099uhR\u00b0\u0091\u000b"
#     ]
# }

# Output to file as json
ssh_cert_parser.py -f /path/to/ssh/certificate --output /path/to/output/file.json

# Overwrite existing file if exists
ssh_cert_parser.py -f /path/to/ssh/certificate --output /path/to/output/file.json --overwrite

```

### In scripts
```python
from ssh_cert_parser.core import parse_from_string, parse_from_file, parse_from_bytes

cert_1 = parse_from_file('/path/to/ssh/certificate')

cert_2 = parse_from_string('ecdsa-sha2-nistp521-cert-v01@openssh.com AAAAA....')

cert_3 = parse_from_bytes('ecdsa-sha2-nistp521-cert-v01', b'AAAAA....')

```
