import os
import jinja2

J2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

ALLOWED_TYPES = [{
    'key': 'secops_instance_details',
    'template_file': 'secops_instance_details.html'
}]

#1 make this a package and include in the jinja2 layer script
""" ADD TO HELLOWORLD LAMBDA
from templates import generate_email
generate_email(type='general_alert', {'ip_address':'1234'})
"""

def generate_email(self, type, data):
    if not type in ALLOWED_TYPES:
        #raise error:
        pass

    _the_type = None

    for type in ALLOWED_TYPES:
        if type['key'] == type:
            _the_type = type



    # == data
    """
    users will be known by the lambda
    """
    example_struct = {
        'users': ['user1@nowhere.com', 'user2@nowhere.com'],
        'content': {
            'ssh_key': """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAjK5xijRRoCQlF3RYFsrR90C5ejyRbGnr2FtTxR4xPJf75i3DDxUcXZB8nEGL
f5CYRWqw3plQLCzIq3lVJtAYPI2vziuT/dRLWyh5IXtcDcP7ndZCteGT+kUn2tICKElJQ0LDPsiy
XXFWOJm98JbGg3M/5HNndHKpb1+chjc4REzsq+y/wVGHKiAE/zlizntL3S/1uGDMIL6Sguu0bthB
5NXLTzy3miEXuopyvO4A6BCg48ir7bUcmSRoKes6H5/Cdtpa1YAk9EbQ/pP7cCiSohlbKcLSuz0j
PI+8wIaNDIADSMKiXt6X7T3tFUeeKobN1pH5cD6SBYFZ/yo4i5x40wIDAQABAoIBAD/7yxoPh5xt
NA2B1dqv7mUlI/are3yyhBjIGMaLX9tuSJw87f17HYaUg4hR609ehVL1HnJvil49FBuhOJBJjuxj
iLUdbtbAanGQa99Fiu2b2GHGJFsyuKnYMDM+1spZ4p9byw9QGoeTV6KwkgnNmYYJseKGdmQpDlTg
SIFmtgmhu0zZpz0yrD/VyXj2XEvFIPWQlAch77vMq7TtS4WNUJEbaQrLwyRHTcp4+2y4OrKJa0NL
35MzVeQ4EKrHNZJsXQ6OXOcR0Ukrhj8gEAFfhToB/rMK5VJvX7FUx2tsDOt7tsKdjUzmcUWLKZTf
tZYV1cqQKxjangZMmjBT9GKWSskCgYEA/EASzmAuiXA9UN5fXvQQ0C/hnyJ3pYAsomsZbfWYbYS3
7gJ0mqHoWzOE50i9ePj+X0dDaxv7sfT3ommMVjk8KwPLexa2S9uvd2qotUWNexdl5pf2IfLUW9Yw
pa73JIurYddWaxe2QOujDB8NeTJKdkYLdNNNksN4l7hsp3Fba7UCgYEAjsXMzTShonNqeCgIeiJT
FN/NYlQjwICrKH9s7RW+TdlLEJ1uIY453pmrX8H4hW/FMVAOHzy68c3Aqz1lUfCpWkGnJ3/LKLZd
fCrELX8LVvJhaT2pIXQkBIBqpNay1UyDFqhCFvJWwnvk5xgA5/d57o6cTTU4MF5Cb4ahN+WXd2cC
gYEAkH2TSCvH/GoSdVQrhRSA3P/QWXtA1chJyO9YLahUm8c+JFO7vyenFTa5llIQVk8qRiFn+N6a
miEcCCg1ft5iHLGbyPIFkgZQyDKMWOlyVWPdtuyszF1wTvqt+vnyDzkB/pV+pvF6ME3Jo5PV/+pS
xNTykwTGlp7pYN7/Phqsp1ECgYBhGR729HN1Ax+Gxls1jQCJ8sdAt051TkyZR0gyWZZKZZyKmTbc
NVkgDcyiXE4Dmgc3SWXBUtElQDRngWLV/mF+06W11FC7yIL9viwbcQqqQD+FjnznFpCkSx28K5QG
Qnnov9fquTfOHuqHTCjZmdJgLrcYPziOlJyEMsCUPl3rwwKBgEtuMuTq9A73N1MOrudVa+p03oo8
G1RVIZ6PyK+WDcRqbu41jmJbLd4xqs7saThZyZvq7XLK9kn/0cjl4nZwwI2PADNbopxQ+OdGCahs
uduK+zc6YiCueD0WABuSXV7scaF8E5gQ57lr6k+Xu7hzCaObJeji05sHd7+ojWSCRwII
-----END RSA PRIVATE KEY-----""",
            'ip_address': '192.168.1.100',
            'urls': {
                'approve': 'https://example/?a=b&c=d',
                'reject': 'https://example/?1=2&3=4',
            }
        }
    }

    # template = J2.get_template('secops_instance_details.html')
    template = J2.get_template(_the_type['template_file'])

    # emails_to_send = []
    # for user in example_struct['users']:
    #     emails_to_send.append({
    #         'email': user,
    #         'body': template.render({'content': example_struct['content']})
    #     })
    #
    # print('writing out first email')
    # with open('output.html', 'a') as email:
    #     print(emails_to_send[0]['body'], file=email)

    rendered = template.render({'content': data})

    return rendered #emails_to_send

if __name__ == '__main__':
    main()