# Simple Network Configuration Validator

## 🔍 Overview

**Simple Network Configuration Validator** is a lightweight Python security auditing tool that validates your system's network services and configurations against a customizable security baseline.

This is **Version 3 (V3)** of the tool, featuring:

- **YAML-based baseline configuration** - Define your security standards in a simple YAML file
- **Unauthorized port scanning** - Detects open ports not in the baseline
- **Configuration file validation** - Reads and analyzes service config files against baseline rules
- **Centralized policy management** - All security rules in one place

---

## 📋 Features

### 1. YAML Baseline Configuration

- Define allowed ports in a YAML file
- Specify expected SSH configuration parameters
- Set Nginx security requirements
- Easily extendable for additional services
- Human-readable policy format

### 2. Port Scanning

- Scans ports from **1 to 1024** (well-known ports)
- Alerts on any open port not in the baseline
- Fast scanning with a timeout of `0.2` seconds per port

### 3. Configuration Validation

- **SSH** (`/etc/ssh/sshd_config`):
  - Validates parameters like `PermitRootLogin`
  - Checks any custom SSH configuration keys
- **Nginx** (`/etc/nginx/nginx.conf`):
  - Verifies `ssl_protocols` settings
  - Ensures TLS configuration matches baseline

### 4. General

- Lightweight with minimal dependencies (PyYAML only)
- Clear, actionable output
- Easy to customize and extend

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- PyYAML library:

```bash
pip install pyyaml
```

Root/sudo access for reading configuration files (if needed)

### Installation

Clone or download the script:

```bash
git clone https://github.com/adelkamell/simple-network-validator.git
cd simple-network-validator
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Create or edit your baseline.yaml file (see example below).

### Usage

Run the script with appropriate permissions:

```bash
sudo python network_validator.py
```

### Example Output

```text
Non-compliant port: 3306
Non-compliant port: 8080
SSH config: PermitRootLogin should be no
Nginx: TLSv1.2 not enabled
```

## 📄 Baseline Configuration (baseline.yaml)

The baseline.yaml file defines your security standards:

```yaml
ports:
  - 22
  - 80
  - 443

ssh:
  PermitRootLogin: no
  PasswordAuthentication: no
  # Add any SSH configuration key-value pairs

nginx:
  ssl_protocols: TLSv1.2
  # Add any Nginx configuration patterns
```

### Customizing the Baseline

Add or remove ports based on your security policy:

```yaml
ports:
  - 22      # SSH
  - 80      # HTTP
  - 443     # HTTPS
  - 53      # DNS (optional)
  - 8443    # Alternative HTTPS
```

Add new SSH parameters to check:

```yaml
ssh:
  PermitRootLogin: no
  PasswordAuthentication: no
  X11Forwarding: no
  ClientAliveInterval: 300
```

Add more Nginx security requirements:

```yaml
nginx:
  ssl_protocols: TLSv1.2
  ssl_ciphers: HIGH:!aNULL:!MD5
  add_header: "X-Frame-Options SAMEORIGIN"
```

## 🛠️ Extending the Tool

Adding New Service Checks
Create new validation functions in the script:

```python
def check_mysql(path='/etc/mysql/mysql.conf.d/mysqld.cnf'):
    with open(path) as f:
        content = f.read()
    baseline = load_baseline()
    for key, val in baseline.get('mysql', {}).items():
        if f'{key} {val}' not in content:
            print(f"MySQL: {key} should be {val}")
```

Then add to your baseline.yaml:

```yaml
mysql:
  bind-address: 127.0.0.1
  max_connections: 100
  skip-networking: 0
```

### Custom Validation Logic

For complex validations, you can add pattern matching:

```python
import re

def check_firewall(path='/etc/ufw/ufw.conf'):
    with open(path) as f:
        content = f.read()
    if not re.search(r'ENABLED=yes', content):
        print("Firewall not enabled")
```

### 📁 Project Structure

```text
simple-network-validator/
├── network_validator.py   # Main script
├── baseline.yaml          # Security baseline configuration
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── LICENSE                # License file
```

### 📦 Dependencies

- Python 3.x - Core language

- PyYAML - YAML file parsing

- All other modules are from Python standard library

- Install Dependencies

```bash
pip install pyyaml
```

Or create a requirements.txt:

```text
pyyaml>=6.0
```

### ⚠️ Disclaimer

This tool is intended for educational and administrative use only. Use it only on systems you own or have explicit permission to audit. Misuse of this tool may violate applicable laws and regulations.

### 🤝 Contributing

Contributions are welcome! Here's how you can help:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

### Contribution Ideas

Add support for more configuration files

Implement additional security checks

Improve error handling and logging

Create a web-based dashboard

Add automated testing

Write comprehensive documentation

### 🐛 Reporting Issues

Found a bug or have a suggestion? Please open an issue on GitHub with:

Description of the problem

Steps to reproduce

Expected vs actual behavior

Your environment (OS, Python version, etc.)

### 👤 Author

- Adel Kamell

- GitHub: @adelkamell

### 🙏 Acknowledgments

Inspired by industry best practices:

[CIS Benchmarks](https://www.cisecurity.org/benchmarks/)

[SSH Hardening Guide](https://www.ssh.com/ssh/hardening)

[Nginx Security Guide](https://nginx.org/en/docs/http/configuring_https_servers.html)

[YAML Specification](https://yaml.org/spec/)

### 📚 Resources

[PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

[Python Socket Programming](https://docs.python.org/3/library/socket.html)

[Security Best Practices](https://www.owasp.org/)

### Made with ❤️ for the security community
