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

## In Hindsight

Flask uses Jinja templating. These templates are rendered on the server side (SSR). Interactivity is limited as the interaction has to be sent back to the server, and the server has to reply with HTML. So you don't get 'dynamic' interaction.

React is a framework (maybe?) which renders on the client side (CSR). React allows for dynamic interaction with rendered items. Data which needs to be stored, or pulled, is done so via a call to a backend server when needed. 

Pages that are rendered client side have negatives, such as SEO / search engine optimisation, and there is a solution - a kind of halfway solution, where an interactive CSR layer sits on top of HTML which is provided through SSR. This is known as 'hydration' - the HTML is loaded first from the server, and then 'hydrated' with the CSR application in Javascript.

Here, I have created an app using Flask, and Jinja templating, in attempt to replicate a Vue application - but cannot achieve the same level of interactivity due to Flask being an SSR, and Vue being a CSR. So, I use form HTML tags to send a request to the server, which then responds, but the user has to 'submit' (POST) the data - i.e. via a button. In Vue, this was not the case as the data had been loaded on the client side, and so could be accessed immediately within the same page, without the need to 'submit' (POST) data back to the server.

To achieve the same interactivity as in the Vue app, I would need to use a CSR framework/library (Vue, React). This would then call the Flask backend for data when needed. Ultimately, this would be a bad idea in this codebase, as the CSR could request the API directly, rather than through the Flask backend (which is essentially acting as a proxy for the API right now).

