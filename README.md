# Git Workshop

## Description
The Git workshop is organised into 7 (or 8?) sessions, each taking up to 1 hour.

The sessions are designed to build off from the previous one and should be done sequentially. 

The sessions should be done as close to one another as possible such that participants do not completely forget what was gone through previously.


## Instructions
For each session, follow along the session materials in the `sessions` folder

## Sessions
- Session 0: Intro to Git Basics and GitLab Setup
- Session 1: Local Workflows
- Session 2: Remote Workflows
- Session 3: Branching
- Session 4: Safe Undo of Code Changes
- Session 5: Merge Requests and Code Review
- Session 6: Team Workflow Standards

Session 0 is a pre-workshop session to set up the required environment on analytics@gov and Gitlab

For each session, participants will access this repo to read the session materials (e.g. `session1.md`). Some sessions may require you to access a separate repo concurrently, to practice git commands (e.g. `git clone`).


## Content
Each session's content was derived from my [Git Summary Notes](https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?source=copy_link) on Notion. I group related activities into each session.


## Datasets and materials
`Minions Visitorship` repo
- This is a project simulating an analysis of museum visitorship where all the visitors are minions from the Despicable Me franchise. It is similar to the Overseas Visitorship Survey analysis.
- `minions.csv` contains transaction-level data on visitorship to NHB's museums by the minions
    - It was originally generated using Mirage
    - I then used Python to make hourly transactions follow a more natural distribution throughout the day (Mirage only generates uniform distribution)
- `analysis.ipynb` contains plots and analyses based on the minion visitorship data