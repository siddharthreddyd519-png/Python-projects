# Git & GitHub – Beginner Notes

## 1. What is Git?
Git is a version control system used to track changes in files and code. It allows developers to record changes, recover files, and collaborate.

## 2. What is GitHub?
GitHub is an online platform where Git repositories can be stored and shared.

- Git = Version control tool.
- GitHub = Online platform to host Git repositories.

---

## 3. Configure Git

Configure your name and email so Git can identify you in commits.

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Check your configuration:

```bash
git config --global --list
```

---

## 4. Create a Repository

Create a folder:

```bash
mkdir git-practice
cd git-practice
```

Initialize Git:

```bash
git init
```

`git init` initializes a Git repository inside the folder.

---

## 5. Check Repository Status

```bash
git status
```

Shows:
- Untracked files
- Modified files
- Staged files
- Current branch

---

## 6. Git Staging Area

Add a file to the staging area:

```bash
git add hello.py
```

Add all files:

```bash
git add .
```

`git add` prepares changes for the next commit.

---

## 7. Commit Changes

```bash
git commit -m "Create hello.py"
```

A commit records a snapshot of the staged changes in Git history.

---

## 8. View Commit History

```bash
git log
```

Shows detailed commit history, including date and time.

```bash
git log --oneline
```

Shows a compact version of commit history.

---

## 9. Connect Local Repository to GitHub

```bash
git remote add origin https://github.com/username/repository.git
```

- `remote` = Remote repository configuration.
- `add` = Add a new remote.
- `origin` = Common name for the remote repository.
- URL = Address of your GitHub repository.

---

## 10. Rename the Branch

```bash
git branch -M main
```

Renames the current branch to `main`.

---

## 11. Push Code to GitHub

```bash
git push -u origin main
```

Uploads local commits to GitHub.

For subsequent pushes:

```bash
git push
```

`push` sends committed changes from your local repository to the remote repository.

---

## 12. Pull Changes from GitHub

```bash
git pull origin main
```

Downloads and integrates changes from the remote `main` branch into your local branch.

### Example:
1. Create or edit a README.md on GitHub.
2. Commit the change on GitHub.
3. Run `git pull origin main` locally.
4. The changes will be integrated into your local repository.

---

# 13. Recover a Deleted File

## Scenario 1: Deleted but NOT committed

If you accidentally delete a file and haven't committed the deletion:

```bash
git restore hello.py
```

Restores the file from the latest committed version.

### Workflow:
1. Delete the file.
2. Run `git status`.
3. Run `git restore hello.py`.
4. The file is restored.

---

## Scenario 2: Deleted and COMMITTED

If the deletion was committed, use Git history to find an earlier version.

### Step 1: View commit history

```bash
git log --oneline
```

Find the commit ID where the file existed.

### Step 2: Recover the file

```bash
git checkout <commit-id> -- hello.py
```

Example:

```bash
git checkout 0ce4811 -- hello.py
```

This retrieves `hello.py` from the specified historical commit without reverting the entire repository.

---

# 14. Git Workflow

### Uploading new changes

```bash
git add .
git commit -m "Describe changes"
git push
```

### Downloading remote changes

```bash
git pull origin main
```

### Checking status

```bash
git status
```

---

# 15. Important Commands – Quick Revision

| Command | Purpose |
|---|---|
| `git config` | Configure Git identity |
| `git init` | Initialize a repository |
| `git status` | Check repository status |
| `git add` | Stage changes |
| `git commit` | Record changes |
| `git log` | View commit history |
| `git log --oneline` | Compact commit history |
| `git remote add origin` | Connect to GitHub |
| `git branch -M main` | Rename branch |
| `git push` | Upload commits |
| `git pull` | Integrate remote changes |
| `git restore filename` | Restore uncommitted file changes |
| `git checkout commit-id -- filename` | Recover a file from a historical commit |

---

## 16. Git Upload Flow

Create/Edit File  
↓  
`git init`  
↓  
`git add .`  
↓  
`git commit -m "message"`  
↓  
`git remote add origin URL`  
↓  
`git branch -M main`  
↓  
`git push -u origin main`

---

## 17. Remember

- **Git** tracks changes.
- **GitHub** hosts repositories online.
- **Add** stages changes.
- **Commit** records changes.
- **Push** uploads commits.
- **Pull** integrates remote changes.
- **Restore** recovers uncommitted changes or deletions.
- **Log** displays commit history.

## 7. Git Remote Commands (Connecting to GitHub)

### 1. Check connected repositories
```bash
git remote -v
```
**Purpose:** Displays the remote repository URLs connected to your local project.

---

### 2. Add a new remote repository
```bash
git remote add origin https://github.com/username/repository.git
```
**Purpose:** Connects your local Git repository to a GitHub repository.

- `remote` → manages remote connections.
- `add` → adds a new remote.
- `origin` → the nickname of the remote.
- `URL` → the GitHub repository address.

---

### 3. Change an existing remote URL
```bash
git remote set-url origin https://github.com/username/new-repository.git
```
**Purpose:** Changes the URL associated with an existing remote named `origin`.

**Use this when:** Your local project is connected to the wrong GitHub repository.

---

### 4. Remove a remote repository
```bash
git remote remove origin
```
**Purpose:** Removes the remote connection named `origin` from your local repository.

**Note:** This does not delete your local files or the GitHub repository itself.

---

### 5. Push your code to GitHub
```bash
git push -u origin main
```
**Purpose:** Uploads your local commits to the GitHub `main` branch and establishes upstream tracking.

- `push` → uploads commits.
- `origin` → remote repository name.
- `main` → branch name.
- `-u` → establishes upstream tracking for future pushes.

---

### Quick Revision

| Command | What it does |
|---|---|
| `git remote -v` | View remote URLs |
| `git remote add origin <URL>` | Add a remote |
| `git remote set-url origin <URL>` | Change remote URL |
| `git remote remove origin` | Remove a remote |
| `git push -u origin main` | Push commits to GitHub |

