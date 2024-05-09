## Overview


## The `sql-test-cli init` command
The idea is to create one place for all of your sql  tests. Follow the steps below to initialize a sql  test project folder:

1. If you don't already have a folder to hold your  tests, create one and cd into it.

    ```cmd
    mkdir <your folder name>
    cd <your folder name>
    ```

2. Then run the following command:
    ```cmd
    sql-test-cli init
    ```
    Once the initialization is complete, you should see the following output:
    ```
    =======================================================================================================================
                                                        SQL Test
    =======================================================================================================================


                                Project successfully initialized in <your folder name>!
    ```
3. You should see three new objects in your directory: a `.gitignore` file, a `.sql-test-cli` folder, and a `sql-test-cli.yaml` configuration file.

## Configuration
The following configuration values can be set by a user. (* = required)

- `app_env`: This doesn't need to be touched unless you are a developer contributing to `sql-test-cli`.
- `uri*`: This is a valid sqlalchemy uri string that points to the database which holds the objects you want to run tests against. 
- `target_dir`: This is the directory in which to execute the `sql-test-cli run` command. *Default is the current working directory.*
- `log_level`: This value overrides the log level used. *The default value is `WARN`.*

The most convenient way to set these values is in the `sql-test-cli.yaml` at the root of the project. They can also be set at runtime by passing in the value as an option to the `sql-test-cli run` command. (ex. `sql-test-cli run --uri 'sqlite:///sample//test_database.db'`)

Below is the order of operations that `sql-test-cli run` takes to find the proper config:

1. Checks for config values passed to the command as options.
2. Checks for `sql-test-cli.yaml` in current working directory.
3. Walks up the folder hierarchy until it finds `sql-test-cli.yaml` in the project root or times out after searching for 1 second.
4. Uses defaults for non-required config values.

Therefore, the `uri` config value must *either* be passed as an option at runtime *or* be present in the `sql-test-cli.yaml`, as it is required and has no default value.

## Test Repo Cold setup
This tool is made to be used in a repository with a particular structure. 

The recommended repo structure is one that models the interior structure of your data warehouse. This helps greatly with organizing the tests. Here's an example, where our data warehouse contains 3 databases. 

```
.
├───prod # db level
│   ├───sales # schema level
│   │   ├───factOrders # object level
│   │   └───...
│   └───...
│       └───...
├───raw # db level
│   ├───crm # schema level
│   │   ├───customers # object level
│   │   └───...
│   └───...
│       └───...
└───stage # db level
    ├───crm # schema level
    │   ├───stg_customers # object level
    │   └───...
    └───...
        └───...
```


While this is the recommended test repo structure, the level at the root of the repository does not necessarily have to be database. It is valid to split up tests in any number of ways. The only hard fast requirement to be able to run `sql-test-cli` is that the test directory contains *only* valid sql  test files. 

## Writing sql tests
TODO

## `sql-test-cli run`
Running `sql-test-cli` is simple. 

The most convenient way to run it is by setting up `sql-test-cli.yaml` the file with your important config values, and then simply cd'ing into the desired target folder within the  test repo and running `sql-test-cli run` in the command line. 

Let's take a look at the usage output straight from the command line:

```
PS J:\Justin\internal_tools\sql-test-cli> sql-test-cli --help
Usage: sql-test-cli [OPTIONS]

Options:
  --uri TEXT         A sqlalchemy URI that will override the URI provided in
                     .env.
  --target_dir TEXT  The target directory in which run sql-test-cli. Default
                     is the current directory from which the sql-test-cli
                     command is run.
  --filepath TEXT    A path to a single sql  test file.
  --help             Show this message and exit.
```

Passing in any of these options will also override config values that are set in the `sql-test-cli.yaml`.
