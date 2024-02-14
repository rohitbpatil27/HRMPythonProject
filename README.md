# HRMPythonProject Automated Tests

This project contains automated tests for the HRMPythonProject application using Selenium and pytest. It enables you to run regression tests on different browsers and environments.

## Installation

Clone or download the project.
Create a virtual environment (recommended):
Bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Install dependencies:
Bash
pip install -r requirements.txt
Use code with caution.
Set up browser drivers:

Chrome: Download and install ChromeDriver from https://chromedriver.chromium.org/downloads.
Firefox: Download and install GeckoDriver from https://github.com/mozilla/geckodriver/releases.
Other browsers: Refer to relevant documentation for driver installation.
## Running Tests

Activate the virtual environment (if used).
Navigate to the project root directory.
Run tests:
Bashso
pytest tests/
Use code with caution.
View reports:

HTML reports: Open reports/index.html in your browser.
## Additional Notes:

Ensure you have the required browser drivers installed and accessible.
Refer to the tests/ directory for individual test scripts.
Adjust commands and instructions as needed for your environment.
For more details on specific test features or configurations, refer to the code within the project.