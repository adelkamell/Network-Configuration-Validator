# Simple Network Configuration Validator

## 🔍 Overview
**Simple Network Configuration Validator** is a lightweight Python script designed to scan local open ports and alert you to any unauthorized services running on your system.

This is **Version 1 (V1)** of the tool, focused on detecting open ports that are not part of a predefined allowed list.

---

## 📋 Features
- Scans ports from **1 to 1024** (well-known ports)
- Alerts on any open port not in the allowed set
- Predefined allowed ports:
  - `22`  (SSH)
  - `80`  (HTTP)
  - `443` (HTTPS)
- Fast scanning with a timeout of `0.2` seconds per port
- Lightweight and dependency-free (uses only Python standard library)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- No additional libraries required

### Usage
1. Clone or download the script.
2. Run the script from your terminal:

```bash
python port_scanner.py
```

### Example Output
```text
[ALERT] Unauthorized port 8080 open
[ALERT] Unauthorized port 3306 open
```

### 🛠️ Customization
You can modify the ALLOWED set to include or exclude ports based on your security policy:

```python
ALLOWED = {22, 80, 443, 53}  # Add DNS port as allowed
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

### Made with ❤️ for the security community