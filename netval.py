# simple network configuration validator 
# V3 --> Enhancement: loading baseline from YAML file and matching.



import yaml
import socket
import re

def load_baseline(path='baseline.yaml'):
    with open(path) as f:
        return yaml.safe_load(f)

baseline = load_baseline()
# e.g.: {'ports': [22, 80, 443], 'ssh': {'PermitRootLogin': 'no'}, 'nginx': {'ssl_protocols': 'TLSv1.2'}}
for port in range(1, 1025):
    s = socket.socket(); s.settimeout(0.2)
    if s.connect_ex(('127.0.0.1', port)) == 0 and port not in baseline['ports']:
        print(f"Non-compliant port: {port}")
    s.close()

# Check SSH config
with open('/etc/ssh/sshd_config') as f:
    content = f.read()
for key, val in baseline.get('ssh', {}).items():
    if f'{key} {val}' not in content:
        print(f"SSH config: {key} should be {val}")

# Check Nginx config
with open('/etc/nginx/nginx.conf') as f:
    content = f.read()
if 'TLSv1.2' in baseline.get('nginx', {}).get('ssl_protocols', ''):
    if 'ssl_protocols TLSv1.2' not in content:
        print("Nginx: TLSv1.2 not enabled")