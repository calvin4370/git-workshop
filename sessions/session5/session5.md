# Session 5: Merge Requests and Code Review

As we learnt from Session 3 on Branching, we do not commit our changes straight to `main` to prevent any bad changes from making it straight into production.

Instead, we work on feature branches, until we finish a feature or set of specific changes. Once we are happy with it, we will merge our feature branch into main to merge in our changes.

The workflow for doing this is as follows:

1. We create a feature branch off main, say `pipeline/add-models`
2. We work on our changes in the branch, staging and committing changes locally as we go
    - By commiting changes, they are tracked locally in your local git repo
    - Your teammates cannot see them yet, as all they can see is their own local repo, and the remote repo on GitLab
3. Once we are done (or any time in between commits), we can push our commits to remote
    - This pushes the feature branch to the remote repo on GitLab where everyone in the team can see the code
    - They can now see the changes on the web, or even pull the branch to work on the code locally
4. To merge the feature branch into main (or any other branch), we initiate a merge review on GitLab from our browser.
5. A reviewer, typically someone else on the team, will go through the changes in the feature branch
    - They can leave comments, approve or disapprove the merge request
    - If the merge request is approved, the feature branch's changes can be merged into main
    - This updates the main branch remotely, and other team members need to pull the main branch to get the changes locally.


<br>


## Activity 1: 


<br>


## Activity 2: Fixing a Merge Request Blocked by Merge Conflicts

> Repo: `minions-visitorship`
> Branch: `feature/p<N>-update` (your feature branch from Session 3)
>
> While your feature branch was in progress, a teammate's merge request was merged into `main`, and it changed the **same lines** you changed. Your merge request now has a merge conflict, and GitLab will not let it be merged until the conflict is resolved.
>
> GitLab can resolve simple conflicts in the browser, but you cannot run or test your code there, and for some conflicts GitLab does not offer it at all. Instead, the usual fix is to **merge `main` into your feature branch locally**, resolve the conflict in your own editor, check that everything still works, then push. Once your branch already contains `main`'s changes, there is nothing left for the merge request to conflict with.

> **Facilitator:** merge a change into `main` that changes `return` to `return None` in **all four** `participant<N>()` functions in `session3_lab/features.py`. Each participant changed their own function in Session 3, so everyone will get a conflict on exactly one line.

#### a. See the blocked merge request
- On GitLab, open a merge request from `feature/p<N>-update` into `main` (or open your existing one from Activity 1)
- GitLab shows that the merge request is blocked by merge conflicts (e.g. `Merge blocked: merge conflicts must be resolved`), and the `Merge` button is disabled
- **Do not** click `Resolve conflicts` on GitLab. We will fix it locally instead

#### b. Update your local `main`
```
git switch main
git pull
```
- Your local `main` now has the teammate's change

#### c. Merge `main` into your feature branch
```
git switch feature/p<N>-update
git merge main
```
- `git merge <branch>` merges `<branch>` into your **current** branch. Here, it merges `main` into `feature/p<N>-update`
- You should see:
    ```
    Auto-merging session3_lab/features.py
    CONFLICT (content): Merge conflict in session3_lab/features.py
    Automatic merge failed; fix conflicts and then commit the result.
    ```
- Run `git status`. It says `You have unmerged paths`, and lists `features.py` as `both modified`

#### d. Resolve the conflict
- Open `session3_lab/features.py`. Only **your** function has a conflict. The other three functions were merged automatically, as only `main` changed them:
    ```python
    def participant1():
        return None


    def participant2():
    <<<<<<< HEAD
        print("Participant 2 was here")
    =======
        return None
    >>>>>>> main
    ```
    - Between `<<<<<<< HEAD` and `=======` is **your** version, from your feature branch
    - Between `=======` and `>>>>>>> main` is the version from `main`
- Keep your `print(...)` line, and delete **all** the markers (`<<<<<<<`, `=======`, `>>>>>>>`)
    - In VSCode, you can instead click `Accept Current Change` above the conflict
- Save the file, and run your code to check it still works

#### e. Complete the merge and push
```
git add session3_lab/features.py
git commit
```
- nano opens with a pre-filled message, `Merge branch 'main' into feature/p<N>-update`. Save and exit to accept it
- Run `git log --oneline --graph` to see `main` joining your branch at the merge commit
- Run `git push` to update your feature branch on GitLab

#### f. Check your merge request again
- Refresh your merge request on GitLab
  - The conflict is gone, and the merge request can now be merged
- Leave it open for now

<hr>

<span style="color:salmon">If your merge request has merge conflicts, merge `main` into your feature branch locally, resolve the conflicts, test, then push. The merge request updates automatically.</span>

- `git merge main` uses your **local** `main`, which is why you `git pull` on `main` first. These all do the same thing:
    - `git switch main`, `git pull`, `git switch <feature-branch>`, `git merge main` (updates your local `main` too)
    - `git fetch`, then `git merge origin/main` (merges the remote `main` directly, without updating your local `main`)
    - `git pull origin main --no-rebase` (fetch and merge in one step, as in Session 3, Activity 5)
- Better still, merge `main` into your feature branch **before** you open a merge request, so the conflict never reaches GitLab
- Only ever use `git merge` to bring `main` **into** your feature branch. **Never** merge your feature branch into `main` with `git merge`. That must always go through a reviewed merge request