
import sys
import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape

loader = PackageLoader('email_templating', 'templates')
J2 = jinja2.Environment(loader=loader)

ALLOWED_TYPES = [
        {
        'key': 'secops_instance_details',
        'template_file': 'secops_instance_details.html'
        },

        {
        'key': 'secops_instance_request',
        'template_file': 'secops_instance_request.html'
        }
    
    ]


def generate_email(type, data):

    _the_type = None

    for _type in ALLOWED_TYPES:
        if _type['key'] == type:
            _the_type = _type

    if _the_type is None:
        raise FileNotFoundError()

    template = J2.get_template('secops_instance_details.html')
    return template.render({'content': data})

def parseContent():

    struct = {
        'content': {
            'build_id': '9090',
            'build_type': 'amz-linux-2',            
            'private_key': """-----BEGIN RSA PRIVATE KEY----- 
            ************bunchofletters*****
            ****************************
            **************************
            -----END RSA PRIVATE KEY-----""",
            'instance_id': 'x-xxxxxxxx',
            'availability_zone': 'us-east-1',                
            'ip': {
                'private': '192.168.1.xxx',
                'public': '193.168.1.xxx'
            },            
            'urls': {
                'approve': 'https://example/?a=b&c=d',
                'reject': 'https://example/?1=2&3=4'
            },      
            'deploy_url': 'https://example/?a=b&c=d'                            
        }
    }

    return struct



""" def main():    

    example_struct = parseContent()
    print(generate_email(type='secops_instance_details', data=example_struct['content']))


if __name__ == '__emailing__':
    main()
 """