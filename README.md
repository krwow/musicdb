# musicdb

musicdb is a project of website with a music albums database and user accounts support created using Django framework.

After deploying on server each user can create its own account and create a collection of music albums with some information about albums and their tracklists.

## How to run this project

### Prerequisites

**Python 3.x** (tested on Python 3.11.2) with **Django** and **Pillow** pip packages.

You can use provided [requirements.txt][1] file to install pip packages using command in folder with this text file:  
`pip install -r requirements.txt`

It is a good idea to install packages in a separate virtual environment, which can be created using command:  
`python -m venv c:\path\to\myenv`

In Windows virtual environment can be activated by command:

| In CMD:                               | In PowerShell:                        |
| ------------------------------------- | --------------------------------------|
| c:\path\to\myenv\Scripts\activate.bat | c:\path\to\myenv\Scripts\Activate.ps1 |

More information about virtual environments can be found in [Python venv documentation](https://docs.python.org/3/library/venv.html).

If you want to use **git clone** command to download code, then you need **git** to be installed on your machine.

But you can also just click on [this link][2] and download code straight from GitHub using your web browser without **git**.

### Running project

1. Clone repository using:  
`git clone https://github.com/krwow/musicdb.git`
2. In command-line shell of your choice go inside **musicdb** folder, where **manage.py** is located.  
(If code was downloaded using web browser instead of cloning repository - unzip **musicdb-main.zip**, then go inside **musicdb-main** folder.)
3. Run command to make database migrations:  
`python manage.py migrate`
4. Run command to start local server:  
`python manage.py runserver`
5. Paste below url address in your web browser to enter website:  
`http://127.0.0.1:8000/account/`
6. When launching project for the first time - click on **here** link on displayed website or go straight to account creation by entering:  
`http://127.0.0.1:8000/account/register/`

## Disclaimer

As musicdb remains in development, at this moment emails with link to reset user account password are being displayed in shell instead of using proper SMTP server, what is made by:  
`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

[1]: ./requirements.txt
[2]: https://github.com/krwow/musicdb/archive/refs/heads/main.zip