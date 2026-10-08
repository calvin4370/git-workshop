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


## Activity 1: Viewing the State of the Repo at a Particular Commit

#### a. Switch to the main branch of your local repo
- Run `git branch` to list out the branches on your local repo
- Run `git switch main` to switch to the main branch

#### b. View the State of the Repo at a Particular Commit
- Open the list of commits using `git log --oneline`

```python
git checkout <hash>
```

- This moves HEAD to that commit and updates your working directory to that snapshot. This is useful for quickly inspecting an old version of your project. 
- You land in a **detached HEAD** state (where HEAD points at a commit instead of a branch, so any new commits you make here aren't on any branch). 
- To leave and go back, run `git switch -`


<br>


## Activity 2: Discarding all commits after a particular commit


<br>


## Activity 3: Reverting ONE commit

#### a. Open the list of commits


#### b. Revert the commit `"TODO"`

```python
git revert <hash>
```

- This creates a new commit that cancels out the changes made in the original commit
- Use the flag `--no-edit` to skip the commit-message editor


#### c. Revert the revert


<br>


## Activity 4: Reverting the last commit without deleting your changes

#### a. Make a minor change to `"TODO"`

#### b. Stage the change

#### c. Commit the change with a message

#### d. Revert the last commit but **KEEP the changes staged**

#### e. Repeat parts b. to c. to commit the change again

#### f. Revert the last commit but KEEP the changes unstaged

<hr>

Note: In this activity, we explored 2 ways to revert the last commit, but retain the changes in our working directory. The difference between this and Activity 4 is that the changes were reverted without leaving them in your working directory


<br>


## Activity 5: Discard uncommited changes in your working directory