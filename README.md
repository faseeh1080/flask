# Flask

This is my second Flask project. I hope you find it useful!

# Setup

1. Run `python3 -m venv .venv` for Linux and `py -3 -m venv .venv` for Windows to create a Python virtual environment named `.venv`.
2. If you are using VS Code, press *Ctrl + Shift + P* to open the command palette, then type `Python: Select Interpreter` to choose the interpreter from the virtual environment. This would also activate the virtual environment in the VS Code terminal. If you are using the VS Code terminal, you don't need to do the next step.
3. Run `source .venv/bin/activate` or `. .venv/bin/activate` for Linux and `.venv\Scripts\activate` for Windows to activate the virtual environment.
4. Run `pip install Flask` to install Flask.
5. Run `flask --app flaskr init-db` to initialize the SQLite database.

## Run the App

- Run: `flask --app flaskr run`
- Run with Debugging: `flask --app flaskr run --debug`

## More Information

- [Official Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)