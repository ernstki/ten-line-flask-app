# A ten-line Flask application

## Requirements

* Python 2.7 and [pip][]


## Installation

```bash
git clone https://github.com/ernstki/ten-line-flask-app.git
cd ten-line-flask-app

# if required; these were the packages on my Ubuntu 16.04 system
sudo apt-get install python-pip python-virtualenv

# optional, but here's how you create an isolated environment
# with only the packages required for this project
virtualenv venv
source venv/bin/activate

# install necessary dependencies; add '--user' if you didn't
# create a virtualenv above
pip install -r requirements.txt

# run the Flask development server; use 'kill %1' to terminate it
FLASK_APP=app.py flask run &
xdg-open http://127.0.0.1:5000  # or just 'open' on OS X / macOS
```


## Notes

See the open [pull request #2][pr2] for an example of how to take a simple
Flask app to the next level by creating a Python module for it and adding
a `setup.py` installation script.

Can you find the bug? When the [`home.html` template][htpl] renders, it should
greet you with "Hello from <your hostname>" instead of "Hello from nowhere."
See [issue #1][iss1] for details.


## Author

Kevin Ernst ([ernstki -at- mail.uc.edu](mailto:ernstki%20-at-%20mail.uc.edu))


## License

Distributed under the terms of the [WTFPL][].


[pip]: https://pip.readthedocs.io/en/stable/installing/
[pr2]: ../../pull/2
[htpl]: templates/home.html#L25
[iss1]: ../../issues/1
[wtfpl]: http://www.wtfpl.net/about/
