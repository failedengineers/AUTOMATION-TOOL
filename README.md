AUTOMATION-TOOL
A lightweight automation tool that extracts recruiter emails and LinkedIn links from raw hiring data, helping streamline job outreach and networking workflows.
A simple Python-based utility that scans Excel files to automatically extract recruiter emails and LinkedIn profile links for faster job outreach and networking.


dependecies:# install these dependencies first
pip install pandas openpyxl



Step 1 — Extract Hiring Posts from LinkedIn

Open:

Apify LinkedIn Post Scraper 
https://console.apify.com/actors/buIWk2uOUzTmcLsuB/input

Enter keywords like:(WHATEVER DOMAIN WHERE YOU  WANT TO FIND OPPERTUNITY)#THE MORE KEYWORDS THE MORE DATA THE MORE CHANCES TO FIND EMAILS
hiring software engineer
hiring python developer

Run the actor
Wait for scraping to complete
Download the dataset as an Excel file (.xlsx)

Step 2 — Extract Emails & LinkedIn URLs

Run the extraction script:

python extractor.py  (Generate clean CSV files OF EMAILS AND ALSO LINKEDIN URL)

Step 3 — Prepare Resume

Place your resume PDF inside the project folder. 
Step 4 — Enable Gmail App Password
Go to:
Google App Passwords
Enable 2-Factor Authentication
Generate an App Password
Copy the generated password

Update your email sender  and resume name and the file name in the script:

SENDER_EMAIL = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_generated_password"  # DONT LEAVE SPACES WHILE ENTERING THE PASSWD HERE

Step 5 — Send Automated Outreach Emails

Run the mail automation script:

python mail_sender.py

Tech Stack
Python
Pandas
Regex
