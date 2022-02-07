from .algs import RSA, DSA, ECDSA, ED25519

PARSER_FORMATS = {
  "ssh-rsa-cert-v01@openssh.com":               RSA,
  "ssh-dss-cert-v01@openssh.com":               DSA,
  "ecdsa-sha2-nistp256-cert-v01@openssh.com":   ECDSA,
  "ecdsa-sha2-nistp384-cert-v01@openssh.com":   ECDSA,
  "ecdsa-sha2-nistp521-cert-v01@openssh.com":   ECDSA,
  "ssh-ed25519-cert-v01@openssh.com":           ED25519,
}