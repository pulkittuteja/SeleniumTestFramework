### **Software Requirements:**
- Python 3.7 or later (Recommended: Python 3.10+)
- Google Chrome, Mozilla Firefox, or Microsoft Edge installed
- ChromeDriver, GeckoDriver, and EdgeDriver (handled automatically by `webdriver-manager`)
- pip (latest version recommended)


## Installation & Setup

### **Step 1: Clone the Repository**
```
git clone <repository_url>
cd <repository_name>
```

**Step 2: Install Dependencies**
```
pip install -r requirements.txt
```

### **Run Tests **
```
pytest tests/test_login.py --html=reports/login_test_report.html
```

## Viewing Test Reports
After test execution, reports will be generated in the `reports/` directory.
- Open `test_report.html` in any browser to view the detailed report.


## Troubleshooting
- If `webdriver-manager` fails, manually download and set up the appropriate WebDriver.
- Ensure that the correct browser is installed.

