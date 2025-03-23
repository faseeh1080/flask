# Flask Example

This is my second Flask project. I hope you find it useful!

The official documentation uses Sqlite whereas this app uses MySQL. If you want to use Sqlite instead, go check the [official documentation](https://flask.palletsprojects.com/en/stable/tutorial/database/).

# Setup

1. Run `python3 -m venv .venv` for Linux and `py -3 -m venv .venv` for Windows to create a Python virtual environment named `.venv`.
2. If you are using VS Code, press *Ctrl + Shift + P* to open the command palette, then type `Python: Select Interpreter` to choose the interpreter from the virtual environment. This would also activate the virtual environment in the VS Code terminal. If you are using the VS Code terminal, you don't need to do the next step.
3. Windows: `.venv\Scripts\activate`  
Linux: `source .venv/bin/activate` or `. .venv/bin/activate`
4. `pip install Flask`
5. `pip install mysql-connector-python`

## Run the App

- Run: `flask --app flaskr run`
- Run with Debugging: `flask --app flaskr run --debug`

## More Information

- [Official Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)