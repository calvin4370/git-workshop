# Session 3: Branching

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
      <td><code>git status</code></td>
      <td>See what has changed, and which branch you are on</td>
    </tr>
    <tr>
      <td><code>git add &lt;file&gt;</code><br><code>git commit -m "commit message"</code></td>
      <td>Stage a file<br>Commit staged changes</td>
    </tr>
    <tr>
      <td><code>git push</code><br><code>git push -u origin &lt;branch&gt;</code></td>
      <td>Upload your commits to the remote branch<br>First push of a new branch, linking it to the remote branch</td>
    </tr>
    <tr>
      <td><code>git pull</code></td>
      <td>Download and merge changes from your branch's remote branch</td>
    </tr>
    <tr>
      <td><code>git fetch</code></td>
      <td>Download remote branches and commits <strong>without</strong> merging them</td>
    </tr>
    <tr>
      <td><code>git log --oneline --graph</code></td>
      <td>Commit history, with lines showing where work split and merged</td>
    </tr>
    <tr>
      <td><code>git branch</code><br><code>git branch -r</code><br><code>git branch -a</code></td>
      <td>List local branches (current branch marked with <code>*</code>)<br>List remote branches<br>List all branches, local and remote</td>
    </tr>
    <tr>
      <td><code>git branch &lt;branch&gt;</code></td>
      <td>Create a new branch from your current branch, <strong>without</strong> switching to it</td>
    </tr>
    <tr>
      <td><code>git switch &lt;branch&gt;</code></td>
      <td>Switch to an existing branch</td>
    </tr>
    <tr>
      <td><code>git switch -c &lt;branch&gt;</code><br><code>git switch -c &lt;branch&gt; main</code></td>
      <td>Create and switch to a new branch, from your <strong>current</strong> branch<br>Create and switch to a new branch, from <code>main</code></td>
    </tr>
    <tr>
      <td><code>git log --oneline --graph --all</code></td>
      <td>Commit history of <strong>all</strong> branches, not just the current one</td>
    </tr>
    <tr>
      <td><code>git pull origin main</code></td>
      <td>Merge the latest remote <code>main</code> into your current branch</td>
    </tr>
    <tr>
      <td><code>git stash</code><br><code>git stash -u</code></td>
      <td>Set aside your uncommitted changes to tracked files<br>Same, but also include untracked files</td>
    </tr>
    <tr>
      <td><code>git stash list</code></td>
      <td>List your stashes</td>
    </tr>
    <tr>
      <td><code>git stash pop</code><br><code>git stash apply</code></td>
      <td>Restore the most recent stash and <strong>remove</strong> it from the list<br>Restore the most recent stash and <strong>keep</strong> it in the list</td>
    </tr>
    <tr>
      <td><code>git stash drop</code><br><code>git stash clear</code></td>
      <td>Delete the most recent stash<br>Delete <strong>all</strong> stashes</td>
    </tr>
    <tr>
      <td><code>git branch -d &lt;branch&gt;</code><br><code>git branch -D &lt;branch&gt;</code></td>
      <td>Delete a local branch (only if merged)<br><strong>Force</strong> delete a local branch, even if not merged</td>
    </tr>
    <tr>
      <td><code>git push origin -d &lt;branch&gt;</code></td>
      <td>Delete a branch on the remote, <strong>for everyone</strong></td>
    </tr>
  </tbody>
</table>

> **Tip:** `git log` opens its output in a scrollable viewer when it does not fit on your screen. Press **`q`** to quit.

<br>

## Overview

> In Session 2, you worked on the `s2` branch without creating it yourself. In this session, you will learn what a branch actually is, create your own, and use branches the way a team does day to day.

<br>

## Setup

- Navigate into the `minions-visitorship` repo you cloned in Session 2: `cd ~/minions-visitorship`
- Run `git switch main` to switch to the `main` branch
- Run `git pull` to get the latest version of `main`
- Run `ls session3_lab` to check that the session 3 files are there. You should see `features.py` and `scratch.md`

<br>

## Activity 1: Prerequisites Recap

> Repo: `minions-visitorship`
> Branch: `main`

#### a. Check which branch you are on
- Run `git status`
  - You should see:
    ```
    On branch main
    Your branch is up to date with 'origin/main'.
    ```
- Run `git branch`
  - `main` is marked with `*`, as it is your current branch
  - `s2` is also listed, as you switched to it in Session 2

#### b. Local vs remote branches
- Run `git branch -r`
  - You should see:
    ```
      origin/HEAD -> origin/main
      origin/main
      origin/s2
    ```
  - Branches starting with `origin/` refer to the remote versions of the branches on GitLab (`origin`)
- Run `git branch -a`
  - Lists both. Remote branches are shown as `remotes/origin/...`

<hr>

> 
> - A **local branch** (e.g. `main`) is the branch you work on locally, on your machine
> - A **remote branch** (e.g. `origin/main`) is Git's record of the state of that branch was on GitLab, the last time you ran `git fetch` or `git pull`
> - You never work on remote branches directly. You `git pull` to bring their changes into your local branch, and `git push` to send yours to them

<br>

## Activity 2: What is a Branch?

> Repo: `minions-visitorship`
> Branch: `main`

> - Branching lets you create a separate line of work that diverges from `main` without affecting it.
> - This allows you to:
>     - work on something unfinished without breaking what already works
>     - if something goes wrong, you can simply delete the branch instead of having to manually find and revert bad changes
>     - many people can work in parallel without getting in one another's ways
> - `main` should always be in a working state (production). Branches are for development of messy or work in progress

#### a. A branch is just a label pointing at a commit

- Every commit points back to the commit before it, forming a chain of history
- A **branch** is simply a movable label that points at one commit, the latest commit on that branch. Each time you commit on a branch, its label moves forward to the new commit
- **`HEAD`** marks where **you** are: the branch you are currently on

```
                      HEAD
                       ↓
                      main
                       ↓
  A  ←  B  ←  C  ←  D
                ↖
                  E
                  ↑
          feature/new-plot
```

- Here, `main` points at commit `D`, and `HEAD -> main` means you are on `main`
- `feature/new-plot` was created at commit `C`, and has 1 commit of its own, `E`. That commit is not on `main`
- Creating a branch does not copy any files. Git just adds a new label, so branches are cheap and fast to create

#### b. See it in your repo
- Run `git log --oneline --graph --all`
  - `--all` shows the commits of **all** branches, not just your current one
  - Look at the labels in brackets beside the commits, e.g. `(HEAD -> main, origin/main, origin/HEAD)` and `(origin/s2, s2)`
  - Each label is a branch pointing at that commit. As in Session 1, `HEAD -> main` marks where you are
  - Press `q` to exit if the output fills your screen

<br>

## Activity 3: Creating and Switching Branches

> Repo: `minions-visitorship`
> Branch: `main`
>
> In this activity, `<N>` is your participant number, e.g. `practice-p1` for Participant 1. These branches stay on your machine only. We will not push them for this activity.

#### a. Create a branch
- Make sure you are on `main`, then run:
    ```
    git branch practice-p<N>
    ```
- Run `git branch`
  - You should see, for example:
    ```python
    # For the rest of this activity, I will use p1 as an example
    * main
      practice-p1
      s2
    ```
  - The branch has been created, but you are still on `main` (`*`). `git branch <branch>` only creates the branch, it does not switch to it
- Note that everyone only sees their locally created branch, and not anyone else's
- Run `git branch -r` to view remote branches. Note that even on the remote, you dont see anyone else's in-progress branches. This is because nobody has pushed their branches to remote yet.

#### b. Switch to your local branch
- Run `git switch practice-p<N>` 
  - You should see `Switched to branch 'practice-p1'`
- Run `git status` and `git branch` to confirm you are now on `practice-p<N>`

#### c. Make a commit on your branch
- Create any new file in the `session3_lab/` folder, e.g. `session3_lab/p<N>_notes.md` and type anything in it
- Stage and commit it:
    ```
    git add session3_lab/p<N>_notes.md
    git commit -m "docs: add p<N> notes"
    ```

#### d. Switch branches and watch your files change
- Run `ls session3_lab`. You should see `p<N>_notes.md` alongside the other files
- Run `git log --oneline` to see the commit history
- Run `git switch main`, then `ls session3_lab` again
  - `p<N>_notes.md` has **disappeared** from your folder (and from the left sidebar)
  - Run `git log --oneline` to see the change to commit history
- Run `git switch practice-p<N>`, then `ls session3_lab`
  - Your new file and commit is back


<hr>

<span style="color:salmon">Switching branches changes the files in your working directory to match the latest commit on that branch.</span> Your notes file was never deleted. It only exists on the `practice-p<N>` branch, so it only appears when you are on that branch.

#### e. Create and switch in one step
- `git switch -c <branch>` creates a new branch **and** switches to it, so you don't need `git branch` then `git switch`
- While still on `practice-p<N>`, run:
    ```
    git switch -c oops-p<N>
    ```
  - You should see `Switched to a new branch 'oops-p1'`

#### f. Important to note: where did your new branch start from?
- Run `ls session3_lab`
  - `p<N>_notes.md` is here, even though you created `oops-p<N>` from scratch
  - This is because `git switch -c <branch>` creates the new branch from your **current** branch. You were on `practice-p<N>`, so `oops-p<N>` started with everything on it, including your notes commit
- Now create a branch from `main` instead, without switching to `main` first:
    ```
    git switch -c clean-p<N> main
    ```
- Run `ls session3_lab`
  - `p<N>_notes.md` is not here. `clean-p<N>` started from `main`
- Run `git log --oneline --graph --all` to see where each of your branches points

<hr>

<span style="color:salmon">If you are creating a new feature branch, generally you want to branch off from `main`!</span>

- Either run `git switch main` then `git switch -c <new-branch>`
- Or `git switch -c <new-branch> main` (this creates a new branch, that branches off `main`, then switches you to it)
- Otherwise, you will be branching from your current branch, which may or may not be what you are intending to do, so be aware

<br>

## Activity 4: The Feature Branch Workflow

> Repo: `minions-visitorship`
> Branch: `main` → `feature/p<N>-update`
>
> This is the workflow you will use whenever you add a new feature or change to a team project. We will go through branch naming conventions in Session 6.

#### a. Switch to local `main`, and pull the most recent remote `main`
```
git switch main
git pull
```
- Always start from the latest version of `main`, so your branch starts from the latest code

#### b. Create and switch to a new feature branch
```
git switch -c feature/p<N>-update
```

#### c. Do your work, then stage and commit your changes
- Open `session3_lab/features.py` and replace `return` in **your** function (`participant<N>()`) with a line of your own, e.g. `print("<your name> was here")`
- Stage and commit:
    ```
    git add session3_lab/features.py
    git commit -m "feat(features): update participant<N>"
    ```

#### d. Push your local branch to remote
```
git push -u origin feature/p<N>-update
```
- This is the first push of a new branch, so you need `-u origin <branch>` (Session 2, Activity 5, Situation B)
- You should see:
    ```
    branch 'feature/p1-update' set up to track 'origin/feature/p1-update'.
     * [new branch]      feature/p1-update -> feature/p1-update
    ```

#### e. Find your branch on GitLab
- Go to the `minions-visitorship` repo on GitLab → `Code` → `Branches`
  - You should see your branch, and your teammates' branches once they have pushed
- GitLab may show a `Create merge request` button. **Do not click it yet**. We will go through merge requests in Session 5

#### f. See your teammates' branches
- Run `git branch -a`. Your teammates' branches should not appear yet
- Run `git fetch`, then `git branch -a` again
  - Your teammates' `remotes/origin/feature/p<N>-update` branches are now listed

<hr>

> Your work is now on its own branch, on GitLab, where your team can see it, and `main` has not been touched. In a real project, the next step is to open a merge request so a teammate can review your changes before they are merged into `main` (Session 5).

<br>

## Activity 5: Keeping Your Branch Up to Date with `main`

> Repo: `minions-visitorship`
> Branch: `feature/p<N>-update`
>
> While you work on your feature branch, your teammates keep merging their work into `main`. The longer you wait to bring those changes into your branch, the further behind it falls, and the bigger the merge conflicts you risk later.

> **Facilitator:** merge a new change into `main` now, then tell everyone.

#### a. See that `main` has moved on
- Run `git fetch`
- Run `git log --oneline --graph --all`
  - `origin/main` now has a new commit that your feature branch does not have
  - Your branch and `main` have **diverged**: each has a commit the other does not

#### b. Merge the latest `main` into your feature branch
```
git pull origin main --no-rebase
```
- `git pull origin main` merges the remote `main` into your **current** branch, whichever branch you are on
    - Compare with a plain `git pull`, which only pulls your branch's **own** remote branch (`origin/feature/p<N>-update`)
- `--no-rebase` is needed because your branch and `main` have diverged (Session 2, Activity 6, Situation A)
    - Don't rebase here. Your feature branch has already been pushed, and rebasing would rewrite commits your teammates may already have
- nano opens with a pre-filled merge message, `Merge branch 'main' of ...`. Save and exit to accept it
- Run `ls session3_lab`. The new file from `main` is now on your feature branch

#### c. See the merge, then push it
- Run `git log --oneline --graph`
  - The lines show `main`'s new commit joining your branch at a merge commit
- Run `git push` to update your feature branch on GitLab
  - A plain `git push` works now, as you linked the branch with `-u` in Activity 4

#### d. Update your local `main` too
- `git pull origin main` updated your **feature branch**, but your **local `main`** is still behind
```
git switch main
git pull
git switch feature/p<N>-update
```

<hr>

<span style="color:salmon">Before continuing work on a feature branch, always run `git pull origin main` to make sure you pull any new commits your teammates merged into `main`.</span>

- `origin main` will ensure you pull the unique commits `main` has that your current branch doesnt yet have. Otherwise, `git pull` pulls from the remote equivalent of your current local branch.
- If you get a merge conflict, resolve it exactly as in Session 2, Activity 2
- This is the only kind of merge you should do yourself. **Never** merge your branch into `main` with `git merge`. Instead, open a merge request on GitLab, so only reviewed code is merged into `main` (Session 5)

<br>

## Activity 6: Switching Branches with Uncommitted Changes

> Repo: `minions-visitorship`
> Branch: `feature/p<N>-update`
>
> Uncommitted changes do not belong to any branch. They only exist in your working directory. So what happens to them when you switch branches?

#### a. When Git carries your changes over
- Open `session3_lab/scratch.md`, add a line and save. Do **not** stage or commit
- Run `git switch main`
  - You should see:
    ```
    M	session3_lab/scratch.md
    Switched to branch 'main'
    ```
  - The switch worked, and your uncommitted change **came with you** to `main` (`M` = modified)
  - Git allows this because the unmodified `scratch.md` is the same on both branches, so switching does not need to overwrite it
- Switch back with `git switch feature/p<N>-update`, then discard the change with `git restore session3_lab/scratch.md`

#### b. When Git refuses to switch
- Open `session3_lab/features.py`, edit **your** function again and save. Do **not** stage or commit
- Run `git switch main`
  - You should see:
    ```
    error: Your local changes to the following files would be overwritten by checkout:
            session3_lab/features.py
    Please commit your changes or stash them before you switch branches.
    Aborting
    ```
  - `features.py` is **different** on `main` (your commit from Activity 4 is not on `main`). Switching would overwrite your uncommitted edit with `main`'s version, so Git refuses and keeps you where you are

<hr>

As the error says, you have 2 options:

1. **Commit your changes** first. This is fine if the change is complete, but not if you are halfway through something
2. **Stash your changes**: set them aside temporarily, without committing

**Git Stash**
- Stashing is a way to temporarily set aside **uncommitted** changes without committing them. It's useful when you are in the middle of working in one branch but urgently need to attend to another branch.
- By default, `git stash` captures **modified tracked files and staged changes**, but not untracked files (new files you haven't `git add`ed before) and git ignored files.

#### c. Something urgent comes up: stash, switch, come back
> **Scenario:** You're mid-way through changes on your feature branch, then something urgent comes up and you need to switch to `main`. However, your changes aren't ready to be committed yet.

- You still have your uncommitted edit to `features.py` from step b. Stash it:
    ```
    git stash
    ```
  - You should see `Saved working directory and index state WIP on feature/p1-update: ...`
- Run `git status`. You should see `nothing to commit, working tree clean`. Your edit has been set aside
- Run `git stash list`
  - You should see your stash, e.g. `stash@{0}: WIP on feature/p1-update: ...`
- Run `git switch main`. It works now
- *(Do your urgent work on `main`...)*
- Switch back to your feature branch:
    ```
    git switch feature/p<N>-update
    ```
- Bring your stashed changes back:
    ```
    git stash pop
    ```
  - Your edit to `features.py` is back, still uncommitted
- Run `git stash list`. It is now empty, as `pop` restores the stash **and removes it** from the list

#### d. `pop` vs `apply`
- Stash your edit again with `git stash`
- This time, run `git stash apply`
  - Your edit is back, just like with `pop`
- Run `git stash list`
  - The stash is **still in the list**. `apply` restores the stash but **keeps** it, in case you want to apply it again somewhere else
- Delete it with `git stash drop`
- Discard your edit with `git restore session3_lab/features.py`

#### e. Stashing untracked files
- Create a new file `session3_lab/p<N>_draft.md` and type anything in it. Do **not** stage it
- Run `git stash`
  - You should see `No local changes to save`. New files that have never been staged are not stashed by default
- Run `git stash -u` instead (`-u` is short for `--include-untracked`)
  - `p<N>_draft.md` disappears from your folder into the stash
- Run `git stash pop` to bring it back, then delete the file

<hr>

| Command | Description |
| --- | --- |
| `git stash` | Saves your local modifications away and reverts the working directory to match the `HEAD` commit |
| `git stash -u` | Same, but also includes untracked files |
| `git stash list` | Shows all your stashes |
| `git stash pop` | Restore **most recent** stash and **remove** from stash list |
| `git stash apply` | Restore **most recent** stash **without removing** from stash list |
| `git stash drop` | Delete the most recent stash entry (or a specific one, e.g. `git stash drop stash@{1}`) |
| `git stash clear` | Delete all the stash entries. Note that those entries will then be subject to pruning, and may be impossible to recover |

<br>

## Activity 7: Deleting Branches

> Repo: `minions-visitorship`
> Branch: `main`
>
> Branches are cheap and disposable. Once a branch has been merged, or an experiment didn't work out, delete it to keep the repo tidy.
>
> ⚠️ Keep your `feature/p<N>-update` branch. We will use it in Session 5.

#### a. You cannot delete the branch you are on
- Run `git switch oops-p<N>`, then `git branch -d oops-p<N>`
  - Git refuses with an error like `error: cannot delete branch 'oops-p1' used by worktree at '...'` (the exact wording depends on your Git version)
- Switch away first: `git switch main`

#### b. Delete a branch safely with `-d`
- Run `git branch -d clean-p<N>`
  - You should see `Deleted branch clean-p1 (was ...)`
  - `clean-p<N>` had no commits of its own, so nothing is lost
- Run `git branch -d practice-p<N>`
  - You should see:
    ```
    error: the branch 'practice-p1' is not fully merged
    hint: If you are sure you want to delete it, run 'git branch -D practice-p1'
    ```
  - `practice-p<N>` has a commit (your notes file) that is not on any other branch. `-d` refuses to delete it, to stop you losing work by accident

#### c. Force delete with `-D`
- If you are sure you no longer need the work on a branch, force delete it:
    ```
    git branch -D practice-p<N> oops-p<N>
    ```
  - You can delete several branches at once
  - ⚠️ The commits that were only on those branches are now almost impossible to get back

#### d. Delete a branch on the remote
- Create a throwaway branch and push it:
    ```
    git switch -c temp-p<N> main
    git push -u origin temp-p<N>
    git switch main
    ```
- Check that `temp-p<N>` is on GitLab (`Code` → `Branches`)
- Delete it on the remote:
    ```
    git push origin -d temp-p<N>
    ```
  - You should see ` - [deleted]         temp-p1`
  - Refresh GitLab. The branch is gone
- The **local** `temp-p<N>` still exists. Delete it with `git branch -d temp-p<N>`

<hr>

<span style="color:salmon">`git push origin -d <branch>` deletes the branch on GitLab for **everyone**. Only delete remote branches that you created, and that are no longer needed.</span>

- In practice, you rarely run this yourself. GitLab can delete the source branch automatically when a merge request is merged (Session 5)
- Your teammates may still see a deleted branch in `git branch -r`, until they run `git fetch --prune` (`--prune` removes records of remote branches that no longer exist)

<br>

## Activity 8: FYI: `git checkout`

> `git checkout` is an older command that is considered overloaded, as it does a lot of different things. `git switch` and `git restore` were introduced to split apart `git checkout`'s roles, so it is best to use them instead.
>
> You don't need to use it, but many older tutorials and Stack Overflow answers still use `git checkout`, so you should recognise it.

```bash
# 1. Switching branches                 → git switch <branch>
git checkout <branch>

# 2. Creating a branch and switching    → git switch -c <branch>
git checkout -b feature/new-dashboard

# 3. Restoring a file                   → git restore <file-path>
git checkout -- <file-path>

# 4. Detached HEAD state (Session 4)
git checkout abc1234        # a commit hash, not a branch name
```

<br>

<span style="color:salmon">In this session, we learnt to create, switch, update and delete branches, and to set aside uncommitted work with `git stash` when switching branches.</span>

- Branch off `main`, using `git switch -c <branch> main`
- Run `git pull origin main` often, to keep your feature branch up to date
- Never commit straight to `main`. Your work reaches `main` through a merge request (Session 5)
- Accidentally committed on the wrong branch? We will learn how to move commits between branches in Session 4

<br>

<hr>
<h1 align="center">End of Session 3</h1>
<hr>
