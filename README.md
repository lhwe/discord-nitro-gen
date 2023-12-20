## Introduction
This repository contains a Python script for generating Discord promo links using a specified API. The script utilizes threading to enhance performance by making concurrent requests. Please read the following guidelines to set up and use the code effectively.

### Prerequisites
- Python 3.11
- Requests library (`pip install requests`)

### Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/lhwe/discord-nitro-gen
   cd discord-nitro-gen
   ```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Configuration:

###    Open the script (discord_promo_generator.py) and set the following variables:
  - api_url: The Discord API URL for fetching promo links.
  - payload: The payload required for API requests.
  - proxy_file: Path to the file containing proxy addresses.
  - output_file: Path to the file where generated promo links will be saved.
### Run the Script:

```bash
python discord_promo_generator.py
```

### Important Notes

Make sure to handle proxies responsibly and ensure compliance with Discord's terms of service.
Adjust the num_threads variable based on your system's capacity to avoid performance issues.

### Disclaimer

This script is provided as-is. Use it responsibly and in accordance with Discord's policies.

### Legal
Copyright © lhwe 2023

All rights reserved. This code is the property of lhwe. Any unauthorized use or reproduction without permission is strictly prohibited. Legal action may be taken in response to any copyright infringement.

For inquiries, contact [me](mailto:lhwe.dev@protonmail.com).
