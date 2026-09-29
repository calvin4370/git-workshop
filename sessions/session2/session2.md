# Session 2: Remote Workflows and Conflict Resolution

### Reference Table

<table>
  <colgroup>
    <col style="width: 40%">
    <col style="width: 60%">
  </colgroup>
  <thead>
    <tr>
      <th>Command</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>git clone &lt;HTTPS_address&gt;</code></td>
      <td>Copy a remote repo onto your machine as a new folder</td>
    </tr>
    <tr>
      <td><code>git status</code></td>
      <td>See what has changed, what is staged, and which files have merge conflicts</td>
    </tr>
    <tr>
      <td><code>git add &lt;file&gt;</code><br><code>git add .</code></td>
      <td>Stage a specific file<br>Stage everything in the present working directory</td>
    </tr>
    <tr>
      <td><code>git commit -m "commit message"</code></td>
      <td>Commit staged changes with a single-line message</td>
    </tr>
    <tr>
      <td><code>git commit</code></td>
      <td>Open nano to write a commit message. After resolving a conflict, the merge message is pre-filled</td>
    </tr>
    <tr>
      <td><code>git push</code></td>
      <td>Upload your local commits to the remote branch</td>
    </tr>
    <tr>
      <td><code>git log --oneline</code></td>
      <td>View commit history, one line per commit</td>
    </tr>
    <tr>
      <td><code>git pull</code></td>
      <td>Download remote changes and merge them into your current branch (<code>git fetch</code> + <code>git merge</code>)</td>
    </tr>
    <tr>
      <td><code>git push -u origin &lt;branch&gt;</code></td>
      <td>First push of a new branch. Links it to the remote branch, so later pushes and pulls only need <code>git push</code> / <code>git pull</code></td>
    </tr>
    <tr>
      <td><code>git merge --abort</code></td>
      <td>Cancel a merge in progress and return to how things were before you pulled</td>
    </tr>
    <tr>
      <td><code>git log --oneline --graph</code></td>
      <td>Commit history, with lines showing where work split and merged</td>
    </tr>
    <tr>
      <td><code>git fetch</code></td>
      <td>Download remote branches and commits <strong>without</strong> merging them or touching your working directory</td>
    </tr>
    <tr>
      <td><code>git branch</code><br><code>git branch -a</code></td>
      <td>List local branches (current branch highlighted)<br>List all branches, including remote ones</td>
    </tr>
    <tr>
      <td><code>git switch &lt;branch&gt;</code></td>
      <td>Switch to another branch (covered in Session 3)</td>
    </tr>
    <tr>
      <td><code>git restore &lt;file&gt;</code></td>
      <td>Discard uncommitted changes to a file. <strong>These changes cannot be recovered</strong> (covered in Session 4)</td>
    </tr>
  </tbody>
</table>

<br>

## Overview

> In Session 1, you cloned a brand new, empty repo you created yourself on GitLab
>
> This time, we will clone a repo that already has files and a commit history, just like joining an ongoing project.

<br>

## Setup

> `Minions Visitorship` is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.

#### a. Clone the `Minions Visitorship` repo

- Navigate to your home directory using `cd ~`
- Run `git clone https://gitlab.analytics.gov.sg/gcc_jun_jie_chan_from.tp/minions-visitorship.git`
- Navigate into the project folder using `cd minions-visitorship`

#### b. Switch to a different branch (`minions-visitorship` repo)

> Branching lets you create a separate line of work that diverges from `main` without affecting it. This allows you to work on something unfinished without breaking what already works, and lets many people work in parallel without getting in one another's ways.
>
> `main` should always be in a working state (production). Branches are for work-in-progress changes.
>
> We will go through branching in detail in Session 3 Branching.

- Run `git switch s2` to switch to the `s2` branch of the repo
- This is to prevent you from pushing changes to modify my clean `main` branch (I have also configured the GitLab repo to not accept direct pushes to main).

#### c. Install the workshop dependencies

- From the root of the `minions-visitorship` repo, run:

    ```bash
    pip install -r requirements.txt
    ```

<br>

## Activity 1: Pushing and Pulling Changes

> Repo: `minions-visitorship`
> Branch: `s2`

> We will demonstrate pushing and pulling with 4 participants. Each person will push changes to the repo, and pull the updated state of the repo

- Open the Jupyter notebook at `minions-visitorship/session2_lab/analysis.ipynb`
- Only the participant whose turn it is should edit or run the notebook. If anyone else runs it, their next `git pull` will fail (see Activity 6, Situation B)

<br>

#### a. Participant 1 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- You should see:
  ![Output of git pull](../../assets/already.png)
- Find the cell under **Config** with the code `YEAR = 2024`
    - Edit the code into `YEAR = 2025`
    - Rerun the notebook to regenerate the plot outputs for 2025
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: rerun notebooks for 2025 data"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase

#### b. Participant 2 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- You should see:
  ![Output of git pull](../../assets/pull-part2.png)
    - This time, `git pull` lists the files that changed, as it is pulling in Participant 1's commit
- Find the first plot, **Top 10 minions by visits**, and look at the code cell under it: `plot_top_minions(visits, MINION_YELLOW, YEAR)`
    - The 2nd argument is the colour of the bars
    - Replace `MINION_YELLOW` with any other colour from the minion colour scheme, e.g. `EVIL_PURPLE`
    - The full list of colours is at the top of `src/minions.py`
    - Rerun the notebook
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: change colour of top minions plot"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase

#### c. Participant 3 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- Find the cell under **Config** with the code `YEAR = 2025`
    - Edit the code back into `YEAR = 2024`
    - Rerun the notebook to regenerate the plot outputs for 2024
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: rerun notebooks for 2024 data"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase

#### d. Participant 4 pushes their changes

- Run `git pull` to update your working directory to the latest state of the remote repo's `s2` branch
- Pick any plot(s) in the notebook
    - e.g. **Visits by museum** has the code cell `plot_visits_by_museum(visits, GOGGLE_GREY, YEAR)`
    - Replace the colour argument with any other colour from the minion colour scheme, e.g. `MARGO_GREEN`
    - Rerun the notebook
- Stage, commit and push your changes to remote
    - `git add session2_lab/analysis.ipynb`
    - `git commit -m "analysis: change colour of plots"`
    - `git push`

> Everyone should now run `git pull` to pull the changes.
>
> Your working directories should now all reflect the updated codebase
>
> Run `git log --oneline` to see all 4 commits in the history. Everyone's local repo now has the same commits, in the same order, as the remote `s2` branch on GitLab.

<br>

## Activity 2: Merge Conflicts

> Repo: `minions-visitorship`
> Branch: `s2`
>
> File: `minions-visitorship/session2_lab/activity2.py`

> `git pull` is `git fetch` then `git merge`. Most of the time, Git merges changes automatically, as long as you and your teammates changed **different parts** of the code.
>
> A **merge conflict** happens when two commits change the **same lines of the same file**. Git will not guess which version to keep. It stops the merge, marks the conflicting lines, and leaves you to decide (conflict resolution).

#### a. Everyone edits the same lines

- Run `git pull`, so everyone starts from the same commit
- Open `session2_lab/activity2.py`, and replace `return` in `function1()` with a line of your own, e.g. `print("<your name> was here")`
- Stage and commit, but do **not** push yet
    - `git add session2_lab/activity2.py`
    - `git commit -m "activity2: update function1"`

#### b. Participant 1 pushes

- **Participant 1:** run `git push`. This works as usual

#### c. Everyone else pulls and resolves the conflict

Go **one at a time**, in order (Participant 2, then 3, then 4). Wait for the previous participant to push before you start.

- Run `git pull --no-rebase`
    - Git stops with `CONFLICT (content): Merge conflict in session2_lab/activity2.py`

    > **Why `--no-rebase`?** You and the remote both have new commits that the other does not have (your branches have _diverged_). Git needs you to choose how to combine them, so a plain `git pull` stops with `fatal: Need to specify how to reconcile divergent branches`.
    >
    > - `--no-rebase` (merge): combines your commit and the remote's with a new **merge commit**. The history shows where the work split and joined back together
    > - `--rebase`: sets your commit aside, applies the remote's commits, then replays your commit on top. The history stays a straight line, with no merge commit
    >
    > We will go through this choice in Activity 6, Situation A.

- Run `git status`. It says `You have unmerged paths`, and lists `activity2.py` as `both modified`
- Open `activity2.py`. Git has marked the conflicting lines:

    ```python
    def function1():
    <<<<<<< HEAD
        print("Participant 2 was here")
    =======
        print("Participant 1 was here")
    >>>>>>> 3f9c2e1a...
    ```

    - Between `<<<<<<< HEAD` and `=======` is **your** version
    - Between `=======` and `>>>>>>>` is the **incoming** version from the remote (followed by its commit ID)

- Edit the file into the final version you want, and delete **all** the markers (`<<<<<<<`, `=======`, `>>>>>>>`)
    - In VSCode, you can instead click `Accept Current Change`, `Accept Incoming Change` or `Accept Both Changes` above the conflict
- Save the file, then complete the merge:
    - `git add session2_lab/activity2.py`
    - `git commit`. nano opens with a pre-filled message, `Merge branch 's2' of ...`. Save and exit to accept it
- Run `git push`

> **Tip:** If you get lost in the middle of a merge, run `git merge --abort`. This puts your repo back exactly as it was before you pulled, so you can try again.

#### d. See the result

- **Everyone:** run `git pull`, then `git log --oneline --graph`
    - The lines show where work split and was joined back together at each merge commit

<hr>

<span style="color:salmon">A merge conflict is not an error, and it is not dangerous. Git is simply asking you to decide which version to keep. The merge is only complete once you remove the conflict markers, `git add` the file and commit.</span>

- Conflicts are easier to avoid than to resolve. `git pull` often, especially before starting any chunk of work
- Conflicts in Jupyter notebooks are far worse, as the markers land in the middle of the JSON, and the notebook will not open until you remove them. This is another reason to keep reusable logic in `.py` files

<br>

## Activity 3: Working with API keys

> Other than rebuildable outputs, large binaries, and clutter which should not be committed for various reasons, there are some environmental variables / files required by your code but still should never be committed to Git.
>
> What to NEVER commit to your Git repositories:
>
> - API keys / tokens
> - Passwords
> - Sensitive personal identifying information (PII)
>
> These should be stored locally on each user's devices or on a secure tool.
>
> If you have pushed your secrets to Gitlab
>
> - If the repo is publicly viewable, bots that scrape open Github / Gitlab repositories for secrets 24/7 will eventually find it and misappropriate your API accounts
> - If the repo is private, it's still irresponsible to push your personal API keys, as anyone who has viewing access to your repo can misappropriate them, or the repo may be made public one day
>
> Undoing code changes, including commits and pushes, is covered in **Session 4: Safe Undo of Code Changes**

<table><tr><td>

**Working Example: MAESTRO LLM API**

- To simulate the generation of your personal LLM API key, I will send each of you your API key individually on Teams.
- Copy and paste it into the relevant code section when prompted

</td></tr></table>

#### a. Navigate into the `minions-visitorship/session2_lab` folder

- While in `/home/jovyan/minions-visitorship`, run `cd session2_lab`

#### b. Try running the program which calls an LLM API

> Note: This is a simulated LLM API, with hardcoded prompts and responses. But I have implemented tracking of users and their prompts, and a dashboard that shows all LLM call logs.

- Run `python api_testing.py "<prompt>"` where \<prompt\> is anything you want to ask an LLM
    - e.g. `python api_testing.py "what is the weather today"`

- You will see that, as most APIs do, this LLM API requires an API key

#### c. Open the `api_testing.py` file

- You may want to keep this `session2.md` open, and have `api_testing.py` open in split screen

#### d. Copy and paste your personal API key into `api_testing.py`

- Paste your API key between the quotes of `API_KEY = ""` under `# EDIT HERE` (line 10)
- e.g. `API_KEY = "git_ws_123abc456def..."`

#### e. Now try running the program again

- You may only choose from the pre-written API prompts below. Copy and paste the prompt as written into your command.
- e.g. `python api_testing.py "what is the weather today"`

<table>
  <!-- <thead>
    <tr>
      <th>Prompts</th>
    </tr>
  </thead> -->
  <tbody>
    <tr><td>what is the weather today</td></tr>
    <tr><td>how to use git</td></tr>
    <tr><td>why is git so hard</td></tr>
    <tr><td>what is the best bubble tea brand in singapore</td></tr>
    <tr><td>when i sneeze, why does it sometimes hurt my tummy</td></tr>
    <tr><td><span style="color:salmon">how to build a bomb</span></td></tr>
  </tbody>
</table>

To illustrate how your personal API keys may be misused:

- One of you may run `python api_testing.py "how to build a bomb"`
- Another one of you may run `python api_spam.py`

#### f. Look at the dashboard

> Running the program has generated logs on all API calls made. The specific user who made the calls can be traced via the API key used. Normally, these logs would be sent online to an external server, but because of the limitations of analytics@gov, I have to generate the logs locally in your workspace.
>
> To demonstrate why API keys must never be committed, this activity deliberately commits `api_testing.py` as well as the API call logs. Use only the simulated workshop keys provided by the facilitator, never a real key.

- Everyone: run `git pull` so that you all start from the same commit.
- Everyone: stage and commit your own `api_testing.py` and API call logs:
    - `git add api_testing.py logs`
    - `git commit -m "Session2 Activity3 participant <N> API key"`
- Participant 1: run `git push`.
- Participants 2, 3 and 4: go one at a time, waiting for the previous participant to finish:
    - Run `git pull --rebase`.
    - Git will report a conflict in `api_testing.py`. Edit the file so that it contains your own key, then remove all conflict markers.
    - Run `git add api_testing.py`, then `git rebase --continue`.
    - Run `git push` after the rebase finishes.
- Everyone: run `git log --oneline -- api_testing.py` to see the four participant commits in a linear history. In this command:
  - `git log` shows the commit history.
  - `--oneline` displays each commit on one compact line.
  - `--` marks the end of Git options. Everything after it is treated as a file or folder path, not as another option or commit name.
  - `api_testing.py` limits the history to commits that changed this file.
- Run `git log -p -- api_testing.py` to see that the keys remain in earlier commits even after the latest file is cleaned up. Here, `-p` shows the line-by-line changes introduced by each commit:

  ```text
  git log    -p    --    api_testing.py
  command  option  separator  file path
             `--` separates options from the file path
  ```

  The `--` is important because it tells Git clearly that `api_testing.py` is a path. Without it, Git may try to interpret a name as a commit, branch, or other revision before treating it as a file.
- In the left pane, right-click `session2_lab/api_dashboard.html` and click `Show Preview`

> ### Learning Points: Why API Keys Must Be Secured
>
> - As you can see, it is easy for administrators to see
>     - which API key made each request,
>     - which participant that key belongs to,
>     - what prompts were submitted, and
>     - how many calls each participant made, including malicious calls.
> - A leaked key can allow someone else to use your API quota, incur costs, access protected services, or create activity that is attributed to you.
> - API keys must never be committed to a Git repository. Removing a key from the latest version does not remove it from the repository's commit history.
> - If a key is exposed, revoke or rotate it immediately and issue a replacement.
> - Store secrets outside source code, such as in environment variables or a secrets manager. We will practise using a `.env` file in the next activity.

<br>

## Activity 4: Using `.env` files

> **Facilitator: Reset the API demonstration**
>
> - From the root of the `minions-visitorship` repo, run:
>
>     ```bash
>     git pull
>     ```
>
> - Open `session2_lab/api_testing.py` and replace the committed simulated key with `API_KEY = ""`. This removes the key from the latest version, but not from the earlier commits where participants committed it.
> - Commit and push this cleanup:
>
>     ```bash
>     git add session2_lab/api_testing.py
>     git commit -m "chore: remove API key from latest source"
>     git push
>     ```
>
> - Then remove the generated logs:
>
>     ```bash
>     git rm -r session2_lab/logs
>     git commit -m "chore: reset API call logs"
>     ```
>
> - Add the following line to `.gitignore` at the root of the repo, so that nobody can accidentally commit their `.env` file:
>
>     ```text
>     .env
>     ```
>
> - Commit and push the change:
>
>     ```bash
>     git add .gitignore
>     git commit -m "chore: ignore .env files"
>     git push
>     ```
>
> - Have everyone run `git pull`, and check that `.env` now appears in their `.gitignore`.

#### a. Create an `.env` file to store your API key

- At the root of the `minions-visitorship` repo, create an `.env` file

- Add your personal key:

    ```python
    API_KEY="your_personal_api_key"
    ```

#### b. Check that `.env` is ignored

- Open `.gitignore` at the root of the repo. The facilitator has already added this line and pushed it, which you pulled:

    ```text
    .env
    ```

- Run `git status` and confirm that `.env` does not appear.

#### c. Update `api_testing.py`

- Replace the `# EDIT HERE` block (`API_KEY = ""`) with:

    ```python
    # EDIT HERE ===================================================
    import os
    from dotenv import load_dotenv

    load_dotenv()
    API_KEY = os.environ["API_KEY"]
    # =============================================================
    ```

- Run the program again with any of the permitted prompts.
- Run `git restore api_testing.py`.
- Run `git status`, and confirm that only your logs in `session2_lab/logs` are listed, and `.env` is not
- Stage, commit and push
    - `git add .`
    - `git commit -m "Session2 Activity4 API call logs"`
    - `git push` (if rejected, run `git pull --no-rebase`, then `git push` again)
- Run `cd ..` to return to the root of the `minions-visitorship` repo. All commands from here on are run from the root

<br>

## Activity 5: Fixing Problems Preventing Pushing

### Situation A: The remote branch is ahead of your local branch

```
 ! [rejected]        s2 -> s2 (fetch first)
error: failed to push some refs to '<remote_url>'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
```

> While `git merge`, `git pull`, and Pull Requests (GitHub) / Merge Requests (GitLab) can cause merge conflicts, `git push` can never cause a merge conflict.
>
> Git will simply not allow you to push if the remote branch is ahead of your local branch (you will have to pull first). Otherwise, your push would overwrite your teammates' commits that you do not have.

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Everyone:** create a new file `session2_lab/push_p<N>.txt`, where `<N>` is your participant number, and type anything in it
- **Everyone:** stage and commit it
    - `git add session2_lab/push_p<N>.txt`
    - `git commit -m "chore: add push_p<N>.txt"`
- **Participant 1:** run `git push`. This works as usual
- **Participants 2, 3 and 4:** run `git push`. Git rejects it with the error above

**Fix: pull first, then push**

Go one at a time, in order (Participant 2, then 3, then 4):

- `git pull --no-rebase`
    - nano opens with a pre-filled merge message. Save and exit to accept it
    - You and the remote both have new commits, so Git needs to know how to combine them. `--no-rebase` means merge. We will go through this choice in Activity 6, Situation A
- `git push`
    - If it is rejected again, someone pushed in between. Just pull and push again

<hr>

### Situation B: No upstream branch set

```
fatal: The current branch s2-p1 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin s2-p1
```

> Your local branch is not linked to any branch on the remote yet, so a plain `git push` does not know where to push to.
>
> ```
>  Local repo                        Remote repo (GitLab)
>  ──────────                        ────────────────────
>  s2        ◄──── upstream ────►    origin/s2
>  s2-p1     ◄──── (none) ─────      (does not exist yet)
> ```
>
> - This happens on the **first** push of a branch you created locally (Session 3), or of a brand new local repo you linked with `git remote add` (Session 0)
> - Branches you get from the remote, like `s2` via `git switch s2`, are already linked. This is why a plain `git push` has worked on `s2` all session

**Fix: push once with `-u`**

```
git push -u origin <branch>
```

- `-u` (short for `--set-upstream`) links your local branch to the remote branch, creating it on the remote if it does not exist yet
- You only need to do this once per branch. After that, a plain `git push` / `git pull` works

<hr>

### Situation C: The branch is protected on GitHub / GitLab

GitLab rejects the push with an error similar to:

```
remote: GitLab: You are not allowed to push code to protected branches on this project.
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to '<remote_url>'
```

> A **protected branch** only accepts changes in approved ways, usually through a merge request. Repo owners protect `main` so that nobody can push unreviewed changes straight into production.
>
> - The `main` branch of `minions-visitorship` is protected, which is why we work on `s2` in this session

**Fix: do not push to the protected branch**

- Push your commits to a separate branch instead, then open a merge request to merge it into `main` (Session 5)
- If you already committed on local `main` by mistake, move those commits to the correct branch first (Session 4)

<hr>

### Situation D: Unrelated histories

```
fatal: refusing to merge unrelated histories
```

> Occurs when Git is asked to combine two branches / repositories that **do not share a common ancestor commit**. Git will not allow this, as it cannot treat one commit history as a continuation of the other.
>
> **Example**
>
> - You have a project folder which you just initialised as a git repo with `git init`, and committed your files
> - You then create a new GitLab repo, but mistakenly tick `Add README`. This creates a separate first commit on GitLab
> - You link the two with `git remote add origin <HTTPS_address>`
> - When you try to push, Git rejects it with the same error as Situation A, because of the README commit on GitLab
> - When you try to pull the README, Git refuses with `fatal: refusing to merge unrelated histories`

**Fix: allow the unrelated histories to be merged, then push**

```
git pull origin main --no-rebase --allow-unrelated-histories
git push -u origin main
```

- `origin main`: your new local branch has no upstream yet (Situation B), so you need to say which remote branch to pull from
- `--no-rebase`: combine them with a merge (Activity 6, Situation A)
- `--allow-unrelated-histories`: tells Git to merge even though the two histories share no common commit

To avoid this entirely, **untick `Add README`** when creating a GitLab repo for an existing local project, as we did in Session 0.

<br>

## Activity 6: Fixing Problems Preventing Pulling

### Situation A: Your local and remote branches have diverged

```
fatal: Need to specify how to reconcile divergent branches.
```

> Your local branch has commits the remote does not have, **and** the remote has commits you do not have. Both branches have moved on from the same commit in different directions, so Git needs you to choose how to combine them.
>
> - This typically happens when you and a teammate work on the same branch at the same time
> - It can also happen if you push from one computer, then continue working on another computer without pulling first
> - This is why you should run `git pull` before starting work on a branch
>
> This is a similar situation to **Activity 5, Situation A**. In both, your branch and the remote branch have each gained commits the other does not have. There, `git push` was rejected because it would overwrite the remote's commits. Here, `git pull` stops because Git needs you to choose how to combine the two.

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Everyone:** create a new file `session2_lab/diverge_p<N>.txt`, where `<N>` is your participant number, and type anything in it
- **Everyone:** stage and commit it, but do **not** push
    - `git add session2_lab/diverge_p<N>.txt`
    - `git commit -m "chore: add diverge_p<N>.txt"`
- **Participant 1:** run `git push`. This works as usual
- **Participants 2, 3 and 4:** run `git pull`. Git stops with:

![Error when running git pull](../../assets/git-pull-error.png)

**Fix: choose how to combine the branches**

> The two options below apply to this one pull only:
>
> - `git pull --no-rebase` (**merge**): combines both branches with a new **merge commit**. The history shows where the work split and joined back together
> - `git pull --rebase` (**rebase**): sets your local commits aside, applies the remote's commits, then replays your commits on top. The history stays a **straight line**, with no merge commit
>
> Only rebase commits you have **not** pushed yet, as rebasing rewrites them.

Go one at a time, in order:

- **Participant 2 (merge):**
    - `git pull --no-rebase`
    - nano opens with a pre-filled merge message. Save and exit to accept it
    - `git push`
- **Participant 3 (rebase):**
    - `git pull --rebase`
    - You should see `Successfully rebased and updated refs/heads/s2.`
    - `git push`
- **Participant 4:** pick either option, then `git push`
- **Everyone:** run `git pull`, then `git log --oneline --graph`
    - Participant 2's merge shows as lines splitting and joining back at a merge commit
    - Participant 3's rebased commit comes directly after the commit before it, with no merge commit of its own

<hr>

### Situation B: Local uncommitted changes would be overwritten

```
error: Your local changes to the following files would be overwritten by merge:
        session2_lab/analysis.ipynb
Please commit your changes or stash them before you merge.
Aborting
```

> You ran `git pull` while you had **uncommitted** changes to a file that the incoming commits also change. <span style="color:salmon">Note this applies by files and not lines! So even when the edits are on different lines, Git will not overwrite your uncommitted changed file, so it stops the pull.</span>
>
> - A common cause is simply running a Jupyter notebook, which changes its outputs and metadata even if you did not edit any code
> - If your uncommitted changes are only in **other** files, the pull works as normal and keeps your changes

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Participant 1:** edit `function1()` in `session2_lab/activity2.py`, then stage, commit and push
    - `git add session2_lab/activity2.py`
    - `git commit -m "feat(activity2): update function1"`
    - `git push`
- **Participants 2, 3 and 4:** edit a **different** function in `session2_lab/activity2.py` and save. Do **not** stage or commit
    - Participant 2 → `function2()`
    - Participant 3 → `function3()`
    - Participant 4 → `function4()`
- **Participants 2, 3 and 4:** run `git pull`. Git stops with the error above, listing `session2_lab/activity2.py`

**Fix: 3 ways**

Each participant tries a different fix. Go one at a time, in order:

- **Participant 2: Commit your local changes**
    - `git add session2_lab/activity2.py`
    - `git commit -m "feat(activity2): update function2"`
    - `git pull --no-rebase` (or `--rebase`). Your branches have now diverged, as in Situation A
        - If you and a teammate changed the same lines, resolve the merge conflict as in Activity 2
    - `git push`
- **Participant 3: Discard your local uncommitted changes**
    - `git restore session2_lab/activity2.py` (or `git restore .` to discard changes in all files)
        - ⚠️ Your edit to `function3()` is gone for good. It cannot be recovered
    - `git pull`
- **Participant 4: Stash your local uncommitted changes**
    - `git stash` sets your uncommitted changes aside, so your files match your last commit
    - `git pull`
    - `git stash pop` puts your changes back, on top of the latest code
    - Your edit to `function4()` is back, still uncommitted. We will cover stashing in more detail in Session 4

<hr>

### Situation C: An untracked local file would be overwritten

```
error: The following untracked working tree files would be overwritten by merge:
        .gitignore
Please move or remove them before you merge.
```

> A teammate pushed a **new** file, and you have an **untracked** file with the same name in the same folder. Git will not overwrite a file it is not tracking, even if both files have identical contents.
>
> - e.g. You and a teammate each create a `.gitignore`, and they push theirs first

**Reproduce the error**

- **Everyone:** run `git pull`, so everyone starts from the same commit
- **Participant 1:** create `session2_lab/meeting_notes.md`, type anything in it, then stage, commit and push
    - `git add session2_lab/meeting_notes.md`
    - `git commit -m "docs: add meeting notes"`
    - `git push`
- **Participants 2, 3 and 4:** create a file with the **exact same name**, `session2_lab/meeting_notes.md`, type anything in it and save. Do **not** stage or commit
- **Participants 2, 3 and 4:** run `git pull`. Git stops with the error above, listing `session2_lab/meeting_notes.md`

**Fix: move or remove your file, as the error suggests**

- **Participants 2 and 3: Rename your file** if you want to keep it
    - In the left pane, right-click your `meeting_notes.md` → Rename, e.g. to `meeting_notes_p2.md`
    - `git pull`. Participant 1's `meeting_notes.md` now appears next to your renamed file
- **Participant 4: Delete your file** if you do not need it
    - In the left pane, right-click your `meeting_notes.md` → Delete
        - ⚠️ Untracked files are not saved in Git, so deleting one is permanent
    - `git pull`

<br>

## Activity 7: Fetch vs Pull

> ```bash
> git fetch
> ```
>
> - Updates your local knowledge of what remote branches are on GitLab
> - Essentially it only downloads remote changes, but unlike `git pull`, it does not merge the changes, so it does not touch your working directory

#### a. Accessing remote branches with fetch

> If you currently do not have a copy of a remote branch locally, running `git switch` to access it will not work, as your local repo has no knowledge of that remote branch.
>
> **Example:**
>
> - Your teammate pushed a feature branch `hyperparameter-tuning` to remote
> - They told you they did that, and you are to continue working on their branch
> - If you simply run `git switch hyperparameter-tuning`, it will not work as your local repo has no knowledge of that remote branch. Running `git branch -a` will also not show that branch
> - After running `git fetch`, your local repo knows about the new remote branch, `origin/hyperparameter-tuning`
> - You can now `git switch hyperparameter-tuning` to get a local copy of it

> **Facilitator:** once everyone has finished Activity 6, push a new branch from the root of the repo:
>
> ```bash
> git switch -c hyperparameter-tuning
> git push -u origin hyperparameter-tuning
> git switch s2
> ```

#### Everyone:

- Run `git branch -a` to list all branches your local repo knows about, including remote ones. `hyperparameter-tuning` is not listed
- Run `git switch hyperparameter-tuning`. It fails with `fatal: invalid reference: hyperparameter-tuning`
- Run `git fetch`. The output lists what is new on the remote since you last fetched or pulled, including `* [new branch]      hyperparameter-tuning -> origin/hyperparameter-tuning`
    - If nothing is new on the remote, `git fetch` prints nothing
- Run `git branch -a` again. `remotes/origin/hyperparameter-tuning` is now listed
- Run `git switch hyperparameter-tuning`. This now works, and creates a local copy of the branch
- Run `git switch s2` to go back

<hr>

**Why not just run `git pull`?**

- `git pull` fetches all remote changes **and merges remote changes for your current branch**, which may be an extra step you don't want to do yet
- `git fetch` only downloads everything from the remote for all new branches and commits, giving your local repo full knowledge of what exists on GitLab, so that you can access a local copy of the new remote branch without affecting the local branch you were previously working on

<br>

## Activity 8: Forking a Repo

> - Forking is an action you can perform on Gitlab / Github to make a copy of another repository you have read access to. This repo copy is a new repo owned by you.
> - From this repo copy, you can work on it as normal e.g. git pull and push to it
> - From corresponding remote branches on your repo copy to the original repo, you can create pull requests for the original repo’s owners / developers to accept and pull into the original repo

<table><tr><td>

**Difference between forking and cloning:**

- **Cloning** a remote repo gives you a **local repo** to work on

- **Forking** a remote repo gives you a new **remote repo** under your GitLab/GitHub account, which you can then clone to a local repo to work on

</td></tr></table>

<hr>

> **Forking Example**
>
> - NUSMods (website, github) is a student-run, open-source project that comprises a timetable builder and knowledge platform, providing students with a better way to plan their school timetable and access useful module-related information.
> - Its GitHub repo is run by a core team of student developers who do most of the development. Let’s say you are another student and want to help out, you see their list of pending issues on their GitHub repo and pick out a certain issue to fix: “Bug: course prerequisite tree does not work properly”
> - Because you have no write access to the repo, you don't have permission to edit their repo directly. So, you **fork** the repo (available since it is public for anyone to view). This creates your own personal copy of the entire NUSMods repo under your GitHub account, at that point in time, including all the remote branches currently listed.
> - You then have to **clone** this forked remote repo, so that you have a local copy to work on in your code editor.
> - You make your bug fix in your local forked copy of the repo, then submit a **pull request** to the original NUSMods repo, asking the core team to review and merge the changes from your repo copy into the actual NUSMods repo
> - Note: if you try git clone the original NUSMods repo directly, you would not be able to git pull or push from this local copy as you have no write access to the repo.

<hr>

#### a. Try forking the Minions Visitorship repo
