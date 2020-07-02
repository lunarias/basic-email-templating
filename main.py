import os
import jinja2

J2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

ALLOWED_TYPES = [{
    'key': 'secops_instance_details',
    'template_file': 'secops_instance_details.html'
}]


def generate_email(type, data):

    _the_type = None

    for _type in ALLOWED_TYPES:
        if _type['key'] == type:
            _the_type = _type

    if _the_type is None:
        raise FileNotFoundError()

    template = J2.get_template(_the_type['template_file'])
    return template.render({'content': data})


def main():
    example_struct = {
        'content': {
            'ssh_key': """-----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAjK5xijRRoCQlF3RYFsrR90C5ejyRbGn2FtTxR4xPJf75i3DDxUcXZB8nEGL
    f5CYRWqw3plQLCzIq3lVJtAYPI2vziuT/dRLWyh5IXtDcP7ndZCteGT+kUn2tICKElJQ0LDPsiy
    XXFWOJm98JbGg3M/5HNndHKpb1+chjc4REzsq+y/VGHKiAE/zlizntL3S/1uGDMIL6Sguu0bthB
    5NXLTzy3miEXuopyvO4A6BCg48ir7bUcmSRoKes6H5/Cdtpa1YAk9EbQ/pP7cCiSohlbKcLSuz0j
    PI+8wIaNDIADSMKiXt6X7T3tFUeeKobN1pH5cD6SBYFZ/yo4i5x40wIDAQABAoIBAD/7yxoPh5xt
    NA2B1dqv7mUlI/are3yyhBjIGMaLX9tuSJw87f17YaUg4hR609ehVL1HnJvil49FBuhOJBJjuxj
    iLUdbtbAanGQa99Fiu2b2GHGJFsyuKnYMDM+1spZ4p9byw9QGoeTV6KwkgnNmYYJseKGdmQpDlTg
    SIFmtgmhu0zZpz0yrD/VyXj2XEvFIPWQlAch77vq7TtS4WNUJEbaQrLwyRHTcp4+2y4OrKJa0NL
    35MzVeQ4EKrHNZJsXQ6OXOcR0Ukrhj8gEAFfhToB/rMK5VJvX7FUx2tsDOt7tsKdjUzmcUWLKZTf
    tZYV1cqQKxjangZMmjBT9GKWSskCgYEA/EASzmAuiXA9UN5XvQQ0C/hnyJ3pYAsomsZbfWYbYS3
    7gJ0mqHoWzOE50i9ePj+X0dDaxv7sfT3ommMVjk8KwPLexa2S9uvd2qotUWNexdl5pf2IfLUW9Yw
    pa73JIurYddWaxe2QOujDB8NeTJKdkYLdNNNksN4l7hsp3Fba7UCgYEAjsXMzTShonNqeCgIeiJT
    FN/NYlQjwICrKH9s7RW+TdlLEJ1uIY453pmrX8H4hW/FMVAOHzy68c3Aqz1lUfCpWkGnJ3/LKLZd
    fCrELX8LVvJhaT2pIXQkBIBqpNay1UyDFqhCFvJWwnvk5xgA5/d57o6cTTU4MF5Cb4ahN+WXd2cC
    gYEAkH2TSCvH/GoSdVQrhRSA3P/QWXtA1chJyO9YLahUm8c+JFO7vyenFTa5llIQVk8qRiFn+N6a
    miEcCCg1ft5iHLGbyPIFkgZQyDKMWOlyVWPdtuyszF1wTqt+vnyDzkB/pV+pvF6ME3Jo5PV/+pS
    xNTykwTGlp7pYN7/Phqsp1ECgYBhGR729HN1x+Gxls1jQCJ8sdAt051TkyZR0gyWZZKZZyKmTbc
    NVkgDcyiXE4Dmgc3SWXBUtElQDRngWLV/mF+06W11FC7yIL9viwbcQqqQD+FjnznFpCkSx28K5QG
    Qnnov9fquTfOHuqHTCjZmdJgLrcYPziOlJyEsCUPl3rwwKBgEtuMuTq9A73N1MOrudVa+p03oo8
    G1RVIZ6PyK+WDcRqbu41jmJbLd4xqs7saThyZvq7XLK9kn/0cjl4nZwwI2PADNbopxQ+OdGCahs
    uduK+zc6YiCueD0WABuSXV7scaF8E5gQ57l6k+Xu7hzCaObJeji05sHd7+ojWSCRw2Q
    -----END RSA PRIVATE KEY-----""",
            'ip_address': '192.168.1.100',
            'urls': {
                'approve': 'https://example/?a=b&c=d',
                'reject': 'https://example/?1=2&3=4',
            }
        }
    }

    print(generate_email(type='secops_instance_details', data=example_struct['content']))


if __name__ == '__main__':
    main()
