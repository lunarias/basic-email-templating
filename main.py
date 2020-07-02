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
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
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
