# PyBuster

A fast, multi-threaded directory and file brute-forcing tool written in Python. 

This tool is designed to uncover hidden directories and files on target web servers. It utilizes `concurrent.futures` for high-speed multi-threaded requests and supports custom file extension fuzzing.

## 🚀 Features

- **Multi-threaded Execution:** Extremely fast scanning using Python's ThreadPoolExecutor.
- **Extension Fuzzing (`-x`):** Dynamically append file extensions (e.g., php, txt) to your wordlist payloads.
- **Clean Output:** Automatically filters out clutter and only displays successful hits (200 OK), ignoring standard errors.
- **Lightweight:** Built with minimal external dependencies.

## 🛠️ Installation

Clone the repository and install the required `requests` library if you haven't already:

```bash
git clone [https://github.com/YOUR_USERNAME/PyBuster.git](https://github.com/YOUR_USERNAME/PyBuster.git)
cd PyBuster
pip install requests
```

## 💻 Usage

The tool requires a target URL (`-u`) and a wordlist (`-w`).

**Basic Directory Scanning:**
```bash
python pybuster.py -u [http://example.com](http://example.com) -w /path/to/wordlist.txt
```

**Scanning with Extensions:**
Use the `-x` flag followed by extensions separated by spaces to search for specific file types:

```bash
python pybuster.py -u [http://example.com](http://example.com) -w /path/to/wordlist.txt -x php txt html bak
```

### Arguments:

* `-u`, `--url`      : Target URL (Required)
* `-w`, `--wordlist` : Path to the wordlist (Required)
* `-x`, `--extension`: Target extensions separated by space (Optional)

## ⚠️ Disclaimer

This tool is created for educational purposes and ethical hacking only. You are only authorized to use this tool on systems you own or have explicit permission to test. The author (Serkan Yeltekin) is not responsible for any misuse or damage caused by this program.
