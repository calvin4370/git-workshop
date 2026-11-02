# Git Summary Notes

## 0. Linux and the Terminal

<aside>

The **terminal** (aka command line or shell) is a text-based interface for interacting with your computer. This is opposed to a graphical user interface like Windows Explorer that lets you click on folders to navigate.

**Linux** is an operating system kernel used in servers, cloud environments, and data engineering.  Bash is the language used in the terminal to run Linux commands.

A **Shell** is a program that reads commands you type, interprets them, and tells the OS kernel to execute them. The shell is the interface between you and the kernel.

We use the **Bash** shell. Bash is two things simultaneously:

1. **A command interpreter:** reads commands you type line by line and executes them
2. **A programming language:** has variables, conditionals, loops, and functions, so you can write scripts (`.sh` files) that automate sequences of commands 
- We write our Linux commands in **Bash**. 
Note: Bash is case-sensitive.
</aside>

### Useful Terminal Commands

- Many of the commands in the following sections require you to be in the correct working directory

| `pwd` | Show the path to your **present** working directory |
| --- | --- |
| `ls` | List files in current directory |
| `ls -a` | List all files including hidden ones (e.g. `.git` folder) |
| `ls -la` | List all files with details (permissions, size, date) |
- In Bash, `-` and `--` are used to pass **flags** to commands. Flags modify how a command behaves.
    - **Double dash `--`** is used for long-form flags that are full words. These are more readable and self-explanatory:
        
        ```bash
        git log --oneline        # same as git log -o
        git commit --amend       # no short form version
        ```
        
    - **Single dash `-`** is used for short, single-character flags. Many long-form flags have short versions. You can also chain multiple single-character flags together
        
        ```bash
        ls -a          # show hidden files (short for --all)
        ls -l          # show detailed list
        ls -la         # both combined
        ```
        
    - To find documentation on what flags are available, see [Git - Reference](https://git-scm.com/docs)
    Alternatively, run `<command> --help`, e.g. `git commit --help`, `git push --help`. Note: This may not work on Analytics@Gov as the command manuals are not available.

**Navigation**

- Use these commands to navigate to the correct location before using git commands

| `cd <folder>` | Move into a folder or path |
| --- | --- |
| `cd ..` | Move up (back) one folder |
| `cd ../<folder>` | Move up (back) one folder then enter a folder or path there |
| `cd ~` | Go back to your home directory (e.g. for analytics@gov its `/home/jovyan`) |
| `cd /` | Go back to your root directory (`/`) |
| `cd -` | Go back to the previous directory you were in (back button) |

**Working with files and folders**

| `mkdir <folder>` | Create a folder in the present working directory |
| --- | --- |
| `touch <file>` | Create a new empty file |
| `cp <file> <destination>` | Copy a file to the destination path |
| `mv <file> <destination>` | Move a file to the destination path |
| `rm <file>` | Delete a file |
| `rm -r <folder>` | Recursively delete a folder and everything in it
⚠️ There is no recycle bin for the terminal. `rm` permanently deletes files immediately. |

| `clear` | Clear the terminal screen (deletes all lines) |
| --- | --- |
| `history` | Show command history |

**Useful Terminal Keyboard Shortcuts**

| `Tab` | Autocomplete a file or folder name |
| --- | --- |
| `↑` / `↓` | Scroll through previous commands |
| `Ctrl + C` | Cancel a running command |
| `Ctrl + L` | Clear the terminal screen (by moving your cursor and screen view to the bottom, without actually clearing the lines) |
| `Ctrl + A` | Jump to the start of line |
| `Ctrl + E` | Jump to the end of line |

## 1. Git Environment Setup

<aside>

**Configure your Git identity**

```bash
git config --global user.name "short_username"
git config --global user.email "your_email@agency.gov.sg"

# set your default terminal text editor for git commit
git config --global core.editor nano
```

**Verify your config** 

```bash
git config --list
```

</aside>

<aside>

**Set up your Gitlab Personal Access Token (PAT)**

- GitLab → Profile Avatar (top-right) → Edit profile → Click the menu dropdown at the top-left of your screen → Access → Personal access tokens
    
    ![image.png](c9879a95-9339-4449-ad86-1cbc35d1b1dd.png)
    
    - Scopes needed: `read_repository`, `write_repository` (actually best to just tick all)
        - Scope also mean “Access Control” parameters (i.e. what actions you can do)
    - These scopes set the permission levels granted, which allow the PAT to authorise certain actions
- Store it somewhere safe, Gitlab will not show you this code again
- PAT is required for pushing and pulling from Gitlab
</aside>

<aside>

**Storing and referencing your PAT when pushing / pulling**

- **Options available for use with Analytics@Gov**
    1. **Using a .txt file (Notepad)**
        - Simply store your PAT in a .txt file on disk and copy paste from it every time you need it.
        - This is not secure as its left unencrypted and out in the open.
        - Alternatively, save it in a google docs / word somewhere online. This is still inconvenient and troublesome to copy paste your PAT every time
    2. **Git credential store**
        - `git config --global credential.helper store`
        - After running this command, you will **still need to authenticate your next push/pull with your username + PAT once**, but they will then be stored in **plaintext** to `~/.git-credentials` (in your home directory on Analytics@Gov)
        - Subsequently, whenever these credentials are needed, git will automatically read from the saved file
        - This method is persistent across sessions but is not that secure as your PAT is stored unencrypted, in your analytics@gov home directory. However, this way is more convenient than the .txt method as you don’t need to copy paste your PAT every time.
        
        **If you update your PAT**, simply delete the `.git-credentials` file in your jovyan home directory, and rerun `git config --global credential.helper store`
        
- **Other more secure options**
    1. **OAuth via git-credential-manager**
        - **Windows**: git-credential-manager is automatically packaged with an installation of git. However, curiously it is not available in analytics@gov and can’t be installed there. For Mac and Linux devices, this needs to be downloaded separately.
        - **Steps**
            1. **Point git at GCM**
            On macOS and Windows the installer does this automatically — on macOS you don't need to run git config because GCM configures Git for you.
            
            ```bash
            # To do it explicitly
            git-credential-manager configure
            
            # verify
            git config --global --get-all credential.helper   
            # should show "manager"
            ```
            
            1. **Clear any old PAT stored using `git credential store` or `cache`**
            
            ```bash
            git credential-store erase
            ```
            
            1. **Trigger the OAuth flow once manually**
            E.g. using git clone, git push or git pull. You will need to authenticate on GitHub/GitLab once. Subsequently, all further HTTPS operations are automatically authenticated, while your PAT stays secure. 
</aside>

## 2. Cloning a repository

<aside>

**Terms:**

- **Remote repo**: The version of your repository hosted on GitLab / Github. This is the central copy that your whole team pushes to and pulls from.
- **Local repo**: The version of your repository on your own machine. This is where you make changes before pushing them up to the remote.
</aside>

<aside>

**Clone an existing GitLab repo**

- Do this once per project to get a remote GitLab repo onto your machine.
- You can copy the HTTPS address from Gitlab

![image.png](image.png)

```bash
git clone https://<your-gitlab-instance>/<team>/<repo>.git
```

- This saves the repo as a folder in your current working directory
</aside>

<aside>

**Alternatively, initialise a git repo locally, then link to GitLab**

1. **Initialise a git repo locally**
    
    ```bash
    git init
    git branch -m master main  # rename the "master" branch to "main"
    
    git add .
    git commit -m "initial commit"
    ```
    
    - Note: `git remote add origin` by default sets the first branch in the newly initialised repo to be called `master`. Nowadays, it is standard to name the main branch `main`
2. **Create an empty repo on GitLab**
    - GitLab → Create Project → Create blank project → uncheck "initialise with README”
    - This ensures the remote repo is created empty, else there will be an error when you try to link to your git repo and you will not be able to push your local repo to Gitlab
3. **Link your local repo to GitLab and push**
    - Get the HTTPS address from Gitlab and use `git remote add origin <HTTPS address>` to link the local repo to GitLab
    
    ```bash
    git remote add origin https://<your-gitlab-instance>/<team>/<repo>.git
    git push -u origin main  # push the local main branch to remote
    ```
    
</aside>

<aside>

**Check your remote is configured correctly**

```bash
git remote -v
```

**Expected output:**

![image.png](image%201.png)

These should match the url of the repo on Gitlab (without the .git):

![image.png](image%202.png)

</aside>

## 3. Local Workflow

<aside>

#### The 4 Areas of Git

![git-4-areas.png](git-4-areas.png)

</aside>

<aside>

**Git commands (main)**

```bash
git add <file>                    # stage a specific file
git add file1 file2 file_n        # stage a variable number of files at once
git add .                         # stage everything
git commit -m "commit message"    # commit staged changes
```

**Other commit commands**

```bash
git commit       # opens a nano window for you to write multi-line commit messages
git commit --amend -m "corrected message"    # rewrite message for the last commit
```

- **How to write multi-line commit messages?**
    
    <aside>
    
    Run `git commit` just like that to open a nano window for writing the commit message
    
    ![image.png](image%203.png)
    
    Write your multi line message in the space provided
    
    ![image.png](image%204.png)
    
    Press `Ctrl + X` to exit the nano window. If a commit message has been written, it will automatically commit
    
    </aside>
    
</aside>

<aside>

**Checking State**

```bash
git status                     # see what's changed
```

- `git status` shows which files have been staged or committed. Use this to check which files will be affected before you push
- It can also be used to check if the current folder is a local git repository

```bash
git log                        # view commit history
git log --oneline              # view commit history (condense each into one line)
```

</aside>

<aside>

**Ignoring Files**

We can tell Git which files and directories to ignore in a given repository, using a `.gitignore` file. This is useful for files you know you NEVER want to commit, including:

- Secrets, API keys, credentials (e.g. `.env`)
- Operating System files (`.DS_Store` on Mac)
- Log files (`*.log`)
- Dependencies & packages (e.g. `node_modules/` for node applications, `__pycache__/` for python)
- `.venv/` , `.ipynb_checkpoints/`
- **Syntax**
    
    ```bash
    # This is a comment
    
    # Ignore a specific file
    test.py
    
    # Ignore all files of a specific file type (.csv)
    *.csv
    
    # Ignore a whole folder
    data/
    
    # Ignore a folder's contents but not the folder itself
    data/*
    
    # Ignore everything in a folder except one file 
    # (order of entries DOES matter, put your exceptions after the wide ignore)
    data/*
    !data/keep_this.csv
    
    # Ignore a file only in the root directory
    /config.json
    
    # Ignore a file in any subdirectory
    **/config.json
    ```
    
- **Sample `.gitignore`**
    
    ```bash
    __pycache__/
    
    # Do not save input data
    *.csv
    *.xlsx
    
    # But DO save output data
    # Output data is usually exported to a folder named f"{YEAR} output"
    !*output/*.csv
    !*output/*.xlsx
    
    # Note: *output/ refers to any folder with name ending in "output"
    # so a folder named "2024 output" would get caught
    ```
    

```bash
# Show which line of which .gitignore is causing a file to be ignored
git check-ignore -v <file>
```

</aside>

## 4. Remote Workflow

<aside>

```bash
git push
```

- Push committed changes to GitLab

```bash
git push -u origin <branch>
```

- **When pushing from any new branch for the first time**, you must run this to set `<branch>` as the upstream branch to push to
    
    <aside>
    
    - `-u` : short for `--set-upstream`. This tells Git to remember the relationship between your local branch and the remote branch, so that future pushes and pulls on this branch only need `git push` or `git pull` with no extra arguments.
    - `origin` : the name of the remote you're pushing to. This is the alias for your GitLab repo URL, set when you cloned or ran `git remote add origin <url>`. So you do not have to rewrite the whole url.
    - `<branch>` : name of the branch you are pushing, e.g. `main`, `feature/user-guide`. This creates the branch on the remote if it does not exist yet.
    </aside>
    

### **Fixing problems preventing you from pushing**

<aside>

**Git does not allow you to push local changes to a remote branch that is ahead of your local branch**

- If the remote branch has commits that your local branch does not have, the remote branch is ahead of your local branch by that many commits, e.g. because your teammate pushed some changes to that branch

**Solution:**

- **Pull the remote changes first**. Then your local branch is strictly ahead of remote (by your latest changes). You can then push as normal.
</aside>

<aside>

**Unrelated commit histories between branches / repos**

- Occurs when Git is asked to combine two branches / repositories with that **do not share a common ancestor commit**
- Git will not allow this as it cannot treat one commit history as a continuation of the other
- E.g. You have a project folder which you just initialized with a git repo. You then create a new Gitlab repo, while mistakenly ticking the option to add a README. You  `git remote add <...>` to link the 2 repos
    - When you try to git push the code, Git throws `error: failed to push some refs to '...' hint: Updates were rejected because the remote contains work that you do not have locally.` because of the README added when the Gitlab repo was created.
    - When you try to git pull to get the README, Git throws `fatal: refusing to merge unrelated histories`

**Solution:**

- Insist on pulling remote changes with `git pull --allow-unrelated-histories`
- Then push your local changes as normal
</aside>

</aside>

<aside>

```bash
git pull
```

- Fetches and merges the equivalent <u>**remote branch**</u> into your <u>**local branch**</u>, equivalent to running both `git fetch` and `git merge`
    - Note: if you are on a feature branch, say `model/xgboost`, git pull fetches and merges the changes to the remote `model/xgboost` and merges them into your local branch,
- Before starting work, always run `git pull` while on the local main branch to make sure you are working with the latest version of the codebase.

```bash
git pull origin main
```

- Run to explicitly fetch and merge changes **from `main` into your current branch.**
- Before continuing work on a feature branch, always run `git pull origin main` to make sure you pull any new commits your teammates merged into main.

### **Fixing problems preventing you from pulling**

<aside>

**Git does not allow you to pull remote changes that would cause a merge conflict with your local <u>uncommitted</u> changes**

- E.g. You run a notebook, which causes uncommitted changes it’s metadata regardless of whether there were any changes to exported output. A teammate then pushes code to that branch which you try to pull.
- Normally, when merging (e.g. through git pull), Git will automatically merge changes if possible and prompt you to address merge conflicts if necessary, between your local <u>**commits**</u> and remote changes
- However, it will not allow you to pull remote changes that would cause a merge conflict with your local <u>**uncommitted**</u> changes

**Solutions:**

1. **Commit your local changes**. Then you can pull remote changes and then Git will allow you to manually resolve merge conflicts.
2. **Discard your local uncommitted changes** using `git restore .`
3. **Stash your local uncommitted changes using** `git stash` if you don’t want to discard them. Then you can pull remote changes, and `git stash pop` to retrieve your uncommitted changes.
</aside>

</aside>

<aside>

```bash
git fetch
```

- Updates your local knowledge of what remote branches are on Gitlab
- Essentially it only downloads remote changes, but unlike `git pull`, it does not merge the changes, so it does not touch your working directory
- **Sample output**
    
    ![image.png](image%205.png)
    
    - This shows there is currently only the `main` branch on the remote repo
</aside>

### Conflict Resolution

<aside>

### Merge Conflicts

A merge happens whenever two lines of development need to be combined:

- When you run `git pull` (this combines fetch + merge)
- When you accept a MR on GitLab
- When you run `git merge` directly in the terminal
- Note: `git push` can never cause a merge conflict as Git will not allow you to push if the remote branch is ahead of your local branch (you will have to pull first)

This can result in a **merge conflict** if two branches changed the same part of the same file and Git cannot automatically merge them. You will have to manually resolve this.

</aside>

<aside>

### Resolving Conflicts

- Git will mark the conflicting lines in affected file(s):
- I recommend using the VSCode (code server) view provided by analytics@gov for this as it provides a readable UI to compare changes when resolving merge conflicts

**VSCode view:**

![image.png](image%206.png)

1. Open the file and decide what the final version should look like
2. Remove all the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
3. Save the file, then:
    
    ```bash
    git add <file>
    git commit -m "fix: resolve merge conflict in <file>"
    ```
    
</aside>

<aside>

### Rebase Conflicts

A rebase TODO

</aside>

## 5. Branching

<aside>

**Git Commands**

- Use `git branch` to list your local branches, it will **highlight your current branch**

```bash
git branch                    # list local branches
git branch -a                 # list all branches including remote branches

git branch <branch>           # create a new local branch named <branch>

git branch -d <branch>        # delete a branch locally
git branch -D <branch>        # FORCE delete a branch locally (even if not merged)
git push origin -d <branch>   # delete a branch on the remote (*dangerous*)
```

```bash
git switch <branch>            # switch to an existing local branch
git switch -c <branch>         # create and switch to a new branch (from current)
git switch -c <branch> main    # create and switch to a new branch (from main)
```

- **If you are creating a new feature branch, make sure to branch off from main!**
    
    <aside>
    
    - This means you should `git switch main` then `git switch -c <new-branch>`
    - or `git switch -c <new-branch> main`
    - Otherwise, you will be branching from your current branch, which may or may not be what you are intending, so be aware.
    </aside>
    
- FYI, an older alternative command: `git checkout`
    - This is an older command that is considered overloaded as it does a lot of different things
    - `git switch` and `git restore` were subsequently introduced to split apart `git checkout`‘s roles, so it is best to use them instead
    - FYI as many older tutorials still teach `git checkout`
    
    ```bash
    # 1. Switching branches
    git checkout <branch>
    
    # 2. Creating a branch and switching
    git checkout -b feature/new-dashboard
    
    # 3. Restoring a file
    git checkout -- <file-path>
    
    # 4. Detached HEAD state
    git checkout abc1234        # a commit hash, not a branch name
    ```
    

**Accessing remote branches with fetch**

- If you currently do not have a copy of the remote branch locally, running `git switch` to access the remote branch will not worku as your local repo has no knowledge of the remote branch
    
    <aside>
    
    **Example:**
    
    - Your teammate pushed a feature branch “hyperparameter-tuning” to remote
    - They told you they did that, and you are to continue working on their branch
    - If you simply run `git switch hyperparameter-tuning`, it will not work as your local repo has no knowledge of that remote branch. Running `git branch` will also not show that branch.
    - After running `git fetch`, this downloads all new remote changes, and gives you local branches (of those remote branches)
    - You can now `git switch` to the new feature branch locally or use `git branch` to see them
    </aside>
    
    - To fix this, run `git fetch`:
        - This shows you what remote branches are in Gitlab
        - Also updates your local knowledge on what remote branches are on Gitlab, so that you can run `git switch <branch>` to access a local copy of the remote branch
- **Why not just run `git pull`?**
    
    <aside>
    
    - `git pull` fetches all remote changes **and <u>merges remote changes for your current branch</u>**, which may be an extra step you don’t want to do yet.
    - `git fetch` only downloads everything from the remote for all new branches and commits, giving your local repo full knowledge of what exists on GitLab, so that you can access a local copy of the new remote branch without affecting the local branch you were previously working on
    </aside>
    
</aside>

<aside>

**Branch Naming Convention**

- `main`: The main development branch
- `feature/` (or `feat/`): For new features (e.g. `feature/add-login-page`)
- `fix/`: For bug fixes (e.g. `fix/header-bug`)
- `hotfix/`: For urgent fixes (e.g. `hotfix/security-patch`)
- `release/`: For branches preparing a release (e.g. `release/v1.2.0`)
- `chore/`: For non-code tasks like dependency, docs updates (e.g. `chore/update-dependencies`)
</aside>

<aside>

**Example workflow for working on a feature**

```bash
# 1. Switch to local main, and pull the most recent remote main
git checkout main
git pull origin main

# 2. Create and switch to a new feature branch
git switch -c feature/visitor-forecast-model

# 3. Do your work, then stage and commit your changes
git add .
git commit -m "model(sarimax): add SARIMAX baseline for visitor forecasting"

# 4. Push your local branch to remote
git push origin feature/visitor-forecast-model

# 5. Open a Merge Request (GitLab) / Pull Request (GitHub) from the browser
```

</aside>

<aside>

**Why use branching?**

- Branching lets you create a separate line of work that diverges from `main` without affecting it.
- This allows you to:
    - work on something unfinished without breaking what already works
    - if something goes wrong, you can simply delete the branch instead of having to manually find and revert bad changes
    - many people can work in parallel without getting in one another’s ways
- `main` should always be in a working state (production). Branches are for development of messy or work in progress
- See [Conventional Branch](https://conventionalbranch.org/) for more information
</aside>

### Working Across Branches

<aside>

**Merging Branches**

- 

<aside>

- **Example**
    - 
</aside>

</aside>

<aside>

**Applying commits**

```bash
git cherry-pick <hash>                  # Apply the commit to the current branch
git cherry-pick <hash1> <hash2> <hash3> # You can apply many commits at a time
```

- `cherry-pick` creates **new commit(s)** with the changes applied by the commit(s) given
- **Available flags:**
    
    <aside>
    
    - By default, the new commit(s) will have the same commit messages as the original(s).
    Use `--edit` to specify a different commit message for one commit
    - Cleaner way to apply commits: `git cherry-pick **--no-commit** <hashes ...>`
        - `--no-commit` applies the commits to your workspace and stages them. Once you are ready, you can commit your code as normal
    - `-x` : appends a line to the commit message like `(cherry picked from commit abc1234)`, so anyone can trace the original branch’s commit easily
    </aside>
    

<aside>

- **Example**
    - 
</aside>

</aside>

<aside>

**Git Stash**

- Use `git stash` to temporarily set aside **uncommitted changes** without committing them.

```bash
git stash                  # stash your current uncommitted changes
git switch <other-branch>

# -------------------------------------------------- #
# do your urgent work in another branch... ╭(•ᴗ•)╮
#                                           _| |_
# -------------------------------------------------- #

git switch <your-branch>
git stash pop              # restore most recent stash and remove from stash list
```

- Stashing is a way to temporarily set aside **uncommitted** changes without committing them. It's useful when you are in the middle of working in one branch but urgently need to attend to another branch.
- By default, `git stash` captures **modified tracked files and staged changes**, but not untracked files (new files you haven't `git add`ed before) and git ignored files.

| `git stash` | Saves your local modifications away and reverts the working 
directory to match the `HEAD` commit.
(Note: Untracked files like newly added files are not included) |
| --- | --- |
| `git stash -u` | Also include untracked files |
| `git stash push -m "message"` | Also include a message to tell stashes apart |
| `git stash list` | Shows all your stashes |
| `git stash pop` | Restore **most recent** stash and <u>**remove**</u> from stash list |
| `git stash apply` | Restore **most recent** stash <u>**without removing**</u> from stash list |
| `git stash drop <hash>` | Delete a single stash entry from the list of stash entries. |
| `git stash clear` | Delete all the stash entries. Note that those entries will then be subject to pruning, and may be impossible to recover |
</aside>

## 6. Merge Requests and Code Review

<aside>

As we learnt from Section 5 on Branching, we do not commit our changes straight to `main` to prevent any bad changes from making it straight into production.

Instead, we work on feature branches, until we finish a feature or set of specific changes. Once we are happy with it, we will merge our feature branch into main to merge in our changes.

- **The workflow for doing this is as follows:**
    
    <aside>
    
    1. **We create a feature branch off main, say `pipeline/add-models`**
    2. **We work on our changes in the branch, staging and committing changes locally as we go**
        - By commiting changes, they are tracked locally in your local git repo
        - Your teammates cannot see them yet, as all they can see is their own local repo, and the remote repo on GitLab
    3. **Once we are done (or any time in between commits), we can push our commits to remote**
        - This pushes the feature branch to the remote repo on GitLab where everyone in the team can see the code
        - They can see the changes on the web, or even pull the branch to work on the code locally
    4. **To merge the feature branch into `main` (or any other branch), we initialise a merge review on GitLab from our browser.**
    5. **To merge the feature branch into main (or any other branch), we initiate a merge review on GitLab from our browser.**
    6. **A reviewer, typically someone else on the team, will go through the changes in the feature branch**
        - They can leave comments, approve or disapprove the merge request
        - If the merge request is approved, the feature branch's changes can be merged into main
        - This updates the main branch remotely, and other team members need to pull the main branch to get the changes locally.
    </aside>
    
</aside>

<aside>

### **Author: Opening a MR for branch → main**

- **GitLab**
    1. Push your branch to remote using `git push` (or `git push -u origin <branch-name>` if pushing from a new feature branch for the first time)
    2. Go to the repo page on GitLab, a prompt should appear immediately and persist for recent pushes to the remote repo
        
        ![image.png](image%207.png)
        
        Or if the prompt is not there anymore, create the MR manually
        `GitLab → Your repo → **Merge Requests → New Merge Request**`
        
    3. Set **source branch** to the feature branch, and **target branch** to `main`
        
        ![image.png](d03bd9b0-4421-4a04-8ddc-6de89f4c2b99.png)
        
    4. Fill in the MR description
    5. Assign a Reviewer
    6. Click **`Create Merge Request`**
- **GitHub**
    
    Merge requests are called <u>**Pull requests (PR)**</u> in GitHub. Otherwise, PRs in GitHub are essentially the same thing as in GitLab
    
    1. Push your branch using `git push` (or `git push -u origin <branch>` if pushing from a new feature branch for the first time)
    2. Go to the repo page on GitHub, a prompt should appear immediately
        
        ![image.png](image%208.png)
        
        Or if the prompt is not there anymore, create the PR manually
        `GitHub → <Your repo page> → "Pull requests" tab → "New pull request" button`
        
        ![image.png](image%209.png)
        
    3. **base** should be `main` and **compare** should be the feature branch you are merging
        
        ![image.png](image%2010.png)
        
    4. Fill in the PR description
    5. Assign Reviewer(s)
    6. Click **`Create pull request`**
</aside>

<aside>

### **Reviewer: Reviewing a MR**

This process is the same for MRs on GitLab and PRs on GitHub

```html
git fetch
git switch <branch-name>
```

1. Run `git fetch` to get local knowledge on what remote branches are on GitLab
2. Run `git branch -r` to list the remote branches
    - You will see something like `origin/<branch-name>` 
    (origin is the alias for the remote address)
3. Run `git switch <branch-name>` to get a local copy tracking the remote branch
    - For example, typing `git switch fix/sarimax`  (without the prefix `origin`
    - The output looks likes below
    
    ```
    branch 'fix/sarimax-bug' set up to track 'origin/fix/sarimax-bug'.
    Switched to a new branch 'fix/sarimax-bug'
    ```
    
4. Now that you have a local copy of the branch, run the code and make sure all the objectives are met
5. Approve / reject the merge request and leave comments

Notes:

- If you run a brand new `git clone <repository>` , the newly cloned repository will have all the branches and commits from the remote repository. By running `git branch -r` will list all remote repositories at the time of `git clone`.
- Looking at `git branch -r` output `origin/fix-sarimax-bug`, do remember to delete the prefix `origin/` when switching branches. At local repository, the branch name will look like `fix/sarimax-bug`
</aside>

<aside>

### **Assignee: The one who actually merges**

- Could also be the Author or Reviewer
- From the Author perspective and if you want your code to be reviewed, set the `Assignee` to `Reviewer` right after the Pull Request is created. This is to trigger a notification to the `Reviewer` via GitHub or Email
</aside>

## 7. Safe Undo of Code Changes

<aside>

**Background info:**

- **Untracked** files are files that have never been staged to Git (`git add`), such as a new file or new pipeline outputs.
    - Git doesn't track their changes, and `git restore` ignores them.
    - Once you stage a new file, they become **tracked** by Git
- **Unstaged** changes are edits to tracked files that you have not staged yet. They exist only in your working directory.
- **Uncommitted** changes are **staged** changes you have not committed yet. They're held in the *staging area* until you commit them**.**
- **Committed changes** are saved permanently in the repo's history as a snapshot.
- **Pushed changes** are commits uploaded to a remote repo such as one hosted on GitHub, where other people can pull them.
</aside>

<aside>

### **Safe Undo**

| `git restore --staged <file>`
`git restore --staged .` | Unstage a specific staged file (keep changes)
Unstage all staged files in the current directory |
| --- | --- |
| `git restore <file>`
**`git restore .`** | Discard unstaged changes in a file (resets it to staged version)
**Discard all <u>unstaged</u> changes in working directory**
(these do not affect untracked changes) |
| `git clean -fd`
`git clean -nd` | Delete untracked files and folders
Dry run of the above command (shows what would be deleted) |
| `git reset --soft HEAD~1` | Undo last commit (keep changes staged) |
| `git reset --mixed HEAD~1` | Undo last commit (keep changes unstaged) |
| `git reset --hard HEAD~1` | Undo last commit (delete changes) |
| `git checkout commit <hash>` | View the state of the repo at a previous commit |
| **`git revert <hash>`** | Revert a pushed commit by performing a new commit that **inverses** the input commit (safe for shared branches on remote as it adds a new commit instead of rewriting commit history) |
- **Never use `git reset` on commits that have already been pushed to a remote branch**, as this rewrites remote commit history that others may have already pulled, which will cause a git mess for your collaborators
- **Use `git revert` instead** as it undoes the change by adding a new commit rather than
rewriting remote commit history
</aside>

<aside>

- **Common cases for safe undoing of code changes**
    - First, run `git log --oneline` while in the desired branch to get a list of commit hashes.
        
        ![image.png](image%2011.png)
        
    1. **You just want to <u>see</u> the code at the point of a specific commit**
        
        <aside>
        
        ```bash
        git checkout <commit-hash>
        ```
        
        - This moves HEAD to that commit and updates your working directory to that snapshot. This is useful for quickly inspecting an old version of your project. You land in a **detached HEAD** state (where HEAD points at a commit instead of a branch, so any new commits you make here aren't on any branch). To leave and go back: `git switch -`
        </aside>
        
    2. **You want to go back completely and <u>discard everything after that commit</u>**
        
        <aside>
        
        ```bash
        git reset --hard <commit-hash>
        ```
        
        - `reset` moves the current branch pointer to `<commit>`
        - The `--hard` flag also forces the working directory and staging area to match it, so everything after that commit is thrown away.
        - **This is a destructive command**, those changes CANNOT be restored afterward.
        </aside>
        
    3. **You want to <u>undo the effect of just that one commit</u> but keep the rest of the commit history the same**
        
        <aside>
        
        ```bash
        git revert <commit-hash>
        ```
        
        - This creates a new commit that cancels out the changes made in the original commit
        - Use the flag `--no-edit` to skip the commit-message editor
        </aside>
        
    4. **You want to <u>undo</u> the last commit but <u>KEEP the changes</u> in your working directory**
        
        <aside>
        
        ```bash
        # CHOOSE ONE:
        # undo last commit, keep changes STAGED
        git reset --soft HEAD~1    
        
        # undo last commit, keep changes UNSTAGED (this is the default)
        git reset --mixed HEAD~1   
        ```
        
        </aside>
        
    5. **You want to discard your <u>uncommitted</u> changes**
        
        <aside>
        
        ```bash
        git restore <file>     # discard uncommitted changes to <file>
        git restore .   # discard uncommitted changes to all files in pwd
        
        # unstage <file>, but keep changes
        git restore --staged <file>
        
        # set <file> to its state at <commit>
        git restore --source=<commit> <file>
        ```
        
        </aside>
        
</aside>

## 8. Team Workflow Standards

### Branching

<aside>

**Keeping main branch in a constant state of production**

- `main` should always be in a working state (production branch). As such, never work directly on your local main branch and do not push changes straight to remote `main`
- Whenever adding a new feature / change, branch off from `main` and push changes to that branch.
- As often as possible, pull the latest changes from main into your feature branch to ensure you are kept up with the latest state of main, using [`git pull origin main`](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?pvs=21)
- When ready to merge your changes to `main`, do not do it directly via `git merge`. Instead, open a merge request on GitLab and request review from teammates to ensure only working code is ever merged into `main`
</aside>

### **Commits**

<aside>

**Commit often**

- At the end of every session, you should have committed any changes you made to a feature branch
- You should be committing often in general

**Atomic Commits**

- When possible, a commit should encompass a single feature, change, or fix. 
i.e. each commit should do **one thing** and leave the codebase in a working state
- This makes it much easier to undo or rollback **specific changes** later on. It also makes your code or project easier to review.

<aside>

**E.g.**

- If you make small edits, e.g. to global variables to run a specific analysis on a certain scope, you can commit just that change
- In the future, if you were required to return to that specific analysis, you can revert just that **one commit** and not affect anything else
</aside>

</aside>

<aside>

**Commit Conventions**

See [Conventional Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/))

```html
<type>(<optional scope>): <description>
empty line as separator
<optional body>
empty line as separator
<optional footer>
```

- **Why follow a standard for commit messages?**
    - A commit message is a note to your future self and your teammates explaining what changed and why. When you're debugging a problem weeks later or onboarding someone new to the project, a well-written commit history is invaluable.
    - Following a standard structure makes the repo’s commit history easier to parse by the whole team, and makes it easier to understand what each commit changed without having to read all the actual code changes.
- **For example, if you are committing the addition of a new model to a ML pipeline**
    
    <aside>
    
    **Minimally include the commit type and a short description**
    
    ```html
    feat: add GBT Classifier to ML pipeline
    ```
    
    **Most descriptive (summary + body + footer)**
    
    ```html
    feat(pipeline): add GBT Classifier to ML pipeline
    
    Added Gradient Boosted Trees (GBT) Classifier as an additional model
    in the training pipeline. The model is trained with default 
    hyperparameters as a baseline and evaluated alongside existing models 
    using the same train-test split and metrics.
    
    Closes #42
    ```
    
    </aside>
    

**Industry-standard Commit Types**

| **Type** | **Use for** |
| --- | --- |
| `feat` | Adding, modifying or removing a feature or analysis
E.g. `feat(auth): add password reset function` |
| `fix` | Bug fix
E.g. `fix(api): correct NA handling in cleaning script` |
| `refactor` | Restructure code without changing behaviour
E.g. `refactor: rewrite function to be more concise` |
| `style` | Code style changes without changing behaviour
E.g. `style: run prettier` |
| `chore` | Cleanup, renaming, formatting of folder structure. Maintenance tasks not affecting source or tests.
E.g. `chore: rearrange files` |
| `docs` | Changes to documentation or README
E.g. `docs: update README` |

**Data-oriented Commit Types**

| **Type** | **Use for** |
| --- | --- |
| `data` | Adding, updating or removing data sources or raw files. 
E.g. `data: add 2025 vouch ticketing data` |
| `analysis` | Exploratory or ad-hoc analysis. 
E.g. `analysis: explore invalid order rows with non-NA Refunded At, Refunded Amount, Cancelled At` |
| `model` | Changes to model architecture, hyperparameters or evaluation. 
E.g. `model: add GBT Classifier pipeline` |
| `pipeline` | Changes to data pipeline or workflow steps. 
E.g. `pipeline: add feature engineering step before model training` |

We don’t have to stick to the above commit types strictly. We can come up with our own ones as a team. See [Section 8: Team Workflow Standards](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?pvs=21)

</aside>

### Documentation

<aside>

**Inline Comments**

</aside>

<aside>

**Docstrings**

- Docstrings are string literals that appear as the first statement in a module, function, class, or method, and serve as **inline documentation** that explains what a piece of code does, what it expects, and what it returns.
- They can be accessed at runtime via the `.__doc__` attribute or the `help()` function
- They can also power IDE tooltips (not analytics@gov unfortunately) and tools like Sphinx or `mkdocs` that can auto-generate documentation sites from your codebase
- **1. Google style**
    - most readable at a glance and is widely used in data and ML teams
    
    ![image.png](image%2012.png)
    
    ![image.png](image%2013.png)
    
- **2. NumPy style**
    - used in scientific Python libraries like NumPy, pandas, and scikit-learn
    - more verbose and structured
    
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
    
- **Bad examples**
    
    This isn’t a docstring but it's a comment that just restates the same parameters readable from the method signature, without value adding
    
    ![image.png](image%2014.png)
    
</aside>

<aside>

**README and documentation**

- Useful References
    
    <aside>
    
    - [GitHub's guide on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
    - [The Markdown Guide](https://www.markdownguide.org) (for Markdown syntax)
    </aside>
    
</aside>

### Project Repository: Organisation and Best Practices

<aside>

**File Naming Conventions**

- **General guidelines**
    
    <aside>
    
    - Use lowercase alphanumeric characters only for filenames. Don’t use special characters
    - Use underscores (`_`) as separators as spaces can cause issues in the terminal
    - Be descriptive but concise, the name should convey what the file does without being a long sentence
    </aside>
    
- **Package and Module Names (Python)**
    
    <aside>
    
    - Python modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.
    - Python packages (folder of modules) should also have short, all-lowercase names, although the use of underscores is discouraged by [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names).
    
    ```bash
    my_project/
    │
    ├── datautils/          ← package (folder, no underscores preferred)
    │   ├── __init__.py
    │   ├── clean_data.py   ← module (file, underscores fine)
    │   └── load_data.py    ← module
    ..
    ```
    
    </aside>
    
- **Folders**
    
    <aside>
    
    - Organize files by function, e.g.:
        - `data/`: raw and processed data files
        - `notebooks/`: Jupyter notebooks for exploration and analysis
        - models/: ML models
        - `src/`: reusable Python scripts and modules
        - `outputs/`: charts, tables, and other generated outputs
        - `utils/`: utility package with utility functions
    
    ```bash
    example-data-project/
    ├── **data/**
    │   ├── raw/
    │   └── processed/
    ├── **datautils/**
    │   ├── __init__.py
    │   ├── clean_data.py
    │   └── load_data.py
    ├── **notebooks/**
    │   └── eda.ipynb
    ├── **src/**
    │   ├── main.py
    │   ├── <>.py
    │   └── <>.py
    ├── **models/**
    └── **outputs/**
    ```
    
    </aside>
    
</aside>

<aside>

**Ensuring reproducibility**

- **Generating a `requirements.txt`**
    - A `requirements.txt` file lists all the packages (and optionally their exact versions) that your project depends on.
    - Anyone cloning your repo can use it to recreate the exact same environment by running `pip install -r requirements.txt` in their terminal. This ensures the code runs the same way on their machine as it does on yours.
    - Example `requirements.txt`
        
        ```python
        # Minimally list the packages needed (don't just do this)
        # It refers to the latest available versions
        pandas
        numpy
        matplotlib
        seaborn
        
        # Best to include the specific versions for reproducability
        pandas==2.3.3
        numpy==2.3.4
        matplotlib==3.10.7
        seaborn==0.13.2
        ```
        
        <aside>
        
        `pip install -r requirements.txt` installs every package listed in requirements.txt
        
        - The `-r` flag tells pip to read it for packages instead of trying to install a package called “requirements.txt”
        </aside>
        
    - Automatically generating a `requirements.txt`
        
        <aside>
        
        - **1. Using the `pipreqs` module (available on analytics@gov through ship-nexus pypi proxy, <u>CURRENTLY NOT WORKING</u>)**
            - `pip install pipreqs`
            - `pipreqs .` scans all `.py` files in your current directory and creates a `requirements.txt` that only includes explicitly imported packages.
            - `--savepath <file>` to specify a file path to save to (default requirements.txt)
            - `--clean <file>` on an existing requirements.txt to remove libraries not actually being used by in the current project
            
            ```bash
            # For analytics@gov
            pipreqs . --pypi-server https://ship-nexus.analytics.gov.sg/repository/pypi-proxy/simple/
            ```
            
        - **2. LLM-driven approach**
            - Step 1: **Navigate to your project directory in your terminal** and run the following command to generate a list of all import statements  from all `.py` files
                
                ```bash
                grep -rh "^import\|^from" --include="*.py" . | sort -u
                ```
                
            - Step 2: Copy the above output and paste this prompt into Pair or other LLMs
                
                <aside>
                
                Below is a list of import statements in my python project, use them to generate a list of terminal commands each in the form of `pip index versions <package> --index-url [https://ship-nexus.analytics.gov.sg/repository/pypi-proxy/simple/](https://ship-nexus.analytics.gov.sg/repository/pypi-proxy/simple/)` which I can immediately copy and paste in my terminal to find the specific package versions. Only include the ones for the packages that are not already packaged with Python
                
                **<Replace with output from step 1>**
                
                </aside>
                
            - Step 3: Copy the above output and paste this prompt into Pair or other LLMs
                
                <aside>
                
                Here is the output from the previous step. Use it to generate the content for me to copy and paste into my requirements.txt
                
                **<Replace with output from step 2>**
                
                </aside>
                
            - Step 4: Copy the above output and paste it into your requirements.txt. it should look like below
                
                ```bash
                pandas==2.3.3
                numpy==2.3.4
                matplotlib==3.10.7
                seaborn==0.13.2
                ```
                
        - **3. Using `pip freeze > requirements.txt`**
            - Captures every package and exact version currently installed in your environment, including packages not used by the project.
            - It will also be exceedingly verbose as it includes dependencies, which is unnecessary as pip installing modules automatically installs all its dependencies
        - **4. Manually writing out requirements.txt**
            - If all else fails, I recommend manually writing out `requirements.txt`
            - Remember to list our packages and specific version numbers
        </aside>
        
- **Using a virtual environment**
    - If you don’t use a virtual environment, your computer would have all the python packages you have ever needed all in specific versions, e.g. [analytics.gov](http://analytics.gov) provides `numpy==2.3.4`
    - If you then run a project which is written with packages of a significantly older or newer version, you may run into compatibility issues e.g. the museum forecasting repo uses `numpy==1.26.4` (a major version difference!)
    - e.g. functions and classes may have been added, removed, or changed significantly between versions, which can cause your code to break
    - Instead of having to reinstall specific versions of every package a project needs using the requirements.txt every single time, simply use a virtual environment, which creates an isolated Python environment for each project, with its own set of packages and versions that are independent of everything else on your computer
</aside>

### Virtual Environment Workflow

<aside>

#### **Using `venv` to isolate package versions**

1. **Create the virtual environment**
    
    <aside>
    
    ```bash
    python -m venv .venv
    ```
    
    - The `-m` flag tells Python to run a module as a script. It will look for the module among the list of installed modules, as opposed to you having to run `python` on the exact file path of the module script
    - `venv` refers to the built-in python module for creating virtual environments
    - `.venv` is the name of the folder containing the virtual environment (It is standard convention to use “.venv”)
    - **NOTE**: Each user (repo creator / collaborators) creates their own venv. 
    .`venv/` is typically added to `.gitignore` (it is typically very large and specific to individual machines)
    </aside>
    
2. **Activate the virtual environment**
    
    <aside>
    
    ```bash
    # Mac/Linux (analytics@gov uses Bash terminal with Linux commands)
    source .venv/bin/activate
    
    # Windows (if you use Powershell terminal on your PC, use this)
    .venv\Scripts\activate
    ```
    
    - You know the virtual environment is active if you see `(venv)` in your terminal line.
    - You activate once at the start of each working session and deactivate when you're done
    </aside>
    
3. **Use the virtual environment to run the repo**
    
    <aside>
    
    ```bash
    pip install -r requirements.txt
    ```
    
    - TODO
    </aside>
    
4. **Deactivate the virtual environment when you are done**
    
    ```bash
    deactivate
    ```
    

#### Using `uv` to isolate both python version and package versions

- Use this for cases where a project absolutely requires a specific version of python and you want to skip the hassle of installing and running another version of python

---

1. **Create the virtual environment with a specific python version**
    
    <aside>
    
    ```bash
    uv venv --python 3.11.9 .venv
    ```
    
    - Put the required python version after the `--python` flag
    </aside>
    
2. **Activate the virtual environment**
    
    <aside>
    
    ```bash
    # Mac/Linux (analytics@gov uses Bash terminal with Linux commands)
    source .venv/bin/activate
    
    # Windows (if you use Powershell terminal on your PC, use this)
    .venv\Scripts\activate
    ```
    
    </aside>
    
3. **Use the virtual environment to run the repo**
    
    <aside>
    
    ```bash
    # Install packages
    uv pip install -r requirements.txt
    
    # Check packages installed in virtual environment
    uv pip list
    ```
    
    - Note the use of `uv pip` instead of `pip`, as uv provides its own pip
    - pip list alone will access the normal pip and show th
    </aside>
    
4. **Deactivate the virtual environment when you are done**
    
    <aside>
    
    ```bash
    deactivate
    ```
    
    </aside>
    

---

Similarly, every user separately creates and uses their own virtual environment. Repo authors should gitignore the virtual environment folder (`.venv/`) as it is very large and specific to each user’s machine

</aside>

## 9. Common Scenarios and Troubleshooting

<aside>

**Made a typo in a git commit message or want to rewrite it?**

- If you have <u>**not</u>** pushed it yet: `git commit --amend -m "corrected message"` to edit the **latest** commit message
- If you did, bopes
    1. If it's a minor typo, just leave it as rewriting remote history is dangerous and messy if you are working in a team
    2. If you *really* want to fix it, you can force push an amended commit message, but <u>**only**</u> if you're sure **no one else has pulled the branch**: 
        
        ```bash
        git commit --amend -m "<corrected message>"
        git push --force-with-lease
        ```
        
        - `--amend` only allows you to rewrite the commit message for the last commit
        - `--force-with-lease` will force a push unless someone else has pushed to the branch since you last fetched, protecting you from accidentally overwriting their work.
    3. If others have already pulled the branch, force pushing a rewritten commit history will cause serious problems for them. Their local history will have diverged from the remote, and Git will refuse to let them push normally (a git mess!). They will need to reset or rebase their own local branch to match the rewritten remote, which is really messy.
</aside>

<aside>

**Want to revert a change / commit?**

- See section on [Safe Undo](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?pvs=21) for the various cases
</aside>

<aside>

**Accidentally made changes while on the wrong branch?**

1. If you have <u>**not**</u> staged the changes (with `git add .`), simply `git switch` to the correct branch and continue from there
2. If you have staged the changes but have <u>**not</u>** committed, run these lines:
    
    ```bash
    git restore --staged .                  # unstage everything (note the ".")
    git switch <correct-branch>             # switch branch
    git add .                               # restage on the correct branch
    ```
    
3. If you have already **committed** the changes, run these lines:
    1. If the correct branch <u>**already exists locally**</u>:
        
        ```bash
        git log --oneline            # check commit hashes and note the latest **hash**
        git switch <correct-branch>
        git cherry-pick <hash>       # apply commit to the correct branch FIRST
        git switch <wrong-branch>
        git reset --soft HEAD~1      # undo the commit on the wrong branch (keep changes staged)
        git restore --staged .       # unstage the changes
        git restore .                # discard changes from the working directory
        
        # The last 3 lines are crucial to fully clean up the wrong branch and prevent a git mess
        # This way also erases the wrong commit from local history before it reaches GitLab
        ```
        
    2. If you have <u>**not**</u> created the correct branch locally yet:
        
        ```bash
        git log --oneline              # check commit hashes and note the latest **hash**
        git switch -c <correct-branch> # create **and** switch to new branch
        git cherry-pick <hash>         # apply commit to the correct branch FIRST
        git switch <wrong-branch>      # switch back to wrong branch
        git reset --soft HEAD~1        # undo commit on wrong branch (keep changes staged)
        git restore --staged .         # unstage the changes
        git restore .                  # discard changes from working directory
        ```
        
    - **E.g. Accidentally committing to your local main branch**
        
        <aside>
        
        - Here I committed a change with the message `"feat(user-guide): Initialise user guide"` while on local main instead of a feature branch I had not created yet.
        - Running `git log --oneline`, observe that the commit hash of the wrong commit is `5d1307f` (the topmost one), copy it
        
        ![image.png](image%2011.png)
        
        - Follow the other steps above (in case 3b) to move the commit and clean up the local history (remote history is unaffected as nothing had been pushed yet)
        - Then, push from the correct branch when ready
        </aside>
        
4. If you have already <u>**pushed</u>** the changes from the wrong branch to remote:
    
    ```bash
    git log --oneline              # see recent commits to find the commit hash
    git switch <correct-branch>
    git cherry-pick <hash>         # apply the commit to the correct local branch
    git push                       # push the commit to the correct remote branch
    git switch <wrong-branch>
    git revert <hash>              # undo the commit on the wrong branch
    git push                       # push the revert to GitLab
    ```
    
    - This method uses `git revert` to create a **new commit** that reverses the effect of the wrong commit.
    - The wrong commit will still be forever in the remote history as completely cleaning the remote history is dangerous and messy
</aside>

<aside>

**You're mid-way through changes on a feature branch, then something urgent comes up and you need to switch to another branch to do something else. However, your changes on the current branch aren't ready to be committed yet**

- Use `git stash` to temporarily set aside **uncommitted changes** without committing them.
- See [](https://app.notion.com/p/40c1331f71ad800ebc51ffc726697d0d?pvs=21)
</aside>

<aside>

**Need to add more commits to an MR that's already open?**

- Commit and push to the same branch as usual. GitLab automatically picks up any new commits pushed to the source branch and adds them to the open MR.
</aside>

## 10. Other Gitlab / Github functions

### Forking a repository on Gitlab / Github

<aside>

- Forking is an action you can perform on Gitlab / Github to make a copy of another repository you have read access to. This repo copy is a new repo owned by you.
- From this repo copy, you can work on it as normal e.g. git pull and push to it
- From corresponding remote branches on your repo copy to the original repo, you can create pull requests for the original repo’s owners / developers to accept and pull into the original repo

**Difference between forking and cloning:**

<aside>

**Cloning** a remote repo gives you a **local repo** to work on

**Forking** a remote repo gives you a new **remote repo** under your Gitlab/Github account, which you can then clone to a local repo to work on

</aside>

**Forking Example**

- NUSMods ([website](https://nusmods.com/timetable/sem-1), [github](https://github.com/nusmodifications/nusmods)) is a student-run, open-source project that comprises a timetable builder and knowledge platform, providing students with a better way to plan their school timetable and access useful module-related information.
- Its GitHub repo is run by a core team of student developers who do most of the development. Let’s say you are another student and want to help out, you see their list of pending issues on their GitHub repo and pick out a certain issue to fix: “Bug: course prerequisite tree does not work properly”
- Because you have no write access to the repo, you don't have permission to edit their repo directly. So, you **fork** the repo (available since it is public for anyone to view). This creates your own personal copy of the entire NUSMods repo under your GitHub account, at that point in time, including all the remote branches currently listed.
- You then have to **clone** this forked remote repo, so that you have a local copy to work on in your code editor.
- You make your bug fix in your local forked copy of the repo, then submit a **pull request** to the <u>original NUSMods repo</u>, asking the core team to review and merge the changes from your repo copy into the actual NUSMods repo
- Note: if you try git clone the original NUSMods repo directly, you would not be able to git pull or push from this local copy as you have no write access to the repo.
</aside>

### Transferring a git repo hosted on Github to analytics@gov Gitlab

<aside>

1. `git clone` the repo locally from github on your personal laptop
2. Transfer the folder from your personal laptop to your GSIB/COMET device using secure thumb drive
3. Copy the folder into your analytics@gov
4. Run the following commands
    
    ```bash
    cd /path/to/repo
    git remote remove origin
    git remote add origin https://analytics.<gov-host>/<group>/<repo>.git
    git push -u origin main
    ```
    
</aside>

**Types of conflicts**

![image.png](image%2015.png)