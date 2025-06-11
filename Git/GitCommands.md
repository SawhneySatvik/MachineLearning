# 🧠 Git & GitHub Command Cheat Sheet

---

## 🔧 **1. Git Configuration**

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global color.ui auto
git config --list                      # View all configs
```

---

## 📁 **2. Starting a Project**

```bash
git init                               # Initialize a Git repo in current directory
git clone <repo_url>                   # Clone remote repo locally
```

---

## 📌 **3. Basic Workflow**

```bash
git status                             # Check current status
git add <file>                         # Stage file(s)
git add .                              # Stage all files
git commit -m "Your commit message"    # Commit staged changes
```

---

## 🔄 **4. Syncing with Remote (GitHub)**

```bash
git remote -v                          # View remote URLs
git remote add origin <repo_url>      # Add remote repository
git push -u origin main                # Push first time and set upstream
git push                               # Push committed changes
git pull                               # Fetch & merge remote changes
```

---

## 🌿 **5. Branching**

```bash
git branch                             # List branches
git branch <branch_name>               # Create new branch
git checkout <branch_name>             # Switch to branch
git checkout -b <new_branch>           # Create and switch
git merge <branch_name>                # Merge into current branch
git branch -d <branch_name>            # Delete branch
```

---

## 🕵️ **6. Viewing Changes**

```bash
git log                                # View commit history
git log --oneline                      # Condensed log
git diff                               # View unstaged changes
git diff --staged                      # View staged changes
git show <commit_hash>                 # See specific commit
```

---

## 🔙 **7. Undoing Changes**

```bash
git reset HEAD <file>                  # Unstage file
git checkout -- <file>                 # Discard changes in file
git revert <commit_hash>               # Revert a commit (creates a new one)
git reset --soft HEAD~1                # Undo last commit, keep changes staged
git reset --hard HEAD~1                # Undo last commit & discard changes
```

---

## 🗃️ **8. Stashing (Temporary Save)**

```bash
git stash                              # Save uncommitted changes
git stash list                         # List stashes
git stash pop                          # Apply and remove latest stash
git stash apply                        # Apply stash, keep in stash list
```

---

## 🧪 **9. Tags (Version Releases)**

```bash
git tag                                # List tags
git tag v1.0                           # Create tag
git tag -a v1.0 -m "Version 1.0"       # Annotated tag
git push origin v1.0                   # Push tag to remote
```

---

## 🚀 **10. GitHub-Specific**

### 🔐 Authenticate (One-time)

- Use [GitHub CLI](https://cli.github.com) or SSH token

```bash
gh auth login                         # With GitHub CLI
```

### 🔁 Fork & Pull Request Workflow

```bash
# After forking a repo:
git clone https://github.com/<your-username>/<repo>.git
git remote add upstream https://github.com/<original-owner>/<repo>.git
git fetch upstream
git merge upstream/main
```

> 🧷 Then push and open a PR on GitHub.

---

## ⚙️ **11. Git Aliases (Optional but Useful)**

```bash
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --all"
```

---

## 📦 **12. Miscellaneous**

```bash
git clean -fd                         # Remove untracked files and directories
git blame <file>                      # Show who changed each line
git shortlog -sn                      # Show commits per contributor
```

---
