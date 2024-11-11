# ENPM611 Project Application Template

This is the template for the ENPM611 class project. Use this template in conjunction with the provided data to implement an application that analyzes GitHub issues for the [poetry](https://github.com/python-poetry/poetry/issues) Open Source project and generates interesting insights.

This application template implements some of the basic functions:

- `data_loader.py`: Utility to load the issues from the provided data file and returns the issues in a runtime data structure (e.g., objects)
- `model.py`: Implements the data model into which the data file is loaded. The data can then be accessed by accessing the fields of objects.
- `config.py`: Supports configuring the application via the `config.json` file. You can add other configuration paramters to the `config.json` file.
- `run.py`: This is the module that will be invoked to run your application. Based on the `--feature` command line parameter, one of the three analyses you implemented will be run. You need to extend this module to call other analyses.

With the utility functions provided, you should focus on implementing creative analyses that generate intersting and insightful insights.

In addition to the utility functions, an example analysis has also been implemented in `example_analysis.py`. It illustrates how to use the provided utility functions and how to produce output.

## Setup

To get started, your team should create a fork of this repository. Then, every team member should clone your repository to their local computer. 


### Install dependencies

In the root directory of the application, create a virtual environment, activate that environment, and install the dependencies like so:

```
pip install -r requirements.txt
```

### Download and configure the data file

Download the data file (in `json` format) from the project assignment in Canvas and update the `config.json` with the path to the file. Note, you can also specify an environment variable by the same name as the config setting (`ENPM611_PROJECT_DATA_PATH`) to avoid committing your personal path to the repository.


### Run an analysis

With everything set up, you should be able to run the existing example analysis:

```
python run.py --feature 0
```

That will output basic information about the issues to the command line.


## VSCode run configuration

To make the application easier to debug, runtime configurations are provided to run each of the analyses you are implementing. When you click on the run button in the left-hand side toolbar, you can select to run one of the three analyses or run the file you are currently viewing. That makes debugging a little easier. This run configuration is specified in the `.vscode/launch.json` if you want to modify it.

The `.vscode/settings.json` also customizes the VSCode user interface sligthly to make navigation and debugging easier. But that is a matter of preference and can be turned off by removing the appropriate settings.
-----------------CODE IMPLENTATION DOCUMENTATION STARTS HERE-------------------------
Similar to the above instructions, once everthing is set up.  The code can be run using the "python run.py --feature '# of feature' for 1 - 5 analysis .  There are 6 features besides feature 0.  
--feature 1, utilizes the Analyzer.py module to output a list of all labels and all of the "contributions/events" assoicated with those features.  A graph is also displayed which plots the labels vs "contributions/events"
--feature 2, utilizes the Analyzer.py module to allow for the user to input a number and output issues that are repeated more than the user input to gather feedback as to which issues are more frequently listed.  This feature also allows the user to input a "Creator" name and lists that creators issues and how many times they contributed to their own issues.
--feature 3, utilizes the Analyzer.py module to list all labels and the amount of "comments" that are associated w/ those labels to gather feedback as to which issue labels have an open conversation

--feature 4, utilizes contributor_activity_analysis to analyze contributor activities focusing on interactions with "bug" issues. It identifies top contributors based on their activity 
--feature 5, utilizes contributor_activity_analysis to analyze which issue labels are most active based on comment counts and unique contributor counts.
--feature 6, utilizes contributor_activity_analysis provide activity insights filtered by a specific user and/or label.

### Examples for runnint Analyzer.py module
1. python run.py --feature 1

2. python run.py --feature 2

3. python run.py --feature 3

### Examples for running contributor_activity_analysis.py module

1. **Run Contributor Activity Analysis Focusing on "Bug" Issues**

   ```bash
   python run.py --feature 4
   ```

2. **Run Issue Activity Analysis by Label**

   ```bash
   python run.py --feature 5
   ```

3. **Run Filtered Activity Analysis for a Specific User**

   ```bash
   python run.py --feature 6 --user "john_doe"
   ```

4. **Run Filtered Activity Analysis for a Specific Label**

   ```bash
   python run.py --feature 6 --label "enhancement"
   ```

5. **Run Filtered Activity Analysis for a Specific User and Label**

   ```bash
   python run.py --feature 6 --user "john_doe" --label "bug"
   ```

### Output

The tool will print the analysis results to the console. Depending on the feature selected, you will see different outputs:

- **Feature 4**: Lists the top contributors by activity and their focus on "bug" issues.
- **Feature 5**: Displays issue activity by label, showing comment counts and unique contributor counts for each label.
- **Feature 6**: Shows the activity of contributors filtered by the specified user and/or label.

## Configuration

The script uses a `config` module to manage configuration settings. Command-line arguments are passed to the `config` module via `config.overwrite_from_args(args)`, allowing other parts of the application to access these settings.

If you need to adjust configurations beyond command-line arguments, you can modify the `config` module accordingly.

## Dependencies

- Python 3.x
- Modules:
  - `argparse`: For parsing command-line arguments.
  - `collections`: Provides `defaultdict` for data storage.
  - `data_loader`: A custom module for loading issue data.
  - `config`: Custom configuration management.
  - 'module': models json data file

> **Note**: Ensure that the `data_loader` and `config` modules are properly implemented and accessible. These might be custom modules specific to your project.