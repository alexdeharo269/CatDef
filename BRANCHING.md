# 🌿 Git Branching Guide for AVMD

This document explains how to create a new branch, keep it updated with `main`, and merge it safely.  
Use it as a reference for all branching workflows in this repository.

---

## 🧭 0. Clone the repository (if not yet done)

```bash
git clone https://github.com/yourusername/avmd.git
cd avmd
```

If already cloned:
```bash
cd /path/to/avmd
```

---

## 🌱 1. Create a new branch

Always start from an up-to-date `main`.

```bash
# Update local main
git fetch origin
git checkout main
git pull origin main

# Create and switch to your new branch
git checkout -b feature/your-feature-name

# Work on your files, then stage and commit
git add -A
git commit -m "Start feature: short description"

# Push branch to GitHub and set upstream
git push -u origin feature/your-feature-name
```

---

## 🔄 2. Update your branch with the latest changes from `main`

If others added new commits to `main`, keep your branch up to date.

### Option A — Merge (safe and common)
```bash
git fetch origin
git checkout main
git pull origin main
git checkout feature/your-feature-name
git merge main

# If there are conflicts:
#   fix them manually, then:
git add -A
git commit

git push
```

### Option B — Rebase (cleaner history, advanced)
```bash
git fetch origin
git checkout feature/your-feature-name
git rebase origin/main

# Fix conflicts if any:
git add -A
git rebase --continue

# If you want to abort the rebase:
git rebase --abort

# Push rebased branch
git push --force-with-lease
```

---

## 🔁 3. Merge your branch into `main`

When your feature or fix is finished:

```bash
git fetch origin
git checkout main
git pull origin main
git merge --no-ff feature/your-feature-name
git push origin main
```

Alternatively, open a **Pull Request (PR)** on GitHub and let the team review and merge it.

---

## 🧹 4. Delete the feature branch (optional cleanup)

After merging:

```bash
# Locally
git branch -d feature/your-feature-name

# Remotely
git push origin --delete feature/your-feature-name
```

---

## 💡 Tips

- Use `git status` often to see what’s going on.
- `git fetch` is safe and just updates info about remote changes.
- Prefer `git push --force-with-lease` instead of `--force` to avoid overwriting others’ work.
- Always commit or stash your work before switching branches:
  ```bash
  git stash push -m "WIP before switching"
  git stash pop
  ```

---

## 🔍 Quick Command Reference

| Task | Command |
|------|----------|
| Create & switch to new branch | `git checkout -b feature/your-feature-name` |
| Push new branch to remote | `git push -u origin feature/your-feature-name` |
| Merge latest main into your branch | `git merge main` |
| Rebase your branch on main | `git rebase origin/main` |
| Merge your branch into main | `git merge feature/your-feature-name` |
| Delete local branch | `git branch -d feature/your-feature-name` |
| Delete remote branch | `git push origin --delete feature/your-feature-name` |

---

Maintained for **AVMD project contributors**  
_Last updated: November 2025_
