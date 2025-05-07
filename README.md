# Quake_Mail

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.0+-blue.svg)

An automated system that detects seismic activity near Bangladesh and communicates event details via email.

## Key Functions
- Regularly checks USGS earthquake data (every 5 minutes)
- Identifies seismic events with magnitude >4 within ±2° of Bangladesh
- Automatically sends email notifications with event specifics
- Includes error recovery mechanisms

## Technical Requirements
- Python 3.7+
- Required packages:
  ```bash
  pip install pandas smtplib
