# Session 6: Team Workflow Standards and MLOps


<br>


## Activity 1: Conventional Commits, Branching and Linking Commits to GitLab

> Repo: `minions-visitorship`

#### Conventional Commits

> **Why follow a standard for commit messages?**
> - A commit message is a note to your future self and your teammates explaining what changed and why. When you're debugging a problem weeks later or onboarding someone new to the project, a well-written commit history is invaluable.
> - Following a standard structure makes the repo's commit history easier to parse by the whole team, and makes it easier to understand what each commit changed without having to read all the actual code changes.

Convention for writing commit messages (See [Conventional Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/)):

```
<type>(<optional scope>): <description>
empty line as separator
<optional body>
empty line as separator
<optional footer>
```

For example, if you are committing the addition of a new model to a ML pipeline:

- **Minimally include the commit type and a short description**
    ```
    feat: add GBT Classifier to ML pipeline
    ```

- **Most descriptive (summary + body + footer)**
    ```
    feat(pipeline): add GBT Classifier to ML pipeline

    Added Gradient Boosted Trees (GBT) Classifier as an additional model
    in the training pipeline. The model is trained with default
    hyperparameters as a baseline and evaluated alongside existing models
    using the same train-test split and metrics.

    Closes #42
    ```

<hr>

**Industry-standard Commit Types**

| Type | Use for |
| --- | --- |
| `feat` | Adding, modifying or removing a feature or analysis<br>E.g. `feat(auth): add password reset function` |
| `fix` | Bug fix<br>E.g. `fix(api): correct NA handling in cleaning script` |
| `refactor` | Restructure code without changing behaviour<br>E.g. `refactor: rewrite function to be more concise` |
| `style` | Code style changes without changing behaviour<br>E.g. `style: run prettier` |
| `chore` | Cleanup, renaming, formatting of folder structure. Maintenance tasks not affecting source or tests<br>E.g. `chore: rearrange files` |
| `docs` | Changes to documentation or README<br>E.g. `docs: update README` |

**Data-oriented Commit Types**

| Type | Use for |
| --- | --- |
| `data` | Adding, updating or removing data sources or raw files<br>E.g. `data: add 2025 vouch ticketing data` |
| `analysis` | Exploratory or ad-hoc analysis<br>E.g. `analysis: explore invalid order rows with non-NA Refunded At, Refunded Amount, Cancelled At` |
| `model` | Changes to model architecture, hyperparameters or evaluation<br>E.g. `model: add GBT Classifier pipeline` |
| `pipeline` | Changes to data pipeline or workflow steps<br>E.g. `pipeline: add feature engineering step before model training` |

We don't have to stick to the above commit types strictly. We can come up with our own ones as a team.

<hr>

**Commit often**
- At the end of every session, you should have committed any changes you made to a feature branch
- You should be committing often in general

**Atomic Commits**
- When possible, a commit should encompass a single feature, change, or fix, i.e. each commit should do **one thing** and leave the codebase in a working state
- This makes it much easier to undo or rollback **specific changes** later on. It also makes your code or project easier to review.
- E.g. If you make small edits, e.g. to global variables to run a specific analysis on a certain scope, you can commit just that change. In the future, if you were required to return to that specific analysis, you can revert just that **one commit** and not affect anything else

<hr>

#### Conventional Branching

Name your branches with a prefix that says what kind of work is on it:

- `main`: The main development branch
- `feature/` (or `feat/`): For new features (e.g. `feature/add-login-page`)
- `fix/`: For bug fixes (e.g. `fix/header-bug`)
- `hotfix/`: For urgent fixes (e.g. `hotfix/security-patch`)
- `release/`: For branches preparing a release (e.g. `release/v1.2.0`)
- `chore/`: For non-code tasks like dependency, docs updates (e.g. `chore/update-dependencies`)

See [Conventional Branch](https://conventionalbranch.org/) for more information

<hr>

#### Linking Commits to GitLab

GitLab **issues** are used to track tasks and bugs. Each issue gets a number, e.g. `#12`.

- Write `Refs #12` in the footer of a commit message to link the commit to issue `#12`. The commit then shows up on the issue's page on GitLab
- Write `Closes #12` (or `Fixes #12`) in a commit message or a merge request's description, and GitLab automatically closes issue `#12` when it is merged into `main`
- Similarly, `!5` refers to merge request number 5

<hr>

#### a. Create an issue on GitLab
- Go to the `minions-visitorship` repo on GitLab → `Issues` → `New issue`
- Title: `Add participant <N> to the team list`
- Assign it to yourself, then click `Create issue`
- Note down the issue number e.g. `#12`. We will refer to it as `#<issue>` below

#### b. Create a branch following the branch naming convention
- Run `git switch main`
- Run `git pull`
- Run `git switch -c chore/<issue>-add-p<N>-to-team main` e.g. `chore/12-add-p1-to-team`
  - `chore/`, as adding to the team list is a non-code task
  - Including the issue number in the branch name makes it easy to tell which issue the branch is for

#### c. Make your change
- Create a new file `session6_lab/team/p<N>.md`, and write your name and role in it
  - Each of you creates your own file, so there will be no merge conflicts

#### d. Write a multi-line commit message following the convention
- Run `git add session6_lab/team/p<N>.md`
- Run `git commit` to open nano, and write your commit message following the convention, e.g.:
    ```
    docs(team): add participant <N> to the team list

    Added a file for participant <N> to the team folder,
    with my name and role.

    Refs #<issue>
    ```
- Save and exit nano (`Ctrl + X`, `Y`, `Enter`)
- Run `git log -n 1` to check your full commit message

#### e. Push your branch, and check the issue
- Run `git push -u origin chore/<issue>-add-p<N>-to-team`
- Open your issue on GitLab
  - Your commit now shows up on the issue's page, as your commit message has `Refs #<issue>`

#### f. Open a merge request that closes the issue
- Open a merge request from your branch into `main`
- Title: follow the commit convention e.g. `docs(team): add participant <N> to the team list`
- Description: write `Closes #<issue>`
- Click `Create merge request`

#### g. Merge it, and check the issue
- Tick `Delete source branch`, then click `Merge`
- Open your issue on GitLab. It has been closed automatically
- Run `git switch main`, then `git pull`

<br>


## Activity 2: Organisation of Project Repository and Best Practices

#### File Naming Conventions

- Use lowercase alphanumeric characters only for filenames. Don't use special characters
- Use underscores (`_`) as separators, as spaces can cause issues in the terminal
- Be descriptive but concise. The name should convey what the file does without being a long sentence

<hr>

#### Package and Module Names (Python)

- Python **modules** (`.py` files) should have short, all-lowercase names. Underscores can be used in the module name if it improves readability
- Python **packages** (folders of modules) should also have short, all-lowercase names, although the use of underscores is discouraged by [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names)

```
my_project/
│
├── datautils/          ← package (folder, no underscores preferred)
│   ├── __init__.py
│   ├── clean_data.py   ← module (file, underscores fine)
│   └── load_data.py    ← module
...
```

<hr>

#### Folders

Organise files by function, e.g.:

- `data/`: raw and processed data files
- `notebooks/`: Jupyter notebooks for exploration and analysis
- `models/`: ML models
- `src/`: reusable Python scripts and modules
- `outputs/`: charts, tables, and other generated outputs
- `utils/`: utility package with utility functions

```
example-data-project/
├── data/
│   ├── raw/
│   └── processed/
├── datautils/
│   ├── __init__.py
│   ├── clean_data.py
│   └── load_data.py
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── main.py
│   ├── <>.py
│   └── <>.py
├── models/
└── outputs/
```

<br>

## Activity 3: Documentation

### Comments

> - Comments explain **why** the code does something. The code itself already shows **what** it does
> - Good comments explain things that aren't obvious from the code, e.g. assumptions, business rules, or workarounds:
>     ```python
>     # Exclude 2020, as all museums were closed for most of the year due to COVID
>     visits = visits[visits["year"] != 2020]
>     ```
> - Avoid:
>     - Comments that just repeat the code e.g. `# filter the year` above the line above
>     - Commented-out old code. Delete it instead, as Git keeps it in the commit history
>     - Outdated comments. When you change the code, update its comments too

### Docstrings

> - Docstrings are string literals that appear as the first statement in a module, function, class, or method, and serve as **inline documentation** that explains what a piece of code does, what it expects, and what it returns.
> - They can be accessed at runtime via the `.__doc__` attribute or the `help()` function
> - They can also power IDE tooltips (not analytics@gov unfortunately) and tools like Sphinx or `mkdocs` that can auto-generate documentation sites from your codebase

#### 1. Google style
- Most readable at a glance, and is widely used in data and ML teams

    ![Google style docstring](../../assets/docstring-google.png)

- In an IDE, hovering over the function shows its docstring as a tooltip:

    ![Docstring shown as an IDE tooltip](../../assets/docstring-tooltip.png)

#### 2. NumPy style
- Used in scientific Python libraries like NumPy, pandas, and scikit-learn
- More verbose and structured

    ```python
    def load_data(filepath: str, delimiter: str = ",") -> pd.DataFrame:
        """
        Load a CSV file into a DataFrame.

        Parameters
        ----------
        filepath : str
            Path to the CSV file.
        delimiter : str, optional
            Column delimiter. Defaults to comma.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame containing the loaded data.

        Raises
        ------
        FileNotFoundError
            If the filepath does not exist.
        """
    ```

#### Bad example
- This isn't a docstring, but a comment that just restates the same parameters readable from the function's signature, without adding any value

    ![Bad example of documenting a function](../../assets/docstring-bad.png)

### README

> - `README.md` is the first thing people see on your repo's page on GitLab. It explains the project to your teammates, and to yourself in a few months' time
> - A good README covers:
>     - **What** the project is, in one or two lines
>     - **How to set it up**, e.g. creating a virtual environment and running `pip install -r requirements.txt`
>     - **How to run it**
>     - **Project structure**: what is in each folder
>     - **Data**: where it comes from, and where to put it if it is gitignored
>     - **Configuration**: settings and `.env` variables needed (never the actual secrets)
>     - **Outputs**: what the project produces, and where
>     - **Contact**: who owns or maintains the project
> - Update the README in the same merge request as the changes it describes
> - READMEs are written in Markdown. See [The Markdown Guide](https://www.markdownguide.org) and [GitHub's guide on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

<br>


## Activity 4: Ensuring Reproducibility

#### Writing `requirements.txt`

> - A `requirements.txt` file lists all the packages (and optionally their exact versions) that your project depends on.
> - Anyone cloning your repo can use it to recreate the exact same environment by running `pip install -r requirements.txt` in their terminal. This ensures the code runs the same way on their machine as it does on yours.
>     - The `-r` flag tells pip to read the file for packages, instead of trying to install a package called "requirements.txt"

Example `requirements.txt`:

```python
# Minimally list the packages needed (don't just do this)
# It refers to the latest available versions
pandas
numpy
matplotlib
seaborn

# Best to include the specific versions for reproducibility
pandas==2.3.3
numpy==2.3.4
matplotlib==3.10.7
seaborn==0.13.2
```

<hr>

**Ways to generate a `requirements.txt`**

1. **Using the `pipreqs` module** <span style="color:salmon">(currently not working on analytics@gov)</span>
    - `pip install pipreqs`
    - `pipreqs .` scans all `.py` files in your current directory, and creates a `requirements.txt` that only includes explicitly imported packages
        - `--savepath <file>` to specify a file path to save to (default `requirements.txt`)
        - `--clean <file>` on an existing `requirements.txt` to remove libraries not actually being used in the current project
    - On analytics@gov, it has to use the ship-nexus PyPI proxy:
        ```bash
        pipreqs . --pypi-server https://ship-nexus.analytics.gov.sg/repository/pypi-proxy/simple/
        ```

2. **LLM-driven approach**
    - Step 1: Navigate to your project directory in your terminal, and run this command to list all the import statements in all `.py` files:
        ```bash
        grep -rh "^import\|^from" --include="*.py" . | sort -u
        ```
    - Step 2: Copy the output, and paste this prompt into Pair or other LLMs:
        > Below is a list of import statements in my python project, use them to generate a list of terminal commands each in the form of `pip index versions <package> --index-url https://ship-nexus.analytics.gov.sg/repository/pypi-proxy/simple/` which I can immediately copy and paste in my terminal to find the specific package versions. Only include the ones for the packages that are not already packaged with Python
        >
        > **<Replace with output from step 1>**
    - Step 3: Run the generated commands, copy their output, and paste this prompt into Pair or other LLMs:
        > Here is the output from the previous step. Use it to generate the content for me to copy and paste into my requirements.txt
        >
        > **<Replace with output from step 2>**
    - Step 4: Copy the output into your `requirements.txt`. It should look like the example above, with a specific version for each package

3. **Using `pip freeze > requirements.txt`**
    - Captures every package and exact version currently installed in your environment, including packages not used by the project
    - It will also be exceedingly verbose as it includes dependencies, which is unnecessary as pip installing a package automatically installs all its dependencies

4. **Manually writing out `requirements.txt`**
    - If all else fails, I recommend manually writing out `requirements.txt`
    - Remember to list out the packages and their specific version numbers

<hr>

To install these packages without affecting other projects on your machine, install them into a **virtual environment**, which we will create using `venv` in Activity 5 and `uv` in Activity 6.

<br>


## Activity 5: Using Virtual Environments using `venv`

> Repo: `minions-visitorship`
> Branch: `venv-p<N>`
>
> - If you don't use a virtual environment, every project on your machine shares the same installed packages e.g. analytics@gov provides `numpy==2.3.4`. If you then run a project written for a much older version e.g. the museum forecasting repo uses `numpy==1.26.4`, the code may break, as functions may have been added, removed, or changed between versions
> - A virtual environment is an isolated Python environment for one project, with its own packages and versions, independent of everything else on your machine
> - Each user (repo creator / collaborators) creates their own virtual environment. <span style="color:salmon">A virtual environment should never be committed to Git</span>, as it is very large and specific to each user's machine

First, create a branch for this activity:
- Run `cd ~/minions-visitorship`
- Run `git switch main`, then `git pull`
- Run `git switch -c venv-p<N> main`

#### a. If you are using a Mac/Linux terminal (e.g. bash, zsh) <span style="color:cyan">(Analytics@gov uses bash)</span>
- Run `which python` to see which Python you are currently using
  - It is the Python installed for your whole machine, not just this project
- Create the virtual environment:
    ```
    python -m venv .venv
    ```
  - The `-m` flag tells Python to run a module as a script. `venv` is the built-in Python module for creating virtual environments
  - `.venv` is the name of the folder containing the virtual environment (it is standard convention to use `.venv`)

<hr>

- Run `git status`
  - On older versions of Python, `.venv/` shows up under `Untracked files`. On Python 3.13 and newer, it doesn't, as `venv` automatically adds its own `.gitignore` inside the folder
- Either way, add it to your repo's `.gitignore`, so it is ignored for everyone on any Python version:
  - Open `.gitignore` at the root of the repo, and add the line `.venv/`
  - Run `git status`. Only `.gitignore` is modified
  - Run `git add .gitignore`
  - Run `git commit -m "chore: ignore .venv folder"`

<hr>

- Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```
  - You know the virtual environment is active if you see `(.venv)` at the start of your terminal line
  - You activate once at the start of each working session, and deactivate when you're done
- Run `which python` again
  - It now points inside your project e.g. `/home/jovyan/minions-visitorship/.venv/bin/python`
- Install the project's packages into the virtual environment:
    ```
    pip install -r session6_lab/requirements.txt
    ```
- Run `pip list`
  - Check that the versions of `pandas`, `numpy`, `matplotlib`, `seaborn` and `python-dotenv` match `session6_lab/requirements.txt`
- Deactivate the virtual environment when you are done:
    ```
    deactivate
    ```
  - `(.venv)` disappears from your terminal line
  - Run `which python`. You are back on your machine's Python

#### b. If you are using a Windows terminal (e.g. Windows Powershell)
The steps are the same as part a, except for these commands:

| Step | Mac/Linux | Windows (PowerShell) |
| --- | --- | --- |
| Check which Python you are using | `which python` | `where.exe python` |
| Activate | `source .venv/bin/activate` | `.venv\Scripts\activate` |

- Use `where.exe`, not `where`. In PowerShell, `where` means something else
- If activating fails with `running scripts is disabled on this system`, run this once, then activate again:
    ```
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
    ```

<br>


## Activity 6: Using Virtual Environments using `uv`

> Repo: `minions-visitorship`
> Branch: `uv-p<N>`
>
> - `uv` is a much faster alternative to `pip` and `venv`, and can also manage which **Python version** a project uses
> - Use it when a project requires a specific version of Python. Teammates running the project on their personal laptops will then all use the same Python version
> - Note: On analytics@gov, you cannot install other versions of Python, so a project should use the version analytics@gov already has

First, create a branch for this activity from your `venv-p<N>` branch, so it already ignores `.venv/`:
- If `(.venv)` is still at the start of your terminal line, run `deactivate`
- Run `git switch venv-p<N>`
- Run `git switch -c uv-p<N> venv-p<N>`

#### a. If you are using a Mac/Linux terminal (e.g. bash, zsh) <span style="color:cyan">(Analytics@gov uses bash)</span>
- Install `uv`:
    ```
    pip install uv
    ```
- Run `uv --version` to check it is installed

<hr>

**Standardise the Python version**
- Run `python --version`, e.g. `Python 3.12.3`
- Pin the project to that version (major.minor only), e.g.:
    ```
    uv python pin 3.12
    ```
  - You should see ``Pinned `.python-version` to `3.12` ``
  - This creates a `.python-version` file. Whenever anyone creates a virtual environment for this project with `uv`, it uses this Python version. On a personal laptop, `uv` even downloads that version if it is not installed yet
- Commit the file, so everyone gets the same version:
  - Run `git add .python-version`
  - Run `git commit -m "chore: pin python version"`

<hr>

**Create and use the virtual environment**
- Create a new virtual environment, replacing the one from Activity 5:
    ```
    uv venv --clear .venv
    ```
  - `--clear` is needed, as `.venv` already exists from Activity 5. Without it, you get `A virtual environment already exists at: .venv`
  - It uses the Python version in `.python-version`. You can also choose a version directly, e.g. `uv venv --python 3.12 .venv`
- Activate it the same way as in Activity 5: `source .venv/bin/activate`
- Install the project's packages:
    ```
    uv pip install -r session6_lab/requirements.txt
    ```
  - Note the use of `uv pip` instead of `pip`, as `uv` provides its own `pip`. A plain `pip` would install into a different environment
- Run `uv pip list` to check the installed packages
- Run `deactivate` when you are done

#### b. If you are using a Windows terminal (e.g. Windows Powershell)
- The steps are the same as part a, except you activate with `.venv\Scripts\activate` (see Activity 5, part b)
- Every `uv` command (`uv python pin`, `uv venv`, `uv pip install`, `uv pip list`) is the same on Windows

<br>


## Activity 7: MLOps

> **MLOps** (Machine Learning Operations) is a set of practices for taking an ML model from a notebook experiment to something that runs reliably in production, and keeping it working afterwards. It is like DevOps for ML, except you have to manage **code, data and models**, not just code.
>
> It is not one tool, but a list of practices that a team adopts step by step.

| Practice | What it means |
| --- | --- |
| Version control | Version the code, data and models, so any result can be traced and reproduced |
| Reproducible environments | Make sure the code runs the same way on any machine |
| Experiment tracking | Record each training run's settings and results |
| Automated pipelines | Run data prep → training → evaluation as code, end to end |
| CI/CD | Automatically test, then release, changes to code and models |
| Model registry | A central record of trained models, and which one is in production |
| Monitoring | Watch the model's performance in production, and detect when it gets worse |

<hr>

#### 1. Version control
Every result should be traceable to the exact code, data and model that produced it. Git handles code well, but data and models are usually too large for Git, so they need to be versioned separately.

**How to implement it in an ML project:**
- Keep all code in Git, including notebooks and scripts, not just files on your machine
- Gitignore large data files and trained models (Session 1), and store them in a shared location instead
- Version your data snapshots e.g. `visits_2025-06.csv`, or use a tool like DVC, which tracks data versions alongside your Git commits
- Record which commit and data version produced each model e.g. in the model's filename or a metadata file
- Tag the commit used for each production model e.g. `git tag v1.0`

<hr>

#### 2. Reproducible environments
The same code can give different results, or break, with different package or Python versions.

**How to implement it in an ML project:**
- Pin package versions in `requirements.txt` (Activity 4)
- Use a virtual environment for each project (Activity 5)
- Pin the Python version with `.python-version` (Activity 6)
- Fix random seeds e.g. `random_state=42` in scikit-learn, so training gives the same results each time
- Document the setup steps in the README (Activity 3)

<hr>

#### 3. Experiment tracking
While developing a model, you will train many versions with different features, hyperparameters and data. Without a record, you can't tell which run produced which result, or reproduce your best model.

**How to implement it in an ML project:**
- For every training run, record:
    - the parameters (e.g. features used, hyperparameters)
    - the metrics (e.g. RMSE, accuracy)
    - the data version, the Git commit hash, and where the model file was saved
- The simplest way is to add one row per run to a results CSV
- A tool like MLflow does this with `mlflow.log_param()` and `mlflow.log_metric()`, and gives you a UI to compare runs

<hr>

#### 4. Automated pipelines
Running notebook cells by hand only works if you remember every step, in the right order. A pipeline turns the whole path from raw data to trained model into code you can rerun with one command.

**How to implement it in an ML project:**
- Move each step from notebooks into functions in `.py` modules e.g. `load.py`, `clean.py`, `features.py`, `train.py`, `evaluate.py`
- Have one script e.g. `main.py` that runs the steps in order
- Keep settings (e.g. dates, file paths, hyperparameters) in a config file, not hard-coded in the code
- Use notebooks for exploration only, and import the functions from your modules

<hr>

#### 5. CI/CD
- **Continuous Integration (CI)**: automatically run checks, such as tests, on every push or merge request
- **Continuous Delivery / Deployment (CD)**: automatically release changes that pass the checks

This catches broken code before it reaches `main`, instead of after.

**How to implement it in an ML project:**
- Write tests for your key functions e.g. using `pytest` to check that the cleaning step removes invalid rows
- Add a `.gitlab-ci.yml` file to the repo, which tells GitLab to run your tests on every merge request. GitLab can block merging if the tests fail
- At a later stage, automatically retrain and evaluate the model, and only release it if it performs better than the current one

<hr>

#### 6. Model registry
A central place that stores your trained models, with each model's version, metrics, the code and data used to train it, and its stage (e.g. testing or production). It answers "which model is live, and how was it built?"

**How to implement it in an ML project:**
- Save each trained model with a version number e.g. `model_v3.joblib`, along with a metadata file (date, Git commit hash, data version, metrics)
- Store models in a shared location, not in Git
- A tool like MLflow's Model Registry does this, and lets you mark which version is in production
- Only promote a model to production after it has been evaluated and reviewed

<hr>

#### 7. Monitoring
A model is trained on past data, but real-world data changes over time e.g. visitor patterns change after a new exhibition opens. This is called **drift**, and it can make the model's predictions quietly get worse.

**How to implement it in an ML project:**
- Save the model's predictions, and compare them with the actual values once they are known, to track the error over time
- Compare new input data with the training data e.g. averages, ranges, missing values, and flag when they differ a lot
- Set a threshold for when the model should be retrained
- Check the data quality before making predictions

<br>


## Final Exam: Application of all previously taught Git concepts throughout the workshop

> Repo: `minions-visitorship`
> Branch: `final-main` (consider this the "main" branch for the project)

In this final exam, the 3 of you will build a project together from scratch, applying everything we have learnt throughout the workshop.

- For the sake of time, all the content and code you need is provided below. The point of this exam is purely on the Git concepts, not the code itself
- Each step only tells you **what** needs to be done, but **not** the Git or terminal commands to do it. Refer back to the reference tables and activities from Sessions 1 to 6 when you get stuck
- I will be guiding you throughout, but without handholding

#### The project
A simplified version of a museum visitorship forecasting project, except the visitors are all minions.

- It forecasts monthly visitorship for 5 NHB museums: ACM, IHC, MHC, NMS and TPM
- It trains a baseline (the historical monthly average) and 6 models for each museum: SARIMAX, Holt-Winters, SVR, Random Forest, XGBoost and LSTM
- Every function only **prints** what it would do, as the code is not the point here

`final-main` currently only contains a `README.md` with the project's title. By the end of the exam, the repo will look like this:

```
(repo root)
├── README.md
├── requirements.txt
├── .gitignore
├── .env                 ← gitignored
├── config.py
├── main.py
├── src/
│   ├── __init__.py
│   ├── fetch_singstat.py
│   ├── clean_data.py
│   ├── split.py
│   ├── features.py
│   ├── evaluate.py
│   ├── tune.py
│   ├── plots.py
│   ├── report.py
│   ├── save_models.py
│   └── forecast.py
├── models/
│   ├── __init__.py
│   ├── baseline.py
│   ├── sarimax.py
│   ├── holt_winters.py
│   ├── svr.py
│   ├── rf.py
│   ├── xgboost_model.py
│   └── lstm.py
└── outputs/             ← gitignored (plots, report, saved models)
```

#### How each task works
Unless told otherwise, follow the standard workflow for every task:

1. Create an issue for your task on GitLab, using the title and description provided
2. Create a branch off the latest `final-main`, named following the branch naming convention, and including your issue number
3. Make your changes, committing as you go. Keep your commits atomic, and write multi-line commit messages following the commit convention, referencing your issue
4. Push your branch, and open a merge request into `final-main` that closes your issue
5. Set your reviewer as both the Reviewer and Assignee of your merge request
6. **As a reviewer:** check the code, the commit messages and the merge request, run the code where possible, then approve and merge it. There is no need to delete branches

#### Rules
- The exam is split into phases. Each phase has tasks for each participant. Wait for my signal before starting the next phase
- Each phase ends with step-by-step instructions on who merges which merge request, and in what order
- Before your merge request is merged, make sure your branch has the latest `final-main` merged into it, and resolve any merge conflicts
- At the end of each phase, everyone gets the latest `final-main` and runs the pipeline. The expected output is provided
- Some phases include bugs. The phase will tell you who notices the bug and opens an issue for it, who fixes it, and provides the fix to copy

<hr>

## Phase 1: Project Setup

### <u>Participant 1</u>

#### 1. Create an issue
- Title: `Set up pipeline skeleton with baseline model`
- Description: `Create config.py, main.py and the baseline model (historical monthly average), so the pipeline trains the baseline for ACM, IHC and MHC.`

#### 2. Start writing the config
- Get the latest `final-main`, and start working straight away by creating `config.py`:
    ```python
    """Settings for the minions visitorship forecasting pipeline."""

    # Museums to forecast visitorship for
    MUSEUMS = ["ACM", "IHC", "MHC"]

    # Models to train for each museum
    MODELS = ["baseline"]

    # Features used by the models
    FEATURES = []
    ```

#### 3. Oops, you are still on `final-main`
- You realise you haven't created a branch yet. Move your uncommitted work onto a new branch for your issue, without losing it
- Commit `config.py`

#### 4. Add the baseline model
- Create an empty `models/__init__.py`
- Create `models/baseline.py`:
    ```python
    """Baseline model: the historical monthly average."""
    import time


    def train_baseline(museum):
        """Train the baseline model for one museum.

        The baseline predicts each month's visitorship as the average visitorship
        for that month in previous years. Every other model must beat it to be useful.

        Args:
            museum (str): The museum's code, e.g. "ACM".
        """
        print(f"Training baseline (historical monthly average) for {museum}")
        time.sleep(0.2)  # Pretend to take time, like real training would
    ```
- Commit your changes

#### 5. Add the pipeline
- Create `main.py`:
    ```python
    """Run the minions visitorship forecasting pipeline."""
    from config import MODELS, MUSEUMS
    from models.baseline import train_baseline
    from src.clean_data import clean_visitorship
    from src.fetch_singstat import fetch_visitorship
    from src.split import split_train_test


    def main():
        """Fetch, clean and split each museum's data, then train every model on it."""
        for museum in MUSEUMS:
            print(f"\n===== {museum} =====")
            fetch_visitorship(museum)
            clean_visitorship(museum)
            split_train_test(museum)

            for model in MODELS:
                # Each model has its own training function in the models/ folder
                if model == "baseline":
                    train_baseline(museum)


    if __name__ == "__main__":
        main()
    ```
    - Note: `main.py` uses code from Participants 2 and 3, so it will only run once their merge requests have been merged
- Commit your changes

#### 6. Document the pipeline
- Add this section to `README.md`:
    ````
    ## Pipeline

    For each museum in `config.py`, `main.py`:

    1. Fetches the monthly visitorship data from SingStat
    2. Cleans the data
    3. Splits it into training and test sets
    4. Trains each model in `MODELS`

    Run it from the repo root with `python main.py`
    ````
- Commit your changes

#### 7. Open your merge request
- Push your branch, and open a merge request into `final-main` that closes your issue
- Your reviewer and assignee is Participant 2

### <u>Participant 2</u>

#### 1. Create an issue
- Title: `Add requirements, .gitignore, and data cleaning and splitting`
- Description: `Add requirements.txt and .gitignore, and the functions to clean the data and split it into training and test sets.`

#### 2. Start writing the requirements
- Get the latest `final-main`, and start working straight away by creating `requirements.txt`:
    ```
    pandas==2.3.3
    numpy==2.3.4
    matplotlib==3.10.7
    seaborn==0.13.2
    python-dotenv==1.2.4
    ```

#### 3. Oops, you are still on `final-main`
- You realise you haven't created a branch yet. Move your uncommitted work onto a new branch for your issue, without losing it
- Commit `requirements.txt`

#### 4. Ignore files that should never be committed
- Create `.gitignore`:
    ```
    # Virtual environment
    .venv/

    # Python cache
    __pycache__/

    # Pipeline outputs (plots, reports and saved models)
    outputs/
    ```
- Commit your changes

#### 5. Add data cleaning and splitting
- Create an empty `src/__init__.py`
- Create `src/clean_data.py`:
    ```python
    """Clean the raw visitorship data."""
    import time


    def clean_visitorship(museum):
        """Clean one museum's monthly visitorship data.

        Args:
            museum (str): The museum's code, e.g. "ACM".
        """
        # Months when a museum was closed have zero visitors, and would mislead the models
        print(f"Cleaning {museum} data: removing missing months and closures")
        time.sleep(0.2)  # Pretend to take time, like real cleaning would
    ```
- Create `src/split.py`:
    ```python
    """Split the data into training and test sets."""
    import time


    def split_train_test(museum):
        """Split one museum's data into a training set and a test set by date.

        Time series must be split by date, not randomly, so the models are always
        tested on months that come after the months they were trained on.

        Args:
            museum (str): The museum's code, e.g. "ACM".
        """
        print(f"Splitting {museum} data: train on Jan 2014 to Mar 2024, test on Apr 2024 to Mar 2026")
        time.sleep(0.2)  # Pretend to take time, like real splitting would
    ```
- Commit your changes. Keep them atomic: one commit for cleaning, and one for splitting

#### 6. Document the setup
- Add this section to `README.md`:
    ```
    ## Setup

    1. Create and activate a virtual environment
    2. Install the packages in `requirements.txt`
    3. Create a `.env` file with your SingStat API key (see Data)
    ```
- Commit your changes

#### 7. Open your merge request
- Push your branch, and open a merge request into `final-main` that closes your issue
- Your reviewer and assignee is Participant 3

### <u>Participant 3</u>

#### 1. Create an issue
- Title: `Fetch visitorship data from the SingStat API`
- Description: `Fetch each museum's monthly visitorship data from the SingStat API, reading the API key from a .env file that is never committed.`

#### 2. Start writing the API call
- Get the latest `final-main`, and start working straight away by creating an empty `src/__init__.py`, and `src/fetch_singstat.py`:
    ```python
    """Fetch monthly museum visitorship data from the SingStat API."""
    import os
    import time

    from dotenv import load_dotenv

    # Read the API key from the .env file, so it is never written in the code
    load_dotenv()
    API_KEY = os.getenv("SINGSTAT_API_KEY")


    def fetch_visitorship(museum):
        """Fetch one museum's monthly visitorship data from SingStat.

        Args:
            museum (str): The museum's code, e.g. "ACM".
        """
        if API_KEY is None:
            print("Error: SINGSTAT_API_KEY not found. Add it to your .env file")
            return
        print(f"Fetching {museum} monthly visitorship from SingStat")
        time.sleep(0.2)  # Pretend to take time, like a real API call would
    ```

#### 3. Oops, you are still on `final-main`
- You realise you haven't created a branch yet. Move your uncommitted work onto a new branch for your issue, without losing it
- Commit your changes

#### 4. Store the API key safely
- Create a `.env` file at the repo root, with the API key:
    ```
    SINGSTAT_API_KEY=minions-singstat-7f3a9c
    ```
- <span style="color:salmon">`.env` must never be committed.</span> Create `.gitignore` so that Git ignores it:
    ```
    # Secrets e.g. API keys
    .env
    ```
- Check that `.env` no longer shows up as an untracked file, then commit `.gitignore` only

#### 5. Document the data source
- Add this section to `README.md`:
    ````
    ## Data

    Monthly visitorship for each museum is fetched from the SingStat API in `src/fetch_singstat.py`.

    The API key is read from a `.env` file, which is gitignored and must never be committed:

    ```
    SINGSTAT_API_KEY=<your key>
    ```
    ````
- Commit your changes

#### 6. Open your merge request
- Push your branch, and open a merge request into `final-main` that closes your issue
- Your reviewer and assignee is Participant 1

### <u>Everyone: End of Phase 1</u>

#### 1. Merge the merge requests, one at a time
Follow these steps in order. Wait for each step to be done before moving on to the next:

1. **Participant 3:** review and merge Participant 2's merge request
2. **Participant 3:** merge the latest `final-main` into your branch, and resolve the conflicts:
    - `.gitignore`: Participant 2 also created one. Keep everything from both versions
    - `README.md`: keep both your section and Participant 2's section

    Then push your branch
3. **Participant 1:** review and merge Participant 3's merge request
4. **Participant 1:** merge the latest `final-main` into your branch, and resolve the conflict in `README.md`, keeping everyone's sections. Check that the pipeline now runs, then push your branch
5. **Participant 2:** review and merge Participant 1's merge request

#### 2. Run the pipeline
Once all 3 merge requests have been merged:

- Get the latest `final-main`
- Create a virtual environment, and install the packages in `requirements.txt` (Session 6, Activities 5 and 6)
- Create your own `.env` file at the repo root, with the API key:
    ```
    SINGSTAT_API_KEY=minions-singstat-7f3a9c
    ```
- Run the pipeline. You should see:
    ```

    ===== ACM =====
    Fetching ACM monthly visitorship from SingStat
    Cleaning ACM data: removing missing months and closures
    Splitting ACM data: train on Jan 2014 to Mar 2024, test on Apr 2024 to Mar 2026
    Training baseline (historical monthly average) for ACM

    ===== IHC =====
    Fetching IHC monthly visitorship from SingStat
    Cleaning IHC data: removing missing months and closures
    Splitting IHC data: train on Jan 2014 to Mar 2024, test on Apr 2024 to Mar 2026
    Training baseline (historical monthly average) for IHC

    ===== MHC =====
    Fetching MHC monthly visitorship from SingStat
    Cleaning MHC data: removing missing months and closures
    Splitting MHC data: train on Jan 2014 to Mar 2024, test on Apr 2024 to Mar 2026
    Training baseline (historical monthly average) for MHC
    ```
    - If you see `Error: SINGSTAT_API_KEY not found`, check your `.env` file

<hr>