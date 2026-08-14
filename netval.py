# simple network configuration validator 
# V2 --> Enhancement: reading config files and error reporting.


import re

def check_sshd(path='/etc/ssh/sshd_config'):
    with open(path) as f:
        content = f.read()
    issues = []
    if re.search(r'^PermitRootLogin\s+yes', content, re.MULTILINE):
        issues.append('PermitRootLogin is enabled')
    if not re.search(r'^PasswordAuthentication\s+no', content, re.MULTILINE):
        issues.append('PasswordAuthentication not disabled')
    return issues

def check_nginx(path='/etc/nginx/nginx.conf'):
    with open(path) as f:
        content = f.read()
    issues = []
    if 'ssl_protocols' not in content:
        issues.append('ssl_protocols not defined')
    elif 'TLSv1.2' not in content:
        issues.append('TLSv1.2 not enforced')
    return issues

for issue in check_sshd():
    print(f"[FAIL] SSH: {issue}")
for issue in check_nginx():
    print(f"[FAIL] Nginx: {issue}")