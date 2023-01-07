set -eu 

export PYTHONUNBUFFERED=true

VIRTUALENV=.data/venv

if [! -d $VIRTUALENV]; then
    python3 -m venv $VIRTUALENV
fi

if [! -d $VIRTUALENV/bin/pip];then
    curl --silent --show-error 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python3
fi

$VIRTUALENV/bin/pip install -r requirements.txt

$VIRTUALENV/bin/python3 app.py
Footer