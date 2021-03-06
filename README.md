# Pokemon Search, In Python! 
## Initial Setup

Set up a virtual python environment:

```bash
python3 -m virtualenv .venv
```

Activate the virtual python environment:

```bash
source .venv/bin/activate
```

Install necessary dependencies:
```
pip install -r requirements.txt
```

## How to Run in LocalDev

If virtual python environment is activated, run:

```bash
export FLASK_ENV=development
flask run
```

If virtual python environment is not activated, run:

```bash
python3 -m flask run
```
