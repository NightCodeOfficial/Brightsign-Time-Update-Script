#!/usr/bin/env python3
"""
BrightSign Time Updater Script
--------------------------------
This script generates JavaScript code to update the time on a BrightSign device using the system's current date and time.
The generated code is copied to the clipboard for execution in a browser console.

Usage:
1. Run the script.
2. Provide the IP address when prompted.
3. Paste the generated JavaScript code into your browser's console.

"""

import pyperclip
import re
from datetime import datetime


def validate_ip(ip: str) -> str:
    if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
        raise ValueError("Invalid IP address format.")
    return ip


def generate_js_request(ip_address: str, date: str, time: str) -> str:
    js_code = f"""
    fetch('http://{ip_address}/api/v1/time', {{
        method: 'PUT',
        headers: {{
            'Content-Type': 'application/json'
        }},
        body: JSON.stringify({{
            date: '{date}',
            time: '{time}',
            applyTimezone: true
        }})
    }})
    .then(response => {{
        if (response.ok) {{
            console.log('Time updated successfully!');
            return response.json();
        }} else {{
            console.error('Failed to update time:', response.status);
            return response.text().then(text => {{ throw new Error(text) }});
        }}
    }})
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    """
    return js_code.strip()


def main():
    print("Welcome to the BrightSign Time Updater Script!")
    print("The script will use the system's current date and time.\n")

    try:
        # Get user input for IP address
        player_ip = validate_ip(input("Enter the BrightSign player IP address: ").strip())

        # Fetch current date and time from the system
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M")

        print(f"Using system date: {current_date}")
        print(f"Using system time: {current_time}\n")

        # Generate JavaScript code
        js_code = generate_js_request(player_ip, current_date, current_time)

        # Copy the code to the clipboard
        try:
            pyperclip.copy(js_code)
            print("The JavaScript code has been copied to your clipboard.")
            print("Paste it into your browser's console to execute.")
        except pyperclip.PyperclipException:
            print("\nFailed to copy the code to clipboard. Please copy it manually:")
            print(js_code)

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
