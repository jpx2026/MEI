# Git commands

## Create a repository from a local folder

Use this workflow when the local folder is not already a Git repository.
First, create an empty repository on GitHub without a README, license, or
`.gitignore`. Then run these commands inside your local project folder.
Replace the example URL below with the URL of your empty repository.

```bash
git init -b main
git add .
git commit -m "First commit"
git remote add origin https://github.com/jpx2026/Notes.git
git push -u origin main
```

- `git init -b main` creates a local repository with an initial branch named `main`.
- `git add .` stages changes in the current folder and its subfolders for the next commit, excluding ignored files.
- `git commit` records the staged changes locally.
- `git remote add origin` stores the remote repository's URL under the name `origin`.
- `git push -u origin main` uploads local commits and sets the remote branch as the upstream for `main`. After this, you can normally use `git push` and `git pull` without extra arguments.

You only need to initialize the repository and configure the remote once.

### What does `-b` mean?

Options (also called flags) change how a command behaves. Their meaning depends
on the command they are used with.

In `git init`, `-b` is short for `--initial-branch`. It sets the initial branch name:

```bash
git init -b main
```

A branch is a line of development in your project. This command names the initial
branch `main`. Without `-b main`, Git uses its configured default branch name.

### What does `-u` mean?

In `git push`, `-u` is short for `--set-upstream`:

```bash
git push -u origin main
```

This command pushes your local `main` branch to the remote named `origin` and
sets `origin/main` as its upstream. An **upstream** is the branch that your local
branch tracks, usually in a remote repository.

Git remembers this relationship. While you are on `main`, you can normally use:

```bash
git push
git pull
```

You generally use `-u` on the first push of each new branch, not on every push.
Cloning normally sets up the upstream for the initially checked-out branch automatically.

## Clone an existing repository onto another computer

Run these commands from the folder where you want to place the project folder:

```bash
git clone https://github.com/jpx2026/Notes.git
cd Notes # Change into the Notes folder
```

`git clone` downloads the repository and its history, checks out the default branch,
and configures `origin` automatically. You do not need to run `git init` again.
You normally do not need to run `git pull` immediately after cloning.

## Everyday workflow on either computer

Run these commands inside the repository. This workflow assumes you have no
uncommitted changes when you start. If `git status` shows pending changes,
handle them before pulling. If Git reports a conflict, resolve it before continuing.

```bash
git status
git pull # Fetch remote changes and integrate them into the current branch

# Edit and save your files in the editor

git status
git diff # Review changes that have not been staged
git add .
git diff --staged # Review the changes included in the next commit
git commit -m "Describe your changes"
git push
```

Use `git add filename` instead of `git add .` to stage a specific file.
`git diff` does not show the contents of new, untracked files; use `git status`
to see which files are untracked.

A commit is local until you push it. When switching computers, push your commits
from the first computer, then pull them on the second computer before editing.
The same workflow applies to the computer where you originally ran `git init`.

## Staging and reviewing changes

The **staging area** holds the changes you have selected for your next commit.
`git add .` stages the current changes in your folder and its subfolders.
It does not create a commit or upload anything.

1. Edit and save your files.
2. Run `git add .` to stage your changes.
3. Run `git commit -m "Describe your changes"` to record the staged changes locally.
4. Run `git push` to upload your commits to the remote.

If you edit a file again after staging it, run `git add` again to include those
newer edits in the next commit.

### `git diff` vs. `git diff --staged`

Both commands display changes without modifying your files.

| Command | What it compares | Question it answers |
| --- | --- | --- |
| `git diff` | Your working files against the staging area | What changes have I not staged yet? |
| `git diff --staged` | The staging area against the last commit | What changes will my next commit include? |

For example, suppose a file in your last commit contains `Hello`.
You change it to `Hello world` and save it. Assuming you have no other changes:

| When you check | `git diff` | `git diff --staged` |
| --- | --- | --- |
| Before `git add .` | Shows the change from `Hello` to `Hello world` | Shows nothing |
| After `git add .` | Shows nothing | Shows the change from `Hello` to `Hello world` |
| After committing | Shows nothing | Shows nothing |

After staging, `git diff` is empty because your saved files match what you staged.
If you edit them again, `git diff` shows those additional, unstaged edits.
Both diff commands can therefore show changes at the same time.

**New files are different:** `git diff` does not display untracked files.
Use `git status` to find them. After `git add .`, their contents appear in
`git diff --staged`.

The usual review order is:

```bash
# Edit and save your files first
git status
git diff           # Review unstaged changes to tracked files
git add .          # Stage your changes
git diff --staged  # Review what your next commit will include
git commit -m "Update Git documentation"
git push
```

From the repository's root folder, `git add .` stages changes throughout the
repository. Check `git status` first to make sure you want to include them all.
