import pandas as pd, os, time, base64, pysftp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv

print("This script replaces the old Excel formula/column from the original experiment data spreadsheet \
      utilizing openpyxl (I think, we'll see). The aim is to scrape the relevant fields \
      from the original spreadsheet, process them into a JSON field that needs be appended to \
      example_data.js (or perhaps another, better named file), and to upload these data \
      to IBEX farm which shows the project at https://spellout.net/ibexexps/aubrieamstutz/SPD/experiment.html \
      and whose repo is nonexistent (technique literally called braindead by the original author). \
      It may be possible to update via the web UI via Selenium."

# Assigning env variables for SFTP url, username, and password based on ENV variables
load_dotenv(dotenv_path='.env')
sftp_domain = os.environ.get('SFTP_DOMAIN')
sftp_dir = str(os.environ.get('SFTP_DIR'))
local_dir = str(os.environ.get('LOCAL_DIR'))
ssh_login_name = os.environ.get('SSH_LOGIN_NAME')
password = os.environ.get('PASSWORD')

# Read experimental data, print to terminal
df = pd.read_excel('~/Downloads/experiment_data_revised.xlsx', sheet_name='Sheet1', header=0, usecols="A:K", nrows=64)
print(df)

# upload to remote server
cnopts = pysftp.CnOpts(knownhosts='./known_hosts')
with pysftp.Connection(sftp_domain, username=ssh_login_name, password=password, cnopts=cnopts) as sftp:
    sftp.put_r(local_dir, sftp_dir)

print("Done.")
