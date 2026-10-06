# Session 3: Facilitator Checklist

## Before the session

1. **Delete leftover branches from Session 2.** On GitLab, go to `Code` → `Branches` and delete `hyperparameter-tuning`. Or, from my local repo:
    ```
    git push origin -d hyperparameter-tuning
    ```

2. **Check the merge method.** Under `Settings` → `Merge requests` → `Merge method`, make sure it's set to `Merge commit`. Activity 5a tells participants they'll see a merge commit.

3. **Add the lab files to `main`.**
    ```
    cd ~/minions-visitorship
    git switch main
    git pull
    git switch -c facilitator/s3-setup
    ```
    - Copy `features.py` and `scratch.md` into a new `session3_lab/` folder
    ```
    git add session3_lab
    git commit -m "chore: add session 3 lab files"
    git push -u origin facilitator/s3-setup
    ```
    - On GitLab, create a merge request from `facilitator/s3-setup` into `main`, tick `Delete source branch`, then merge it
    - If GitLab won't let me merge (e.g. it needs an approval), sort that out now, not during the session

4. **Prepare the Activity 5 change, but don't merge it.**
    ```
    git switch main
    git pull
    git switch -c facilitator/s3-announcement
    ```
    - Copy `announcements.md` into `session3_lab/`
    ```
    git add session3_lab/announcements.md
    git commit -m "docs: add session 3 announcement"
    git push -u origin facilitator/s3-announcement
    ```
    - On GitLab, create a merge request from `facilitator/s3-announcement` into `main`. **Leave it open**

5. **Check what participants will see.** Run `git fetch --prune`, then `git branch -r`. It should match Activity 1b:
    ```
      origin/HEAD -> origin/main
      origin/facilitator/s3-announcement
      origin/main
      origin/s2
    ```

## During the session

6. **At Activity 5:** merge the `facilitator/s3-announcement` merge request on GitLab, then tell everyone: "`main` has been updated, start Activity 5."

## After the session

7. **Keep** everyone's `feature/p<N>-update` branches, since we use them in Session 5.
8. On GitLab, check `Code` → `Branches` for any leftover `temp-p<N>` branches from Activity 7, and delete them.
