# Random Link Clicker

This Python script simulates web page views by randomly selecting links and clicking them through proxies at regular intervals.

## Features

- **Randomized Clicks:** Selects a random link and proxy on each iteration.
- **Proxy Support:** Supports proxies with or without authentication.
- **Configurable Delay:** Waits a specified time interval (default: 90 seconds) between clicks.

## Requirements

- Python 3.x
- [Requests](https://pypi.org/project/requests/) library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/eliaskrupa93/outreach.git
   cd outreach
   ```

2. **Install Dependencies:**

   ```bash
   pip install requests
   ```

## Configuration

1. **Proxies File:**
   - Create a text file containing your proxies (one per line).
   - Use one of these formats:
     - `IP:PORT`
     - `IP:PORT:USERNAME:PASSWORD`
   - Update the `file_name` parameter in the `load_proxies()` function in `main.py` with your proxies file path.

2. **Links File:**
   - Create a text file containing the links you want to click (one per line).
   - Update the `file_name` parameter in the `load_links()` function in `main.py` with your links file path.

## Usage

Run the script with:

```bash
python main.py
```

The script will continuously select a random link and proxy, simulate a click, and wait for 90 seconds before the next click. Adjust the delay as needed in the script.

## Disclaimer

This project is for educational purposes only. Ensure that your use of this script complies with all applicable laws, regulations, and website terms of service. The author is not responsible for any misuse of this tool.
