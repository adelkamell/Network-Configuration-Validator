# Simple Network Configuration Validator

## 🔍 Overview

**Simple Network Configuration Validator** is a lightweight Python security auditing tool that checks your system's network services and configurations against security best practices.

This is **Version 1 (V1)** of the tool, featuring:

- **Unauthorized port scanning** - Detects open ports not in the allowed list
- **Configuration file validation** - Reads and analyzes service config files for security misconfigurations

---

## 📋 Features

### 1. Port Scanning

- Scans ports from **1 to 1024** (well-known ports)
- Alerts on any open port not in the allowed set
- Predefined allowed ports:
  - `22`  (SSH)
  - `80`  (HTTP)
  - `443` (HTTPS)
- Fast scanning with a timeout of `0.2` seconds per port

### 2. Configuration Validation

- **SSH** (`/etc/ssh/sshd_config`):
  - Detects if `PermitRootLogin` is enabled
  - Checks if `PasswordAuthentication` is properly disabled
- **Nginx** (`/etc/nginx/nginx.conf`):
  - Verifies `ssl_protocols` is defined
  - Ensures `TLSv1.2` is enforced for secure connections
- Clear error reporting with actionable insights

### 3. General

- Lightweight and dependency-free (uses only Python standard library)
- Simple, readable output format

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Root/sudo access for reading configuration files (if needed)

### Usage

1. Clone or download the script.
2. Run the script from your terminal:

```bash
python network_validator.py
```

Note: For reading system configuration files, you may need to run with appropriate permissions:

```bash
sudo python network_validator.py
```

### Example Output

```text
[ALERT] Unauthorized port 8080 open
[ALERT] Unauthorized port 3306 open
[FAIL] SSH: PermitRootLogin is enabled
[FAIL] SSH: PasswordAuthentication not disabled
[FAIL] Nginx: TLSv1.2 not enforced
```

### 🛠️ Customization

Modify Allowed Ports
Update the ALLOWED set to include or exclude ports based on your security policy:

```python
ALLOWED = {22, 80, 443, 53, 8080}  # Add DNS and alternative HTTP ports
```

### Add New Service Checks

Extend the tool by creating new validation functions:

```python
def check_apache(path='/etc/apache2/apache2.conf'):
    # Add your validation logic here
    return issues
```

### Custom Configuration Paths

Pass custom paths to check functions:

```python
for issue in check_sshd(path='/custom/path/sshd_config'):
    print(f"[FAIL] SSH: {issue}")
```

### 📁 Project Structure

```text
simple-network-validator/
├── network_validator.py   # Main script
├── README.md              # Documentation
└── LICENSE                # License file
```

### 🤝 Contributing

Contributions are welcome! Here's how you can help:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

### 👤 Author

Adel Kamell

GitHub: @adelkamell

### 🙏 Acknowledgments

Inspired by best practices from:

- [CIS Benchmarks](https://www.cisecurity.org/benchmarks/)

- [SSH Hardening Guide](https://www.ssh.com/ssh/hardening)

- [Nginx Security Guide](https://nginx.org/en/docs/http/configuring_https_servers.html)

### Made with ❤️ for the security community
