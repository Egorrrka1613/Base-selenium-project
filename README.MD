# Selenium Python example project

Example of primitive test project using selenium, pytest, allure.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install virtualenv
virtualenv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Setup env
Make sure to create pytest.ini file locally. For example you can use pytest.ini.example


```ini
[pytest]
env =
    BASE_URL=https://passport.yandex.ru

    EXPLICITLY_WAIT_IN_SECOND=40

    LOGIN=
    BLOCKED_LOGIN=
    LOGIN_BY_BROOT_FORCE=
    PASSWORD=
```

## Running locally


```bash
python -m pytest --alluredir=./allure-results
```