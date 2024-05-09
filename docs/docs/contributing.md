## Contributers Welcome!
Contribution from the any and all is welcomed and appreciated! Check out the [issues](https://github.com/cohenj20/sql-test-cli/issues) on github. If you have an idea for an enhancement, or notice something not working properly, please do open a new issue and open a pull request if you want to lend a hand!

## Environment setup
Here's how to set up your development environment:

1. Clone the repository in your development environment.
2. Install [poetry](https://python-poetry.org/docs/#installation) if it is not already installed on your system.
3. Run the `poetry install` command to install the project dependencies. 
4. At the root of the repo run `poetry run python path/to/commands.py init`. This will create a file called `sql-test-cli.yaml` at the root, among other things. Change the `app_env` value to be 'dev'.
5. To adjust the log level, modify the `log_level` value in `sql-test-cli.yaml`. (Options are `CRITICAL`/`WARN`/`ERROR`/`INFO`/`DEBUG`; default is `WARN`)
5. Get developing!
6. To test run the package use poetry: `poetry run python path/to/commands.py run` in /sample/playlists or in a  test directory you create.

## Testing
It is requested that contributers write new  tests for any new or modified functionality in the codebase. Please put these in the `/tests` folder. 

Feel free to run your tests locally, but the tests will also be executed by github upon the opening of your pull request.

