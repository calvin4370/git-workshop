# Session 4: Safe Undo of Code Changes

### Overview
> - In Sessions 1 to 3, you learnt how to make changes, commit them to your local repo, and push them to the remote repo. In this session, you will learn how to undo all of these changes safely.
> - How you undo each change depends on where they have been saved to (See the 4-Areas model of Git below).
>
> 
> **Required**:
> - `Minions Visitorship` repository on GitLab

<br>

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
      <td><code>git log --oneline</code></td>
      <td>View commit history, one line per commit (find commit hashes here)</td>
    </tr>
    <tr>
      <td><code>git switch &lt;branch&gt;</code><br><code>git switch -c &lt;branch&gt; &lt;from-branch&gt;</code></td>
      <td>Switch to a branch<br>Create a new branch from <code>&lt;from-branch&gt;</code>, and switch to it</td>
    </tr>
    <tr>
      <td><code>git push</code><br><code>git push -u origin &lt;branch&gt;</code></td>
      <td>Upload your commits to the remote branch<br>First push of a new branch</td>
    </tr>
    <tr>
      <td><code>git commit --amend -m "corrected message"</code></td>
      <td>Rewrite the message of the last commit (only if not yet pushed)</td>
    </tr>
    <tr>
      <td><code>git restore &lt;file&gt;</code><br><code>git restore .</code></td>
      <td>Discard uncommitted changes to a file<br><strong>Discard all uncommitted changes</strong>. These cannot be recovered</td>
    </tr>
    <tr>
      <td><code>git restore --staged &lt;file&gt;</code><br><code>git restore --staged .</code></td>
      <td>Unstage a file (keep the changes)<br>Unstage all files</td>
    </tr>
    <tr>
      <td><code>git switch --detach &lt;hash&gt;</code><br><code>git switch -</code></td>
      <td>View the repo at a previous commit (detached HEAD)<br>Go back to the branch you were on</td>
    </tr>
    <tr>
      <td><code>git restore --source=&lt;hash&gt; &lt;file&gt;</code></td>
      <td>Set a file back to how it was at a previous commit</td>
    </tr>
    <tr>
      <td><code>git reset --soft HEAD~1</code><br><code>git reset --mixed HEAD~1</code></td>
      <td>Undo the last commit, keep the changes <strong>staged</strong><br>Undo the last commit, keep the changes <strong>unstaged</strong> (the default)</td>
    </tr>
    <tr>
      <td><code>git reset --hard &lt;hash&gt;</code></td>
      <td>⚠️ Move your branch back to <code>&lt;hash&gt;</code> and <strong>throw away</strong> all commits and changes after it</td>
    </tr>
    <tr>
      <td><code>git reflog</code></td>
      <td>List everywhere <code>HEAD</code> has been, to recover "lost" commits</td>
    </tr>
    <tr>
      <td><code>git revert &lt;hash&gt;</code><br><code>git revert &lt;hash&gt; --no-edit</code></td>
      <td>Undo a <strong>pushed</strong> commit, by adding a new commit that does the opposite<br>Same, but skip the commit message editor</td>
    </tr>
    <tr>
      <td><code>git cherry-pick &lt;hash&gt;</code></td>
      <td>Copy a commit onto your current branch</td>
    </tr>
  </tbody>
</table>

> **Tip:** `git log` opens its output in a scrollable viewer when it does not fit on your screen. Press **`q`** to quit.


<br>



>**Background info:**
>
>![The 4 areas of Git](../../assets/git-4-areas.png)
>
>- **Untracked** files are files that have never been staged to Git (`git add`), such as a new file or new pipeline outputs.
>    - Git doesn't track their changes, and `git restore` ignores them.
>    - Once you stage a new file, they become **tracked** by Git
>- **Unstaged** changes are edits to tracked files that you have not staged yet. They exist only in your working directory.
>- **Uncommitted** changes are staged changes you have not committed yet. They're held in the *staging area* until you commit them
>- **Committed changes** are saved permanently in the repo's history as a snapshot.
>- **Pushed changes** are commits uploaded to a remote repo such as one hosted on GitHub, where other people can pull them.


<br>

## Setup
#### a. Navigate into the `minions_visitorship` directory
- Run `cd minions_visitorship`

#### b. Switch to the `main` branch and pull the latest changes to the workshop
- Run `git switch main`
- Run `git pull`
- Run `git branch -r` to show remote branches only
  - Note that the `s4` branch has been created and push to remote for this session
- Run `git branch` to show local branches only
  - You would not yet have a local version of the `s4` branch until you first use `git switch s4` to get Git to create a local version of it. Otherwise, it will not show up in `git branch`

#### c. Switch to the `s4` branch
- Git knows that the branch named `s4` only exists in remote and automatically creates a local copy of it for you before switching you to it

<br>

## Activity 1: Viewing the State of the Repo at a Particular Commit

#### a. Switch to the main branch of your local repo
- Run `git branch` to list out the branches on your local repo
- Run `git switch main` to switch to the main branch

#### b. View the State of the Repo at a Particular Commit
- Open the list of commits using `git log --oneline`

>```python
>git checkout <hash>
>```
> FYI: `git switch --detach <hash>` does the same thing, but does not print the long helpful message that `git checkout <hash>` does
>- This moves HEAD to that commit and updates your working directory to state of the repo as of that commit. This is useful for quickly inspecting and running an old version of your project. 
>- You land in a **detached HEAD** state (where HEAD points at a commit instead of a branch, so any new commits you make here aren't on any branch). 

- Run `git checkout 87c2950`

#### c. What you can do in a detached HEAD state
- Try running `git status` and `git branch`
  - They will confirm that you are in a detached HEAD state
- Run `git log`
  - The latest commit shown is the current commit you are checking out rather than the actual HEAD of the branch
- Make changes to your code / Run your code and produce output
  - This may created new untracked output files or modify tracked files as per normal.
  - You should stash any changes or `git restore .` to clear them before exiting the detached HEAD state
- You can stage and commit changes
  - However, these changes will be committed in a detached HEAD and not to any branch (I would advise against doing this, as it's much simply to just commit to a branch)
  - You will not be able to push or pull changes from a detached HEAD state

> Note: If you run an old version of your project expecting to reproduce old results, they may not match what the code produced back then:
>
> - **Only tracked files go back in time.** New files that were never staged before and gitignored files (e.g. `*.csv` input data), stay as they are today. This means old code will run on **today's** data
> - **Package versions don't go back in time either.** The old code runs with the packages currently installed. If a package has changed since, the old code may break or behave differently. The old commit's `requirements.txt` tells you which versions it expects

#### d. Leave the detached HEAD state
- Run `git switch -` to leave the detached HEAD state
- Run `git status` to confirm you are back in thee `s4` branch
- Run `git log --oneline`
  - HEAD should now point at the actual latest commit for this branch


<br>

## Activity 2: Discarding Uncommitted Changes

#### a. Create a new branch for practicing undoing changes
- Run `git switch -c undo-p<N>`, where `<N>` is your participant number

#### b. Make changes
- Open `session4_lab/config.py` and change any of the variables
- Open `session4_lab/pipeline.py`, make any destructive change to the script e.g. modifying a line, introducing syntax errors, clearing the whole file
- Run `git status`. Both files should be shown as `modified`


#### c. Discard your uncommitted changes
- Discard the change to `config.py` only:
    ```
    git restore session4_lab/config.py
    ```
- Run `git status`. Only `pipeline.py` is still modified

- Run:
    ```
    git restore .
    ```
- Run `git status`. You should see `nothing to commit, working tree clean`

> ⚠️ <span style="color:salmon">`git restore` permanently discards your changes. There is no undo or dry-run (`-n`) for this command</span>

#### c. Unstage a change
- Change `YEAR` in `config.py` again, and stage it with `git add session4_lab/config.py`
- Unstage it:
    ```
    git restore --staged session4_lab/config.py
    ```
- Run `git status`. `config.py` is back under `Changes not staged for commit`. Your change is still there, it is just no longer staged
- Discard it with `git restore session4_lab/config.py`

#### d. Untracked files are not affected
- Create a new file `session4_lab/untracked_p<N>.md` and type anything in it
- Run `git restore .`, then `git status`
  - `untracked_p<N>.md` is still there, under `Untracked files`
  - `git restore` only works on files Git is tracking. Git has never saved a version of this file, so there is nothing to restore it to
- Delete the file

## Activity 3: Undoing Your Last Commit, but Keeping the Changes

> Repo: `minions-visitorship`
> Branch: `undo-p<N>`
>
> You committed too early, or committed the wrong files, and you have **NOT pushed yet**. You want to undo the commit, but keep the work you did.

#### a. Make a commit to undo
- Open `session4_lab/notes.md`, add a line, e.g. `- Participant <N> was here`, and save
- Stage and commit it:
    ```
    git add session4_lab/notes.md
    git commit -m "docs(notes): add p<N> line"
    ```
- Run `git log --oneline -n 2`. Your commit is at the top

#### b. Undo it, keeping the changes staged
```
git reset --soft HEAD~1
```
- `HEAD~1` means "1 commit before where I am now". `reset` moves your branch back to that commit
  - `--soft` only undoes the commit. Your changes stay in the staging area, ready to be committed again

- Run `git log --oneline -n 1`. Your commit is gone, and `docs(notes): update notes` is at the top again
- Run `git status`. Your change to `notes.md` is still there, **staged**, under `Changes to be committed`


#### c. Commit it again, then undo it, keeping the changes unstaged
- Commit it again: `git commit -m "docs(notes): add p<N> line"`
- This time, run:
    ```
    git reset --mixed HEAD~1
    ```
    - `--mixed` undoes the commit **and** unstages the changes. It is the default, so `git reset HEAD~1` does the same thing

  - You should see:
    ```
    Unstaged changes after reset:
    M	session4_lab/notes.md
    ```
- Run `git status`. Your change is still there, but now **unstaged**, under `Changes not staged for commit`

- Discard the change with `git restore session4_lab/notes.md`

<hr>

| Command | The commit | Your changes |
| --- | --- | --- |
| `git reset --soft HEAD~1` | Undone | Kept, **staged** |
| `git reset --mixed HEAD~1` | Undone | Kept, **unstaged** |

- To undo more than one commit, change the number, e.g. `git reset --soft HEAD~3` undoes your *last 3 commits*
- If you only want to fix the **message** of your last commit, `git commit --amend -m "corrected message"` is simpler (Session 1)


<br>


## Activity 4: Discarding ALL commits AFTER a particular commit
> Repo: `minions-visitorship`
> Branch: `undo-p<N>`
>
> Your last few commits went down the wrong path, and you want to throw them away completely, as if they never happened.
> This activity goes through how to reset the state of your branch back to the state of a previous commit, whilst deleting all commits that come after it, from the commit history.

#### a. Go back to an earlier commit, and discard everything after it
- Run `git log --oneline` and copy the hash of a commit you want to restore the branch to
- Run:
    ```
    git reset --hard <hash>
    ```
  - You should see `HEAD is now at <hash> <that commit's message`
- Run `git log --oneline`. All the commits after the chosen commit are gone, and the chosne commit is now the HEAD
- Run `git status`. `working tree clean`: unlike `--soft` and `--mixed`, `--hard` does **not** keep your changes in the working directory

<hr>

<span style="color:salmon">`git reset --hard` is a destructive command. It throws away the commits after `<hash>`, **and** any uncommitted changes in your working directory.</span>

- Uncommitted changes thrown away by `--hard` cannot be restored
- Only use it on commits you have **NOT** pushed, as deleting pushed commits rewrites commit history that your teammates may have already pulled!



<br>


## Activity 5: The Safety Net: `git reflog`

> Repo: `minions-visitorship`
> Branch: `undo-p<N>`
>
> You just threw away 3 commits with `git reset --hard`. What if you didn't mean to?
>
> Git keeps a log of everywhere `HEAD` has been on your machine, called the **reflog**. Commits you "threw away" are not deleted straight away, so you can use the reflog to find them and get them back.

#### a. Look at the reflog
```
git reflog
```
- You should see something like:
    ```
    48d6268 (HEAD -> undo-p1) HEAD@{0}: reset: moving to 48d6268
    ba97285 HEAD@{1}: reset: moving to HEAD~1
    ...
    ```
  - `HEAD@{0}` is where you are now: just after the `reset --hard`
  - `HEAD@{1}` is where you were **just before** it: `ba97285`, the `docs(notes): update notes` commit

#### b. Get your commits back
```
git reset --hard HEAD@{1}
```
- Run `git log --oneline`. All commits are back

<hr>

- The reflog only exists on **your** machine, and only for actions you did. It is not pushed to GitLab
- It can also recover branches you deleted with `git branch -D` (Session 3, Activity 7): find the last commit of that branch in the reflog, then run `git switch -c <branch> <hash>`
- It cannot recover **uncommitted** changes, as they were never saved in a commit



<br>


## Activity 6: Reverting the last commit without deleting your changes

#### a. Make a minor change to `"TODO"`

#### b. Stage the change

#### c. Commit the change with a message

#### d. Revert the last commit but **KEEP the changes staged**

#### e. Repeat parts b. to c. to commit the change again

#### f. Revert the last commit but KEEP the changes unstaged

<hr>

Note: In this activity, we explored 2 ways to revert the last commit, but retain the changes in our working directory. The difference between this and Activity 4 is that the changes were reverted without leaving them in your working directory


<br>


## Activity 7: Discard uncommited changes in your working directory



<br>


## Activity 8: Git Rebase
> - In session 2, we went through `git pull --rebase` and `git pull --no-rebase`
> - Both combine your local commits with new commits from the remote, when the two have diverged:
>     - `--no-rebase` (**merge**): joins the two lines of work with a new **merge commit**. The history shows where the work split and joined back together
>     - `--rebase`: sets your commits aside, moves your branch up to the latest remote commit, then **replays** your commits on top, one by one. The history stays a straight line, with no merge commit, but this <span style="color:salmon">rewrites commit history (which is dangerous if others have pulled the original history)</span>
> - `git rebase <branch>` does the same replaying on its own, without pulling. 
>   - For example, on a feature branch, `git rebase main` replays your feature branch's commits on top of the latest `main`. It is an alternative to `git merge main` for bringing your branch up to date
>   - Only rebase commits you have **NOT** pushed to remote yet. Never rebase a branch your teammates are also working on, or their history will no longer match GitLab's (a git mess!)