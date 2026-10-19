# Session 5: Merge Requests and Code Review

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
      <td><code>git switch &lt;branch&gt;</code><br><code>git switch -c &lt;branch&gt; &lt;from-branch&gt;</code></td>
      <td>Switch to a branch<br>Create a new branch from <code>&lt;from-branch&gt;</code>, and switch to it</td>
    </tr>
    <tr>
      <td><code>git add &lt;file&gt;</code><br><code>git commit -m "commit message"</code></td>
      <td>Stage a file<br>Commit staged changes</td>
    </tr>
    <tr>
      <td><code>git push</code><br><code>git pull</code></td>
      <td>Upload your commits to your branch on GitLab<br>Download and merge changes from your branch on GitLab</td>
    </tr>
    <tr>
      <td><code>git fetch</code></td>
      <td>Download remote branches and commits <strong>without</strong> merging them</td>
    </tr>
    <tr>
      <td><code>git log --oneline --graph</code><br><code>git log --oneline --first-parent</code></td>
      <td>Commit history, with lines showing where work split and merged<br>Only the commits made directly on the current branch, e.g. one line per merge request merged into <code>main</code></td>
    </tr>
    <tr>
      <td><code>git branch -d &lt;branch&gt;</code></td>
      <td>Delete a local branch (only if merged)</td>
    </tr>
    <tr>
      <td><code>git merge &lt;branch&gt;</code></td>
      <td>Merge <code>&lt;branch&gt;</code> into your <strong>current</strong> branch, e.g. <code>git merge main</code> on your feature branch</td>
    </tr>
    <tr>
      <td><code>git merge --abort</code></td>
      <td>Cancel a merge in progress, and go back to how things were before</td>
    </tr>
    <tr>
      <td><code>git rebase &lt;branch&gt;</code></td>
      <td>Replay your current branch's commits on top of <code>&lt;branch&gt;</code> (Activity 6)</td>
    </tr>
  </tbody>
</table>

> **Tip:** `git log` opens its output in a scrollable viewer when it does not fit on your screen. Press **`q`** to quit.

<br>

## Overview

As we learnt from Session 3 on Branching, we do not commit our changes straight to `main` to prevent any bad changes from making it straight into production.

Instead, we work on feature branches, until we finish a feature or set of specific changes. Once we are happy with it, we will merge our feature branch into main to merge in our changes.

The workflow for doing this is as follows:

1. We create a feature branch off main, say `pipeline/add-models`
2. We work on our changes in the branch, staging and committing changes locally as we go
    - By committing changes, they are tracked locally in your local git repo
    - Your teammates cannot see them yet, as all they can see is their own local repo, and the remote repo on GitLab
3. Once we are done (or any time in between commits), we can push our commits to remote
    - This pushes the feature branch to the remote repo on GitLab where everyone in the team can see the code
    - They can now see the changes on the web, or even pull the branch to work on the code locally
4. To merge the feature branch into main (or any other branch), we initiate a merge request on GitLab from our browser.
5. A reviewer, typically someone else on the team, will go through the changes in the feature branch
    - They can leave comments, approve or disapprove the merge request
    - If the merge request is approved, the feature branch's changes can be merged into main
    - This updates the main branch remotely, and other team members need to pull the main branch to get the changes locally.

>**Roles in a merge request:**
>
>- **Author**: The person who made the changes and opens the merge request
>- **Reviewer**: A teammate who goes through the changes, leaves comments, and approves the merge request (or asks for changes)
>- **Assignee**: The person who actually merges the merge request. This could also be the Author or the Reviewer
>
> Note: Merge requests are called Pull requests (PR) on GitHub. Otherwise, they are essentially the same thing.

<br>

## Setup

#### a. Navigate into the `minions-visitorship` directory
- Run `cd ~/minions-visitorship`
- Run `git status` to check your current branch and make sure your working tree is clean
  - <span style="color:salmon">If you have any uncommitted changes on your current branch, discard them using `git restore .`</span>

#### b. Create a new branch off `main` for this session
- Run `git switch main`
- Run `git pull` to make sure your local `main` is up to date
- Run `git switch -c p<N>-mr main`, where `<N>` is your participant number

#### c. Make a change, then commit and push it
- Open `session5_lab/features.py` and replace `return` in **your** function (`participant<N>()`) with a line of your own e.g. `print("<your name> was here")`
- Run `git add session5_lab/features.py`
- Run `git commit -m "feat(features): update participant<N>"`
- Run `git push -u origin p<N>-mr` <span style="color:skyblue">(the first push of a new branch, so we need `-u origin <branch>`)</span>

#### d. Find out whose merge request you will review
- Each of you will review the merge request of the participant **before** you:
  - Participant 2 reviews Participant 1's merge request
  - Participant 3 reviews Participant 2's merge request
  - Participant 4 reviews Participant 3's merge request
  - Participant 1 reviews Participant 4's merge request

<br>

## Activity 1: Opening a Merge Request

> Repo: `minions-visitorship`
> Branch: `p<N>-mr`
>
> You are the **Author** in this activity.

> **Facilitator:** From here until Activity 4, make sure **nobody merges any merge request**, including the `facilitator/s5-return-none` one. If anything is merged into `main` before Activity 4, the merge conflicts in Activity 4 will not turn out as planned.

#### a. Start a new merge request
- Go to the `minions-visitorship` repo on GitLab
- If you see a `Create merge request` prompt for your branch, click it
- Otherwise, go to `Merge requests` → `New merge request`

#### b. Choose the source and target branches
- Set the **source branch** to `p<N>-mr` <span style="color:skyblue">(the branch with your changes)</span>
- Set the **target branch** to `main` <span style="color:skyblue">(the branch you want to merge your changes into)</span>
- Click `Compare branches and continue`

    ![New merge request on GitLab](../../assets/s5-new-mr.png)

#### c. Fill in the merge request
- Title: describe the change, like a commit message e.g. `feat(features): update participant<N>`
- Description: tell your reviewer what you changed, why, and how to test it, e.g.
    ```
    ## What
    Updated participant<N>() to print a message.

    ## Why
    Session 5 practice.

    ## How to test
    Run `python session5_lab/features.py`. It should print my message.
    ```
- Reviewer: set it to the participant **after** you
- Assignee: also set it to your reviewer. This sends them a notification, and they will merge it later in Activity 5
- Click `Create merge request`

#### d. Look around your merge request
- `Overview` shows the description, comments, and the merge section at the bottom
- `Commits` shows the commits on your branch that are not on `main` yet
- `Changes` shows exactly what your branch changes, line by line

    ![Merge request overview](../../assets/s5-mr-overview.png)

- Do not click `Merge` yet

> Note: If your work is not ready for review yet, you can mark your merge request as a **Draft**. GitLab will not allow it to be merged until you mark it as ready.

<br>

## Activity 2: Reviewing a Merge Request

> Repo: `minions-visitorship`
>
> You are the **Reviewer** in this activity, for the participant before you.

#### a. Review the changes on GitLab
- Go to `Merge requests` and open the merge request you are reviewing
- Open the `Changes` tab
- Hover over their `print(...)` line, and click the comment icon that appears beside it
- Leave a comment asking for a change, e.g. `Could you add a docstring to this function, explaining what it does?`

    ![Leaving a review comment](../../assets/s5-review-comment.png)

- Click `Start a review`, then `Submit review`

#### b. Run their code on your machine
Reading the code is not always enough. As a reviewer, you should also check that the code actually runs.

- Run `git fetch`
- Run `git switch p<M>-mr`, where `<M>` is the number of the participant you are reviewing
  - You should see:

    ```
    branch 'p1-mr' set up to track 'origin/p1-mr'.
    Switched to a new branch 'p1-mr'
    ```

  - You now have a local copy of their branch <span style="color:skyblue">(this is the same as Session 2, Activity 7)</span>
- Run `python session5_lab/features.py`
  - You should see their message printed e.g. `Participant 1 was here`
  - The other three functions still just `return`, so they print nothing
- Run `git switch p<N>-mr` to switch back to your own branch

#### c. Don't approve yet
- You asked for a change, so wait for the Author to make it first (Activity 3)

<br>

## Activity 3: Addressing Review Feedback

> Repo: `minions-visitorship`
> Branch: `p<N>-mr`
>
> You are the **Author** again in this activity.

#### a. Read your reviewer's comment
- Open your merge request on GitLab. Your reviewer's comment is in the `Overview` tab

#### b. Make the change, then commit and push
- Open `session5_lab/features.py` and add a docstring to **your** function, as the first line inside it:
    ```python
    def participant<N>():
        """Print a message from participant <N>."""
        print("<your name> was here")
    ```
- Run `git add session5_lab/features.py`
- Run `git commit -m "docs(features): add docstring to participant<N>"`
- Run `git push`

#### c. Check your merge request
- Refresh your merge request on GitLab
  - Your new commit now shows up in the `Commits` and `Changes` tabs
  - You do not need to open a new merge request. GitLab automatically picks up any new commits pushed to the source branch, and adds them to the open merge request
- Reply to your reviewer's comment e.g. `Done, added a docstring`, then click `Resolve thread`

#### d. Reviewer: approve the merge request
- Check the new change in the `Changes` tab
- Click `Approve`
- Do not merge it yet

<br>

## Activity 4: Fixing Merge Conflicts in a Merge Request
> Repo: `minions-visitorship`
> Branch: `p<N>-mr`
>
> While your merge request was being reviewed, a teammate's merge request was merged into `main`. It changed the **same lines** you changed, so your merge request now has a merge conflict.
>
> I will now merge a merge request into `main` that changes `return` to `return None` in all four `participant<N>()` functions in `session5_lab/features.py`. Since each of you changed your own function, everyone will get a merge conflict on exactly one line.

> **Facilitator:** Merge the `facilitator/s5-return-none` merge request on GitLab now. Once it is merged, tell everyone to refresh their merge request.

#### a. See the blocked merge request
- Refresh your merge request on GitLab
- The merge section at the bottom of the `Overview` tab now shows something like:

    > ⚠️ **Merge blocked:** merge conflicts must be resolved.
    >
    > `Resolve conflicts`  `Resolve locally`

  - The `Merge` button is disabled, so nobody can merge it until the conflict is resolved
  - GitLab gives you 2 options to fix it: `Resolve conflicts` (in the browser) or `Resolve locally` (on your own machine)

<hr>

We will look at both ways. As Participant 1, I will first demonstrate resolving the conflict on GitLab (part b). Then, Participants 2, 3 and 4 will resolve their conflicts locally (part c).

#### b. Demonstration: Resolving the conflict on GitLab
Watch as I resolve the conflict in my merge request on GitLab:

- I click `Resolve conflicts`
- GitLab shows each conflict with both versions side by side: the version from my branch, and the version from `main`. For my function, I choose **my** version <span style="color:skyblue">(the one with my docstring and print line)</span>

- I click `Commit to source branch`
  - GitLab creates a merge commit on my branch on GitLab, and my merge request is no longer blocked
- Note that this commit was made on GitLab, not on my machine, so my local branch is now behind. I run `git pull` to update it

#### c. Participants 2, 3 and 4: Resolve the conflict locally
- Update your local `main`:
  - Run `git switch main`
  - Run `git pull`
- Merge `main` into your feature branch:
  - Run `git switch p<N>-mr`
  - Run `git merge main`
  - You should see:

    ```
    Auto-merging session5_lab/features.py
    CONFLICT (content): Merge conflict in session5_lab/features.py
    Automatic merge failed; fix conflicts and then commit the result.
    ```

- Open `session5_lab/features.py`. Only **your** function has a conflict, as the other three functions were merged automatically:
    ```python
    def participant1():
        return None


    def participant2():
    <<<<<<< HEAD
        """Print a message from participant 2."""
        print("Participant 2 was here")
    =======
        return None
    >>>>>>> main
    ```
- Keep your version, and delete all the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
  - In VSCode, you can click `Accept Current Change` above the conflict instead
- Save the file, and run `python session5_lab/features.py` to check it still works. It should still print your message
- Run `git add session5_lab/features.py`
- Run `git commit`
  - nano opens with a pre-filled message `Merge branch 'main' into p<N>-mr`. Save and exit to accept it
- Run `git push`
- Refresh your merge request on GitLab. The `Merge blocked` message is gone, and the `Merge` button is available again

<hr>

#### d. Compare the two ways

| | Resolve on GitLab | Resolve locally |
| --- | --- | --- |
| Speed | Fast, a few clicks | More steps |
| Can you run or test the result? | No | Yes |
| Works for every conflict? | Only simple text conflicts (not notebooks, renamed files or large conflicts) | Yes |
| Afterwards | Your local branch is behind, so you must `git pull` | Nothing else to do |

<span style="color:salmon">To prevent merge conflicts from reaching GitLab at all, merge the latest `main` into your feature branch locally **before** you open a merge request.</span>

- Only use `git merge` to bring `main` **into** your feature branch. Never merge your feature branch into `main` with `git merge`. That should always go through a merge request
- If you get lost in the middle of a merge, run `git merge --abort` to go back to how things were before

<br>

## Activity 5: Merging the Merge Request

> Repo: `minions-visitorship`
>
> You are the **Reviewer / Assignee** in this activity, for the merge request you reviewed.
>
> We will go one at a time, starting from Participant 1's merge request, then 2, 3 and 4.

#### a. Merge the merge request
- Open the merge request you reviewed. It should be approved, and no longer blocked
- Before clicking `Merge`, look at the options in the merge section:

    ![Merge options](../../assets/s5-merge-options.png)

  - Tick `Delete source branch`. Once merged, the feature branch is no longer needed, so GitLab deletes it for you <span style="color:skyblue">(as mentioned in Session 3, Activity 7)</span>
  - Leave `Squash commits` unticked. This would combine all the commits on the branch into 1 commit on `main`. Some teams prefer this to keep the commit history of `main` short
- Click `Merge`
- Let the next participant know they can go ahead

#### b. Everyone: update your local `main`
- Once all four merge requests have been merged:
  - Run `git switch main`
  - Run `git pull`
- Open `session5_lab/features.py`. All four functions now have their author's docstring and print line
- Run `python session5_lab/features.py`. All four messages are printed, one from each of you
- Run `git log --oneline --graph`
  - With 4 merge requests merged, the lines get tangled and hard to read
- Run `git log --oneline --first-parent` instead
  - `--first-parent` only shows the commits made directly on `main`, so you see one line for each merge request that was merged:
    ```
    196d8b0 Merge branch 'p4-mr' into 'main'
    bc57416 Merge branch 'p3-mr' into 'main'
    fd31dad Merge branch 'p2-mr' into 'main'
    795b288 Merge branch 'p1-mr' into 'main'
    74b1c09 Merge branch 'facilitator/s5-return-none' into 'main'
    ```

#### c. Delete your local feature branch
- Your feature branch was deleted on GitLab, but your local copy is still there
- Run `git branch -d p<N>-mr`
  - This works as the branch has already been merged into `main`
- Run `git fetch --prune` to also clear Git's record of the remote branches that were deleted

<hr>

<span style="color:salmon">The full workflow: branch off `main` → commit → push → open a merge request → review → address feedback → merge `main` in and fix any conflicts → merge the merge request → everyone pulls `main`</span>

<br>

## Activity 6: Git Rebase (Optional)

> - In session 2, we went through `git pull --rebase` and `git pull --no-rebase`
> - Both combine your local commits with new commits from the remote, when the two have diverged:
>     - `--no-rebase` (**merge**): joins the two lines of work with a new **merge commit**. The history shows where the work split and joined back together
>     - `--rebase`: sets your commits aside, moves your branch up to the latest remote commit, then **replays** your commits on top, one by one. The history stays a straight line, with no merge commit, but this <span style="color:salmon">rewrites commit history (which is dangerous if others have pulled the original history)</span>
> - `git rebase <branch>` does the same replaying on its own, without pulling.
>     - For example, on a feature branch, `git rebase main` replays your feature branch's commits on top of the latest `main`. It is an alternative to `git merge main` for bringing your branch up to date
>     - Only rebase commits you have **NOT** pushed to remote yet. Never rebase a branch your teammates are also working on, or their history will no longer match GitLab's (a git mess!)

> Repo: `minions-visitorship`
> Branches: `teammate-p<N>`, `rebase-p<N>`, `merge-p<N>` (all created from `main`)

#### a. Pretend a teammate's work was merged first
- Run `git switch main`
- Run `git pull` to make sure your local `main` is up to date
- Run `git switch -c teammate-p<N> main`
- Create a new file `session5_lab/teammate_p<N>.md` and type anything in it
- Run `git add .`
- Run `git commit -m "docs: add teammate notes"`

#### b. Do your own work and push it
- Run `git switch -c rebase-p<N> main`
- Create a new file `session5_lab/feature_p<N>.md` and type anything in it, then stage and commit it with `git commit -m "feat: add feature file"`
- Add another line to the file, then stage and commit it with `git commit -m "feat: extend feature file"`
- Run `git push -u origin rebase-p<N>` <span style="color:skyblue">(as if you were backing up your work)</span>
- Run `git log --oneline --graph teammate-p<N> rebase-p<N>`
  - At the top, you should see both branches splitting from the same commit (the latest commit on `main`):

    ```
    * 43168a2 docs: add teammate notes
    | * e952bf3 feat: extend feature file
    | * c43bd9e feat: add feature file
    |/
    *   196d8b0 Merge branch 'p4-mr' into 'main'
    ```

#### c. Try merging (on a copy of your branch)
- Run `git switch -c merge-p<N> rebase-p<N>`
- Run `git merge teammate-p<N>`
  - nano opens with a pre-filled merge message. Save and exit to accept it
- Run `git log --oneline --graph`
  - The history splits and joins back together at a merge commit

#### d. Now try rebasing
- Run `git switch rebase-p<N>`
- Run `git log --oneline -n 2` and take note of the hashes of your 2 commits
- Run `git rebase teammate-p<N>`
  - You should see `Successfully rebased and updated refs/heads/rebase-p<N>.`
- Run `git log --oneline --graph`

    ```
    * 5a1e0ae feat: extend feature file      ← was e952bf3
    * 5c224f2 feat: add feature file         ← was c43bd9e
    * 43168a2 docs: add teammate notes
    ```

  - The history is now a straight line, with your 2 commits on top of the teammate's commit
  - Your commits have the same messages and changes, but **different hashes**. Rebasing created new copies of them

#### e. Why you shouldn't rebase commits you have already pushed
- Run `git push`
  - You should see:

    ```
     ! [rejected]        rebase-p1 -> rebase-p1 (non-fast-forward)
    error: failed to push some refs to '<repo URL>'
    ```

- Run `git status`. It says your branch and `origin/rebase-p<N>` have diverged
  - GitLab still has your old commits, while your branch now has new copies of them. The only way to push now is to force push, which would cause a git mess for anyone else who had pulled the branch
  - Note: If a branch is only ever used by you, some teams do rebase it and push with `git push --force-with-lease` (Session 4, Activity 6). Never do this on a shared branch

#### f. Clean up
- Run `git switch main`
- Run `git push origin -d rebase-p<N>` to delete the branch on GitLab
- Run `git branch -D teammate-p<N> rebase-p<N> merge-p<N>` to delete your local branches

<hr>

- `git merge main` keeps your commits as they are, and adds a merge commit. It is safe to use on branches you have already pushed
- `git rebase main` replaces your commits with new copies, and keeps the history in a straight line. Only use it on commits you have not pushed
- If there is a conflict during a rebase, resolve it as usual, run `git add`, then run `git rebase --continue` instead of `git commit` (or `git rebase --abort` to cancel)

<br>

<hr>
<h1 align="center">End of Session 5</h1>
<hr>
