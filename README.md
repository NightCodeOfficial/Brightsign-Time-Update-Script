# BrightSign Time Updater

This script helps you update the time on your BrightSign device using the system's current date and time. It generates JavaScript code that can be pasted into your browser's console to synchronize the time on your BrightSign player.

## Features

- Automatically fetches the current system date and time.
- Generates JavaScript code for quick time updates.
- Copies the generated code to your clipboard for easy execution.
- Lightweight and user-friendly.

## Requirements

- Python 3.6 or higher
- `pyperclip` library for clipboard functionality

## Installation

1. Clone the repository:

2. Install dependencies:
   `
   pip install -r requirements.txt
   `

## Usage

1. Open your browser, log in to the BrightSign player

2. Run the script:
   `
   python brightsign_time_updater.py
   `

3. Enter the IP address of your BrightSign player when prompted:

4. The script will:
   - Fetch the current date and time from your system.
   - Generate JavaScript code to update the time on your BrightSign device.
   - Copy the JavaScript code to your clipboard.
   
5. Open the console in your browser 
   - Chrome `ctrl+shift+j`
   - Firefox `ctrl + shift + k`


## Example Output

Here’s an example of the generated JavaScript code:
```javascript
fetch('http://192.168.0.101/api/v1/time', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        date: '2025-01-01',
        time: '12:45',
        applyTimezone: true
    })
})
.then(response => {
    if (response.ok) {
        console.log('Time updated successfully!');
        return response.json();
    } else {
        console.error('Failed to update time:', response.status);
        return response.text().then(text => { throw new Error(text) });
    }
})
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

## Notes

- Ensure that the IP address provided matches your BrightSign player's IP.
- The script assumes your system time and timezone are correctly configured.
- If clipboard functionality fails, the script will display the JavaScript code for manual copying.

