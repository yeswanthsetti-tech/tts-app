# Create GitHub Repository Using Your Token

## Option 1: Use the PowerShell Script (Easiest)

I've created a script for you! Here's how to use it:

### Step 1: Run the script with your token

Open PowerShell and run:

```powershell
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"

.\create_repo.ps1 -Token "YOUR_GITHUB_TOKEN_HERE" -RepoName "tts-app"
```

**Replace `YOUR_GITHUB_TOKEN_HERE` with your actual GitHub Personal Access Token.**

The script will:
1. ✅ Create the repository on GitHub
2. ✅ Connect your local code to it
3. ✅ Push all your code automatically

---

## Option 2: Manual Creation (If script doesn't work)

### Step 1: Create Repository via Web

1. Go to: https://github.com/new
2. Repository name: `tts-app`
3. Choose Public
4. **Don't check any boxes**
5. Click "Create repository"

### Step 2: Push Code Using Token

After creating the repo, run these commands:

```powershell
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"

git remote add origin https://github.com/yeswanthsetti-tech/tts-app.git
git branch -M main
git push -u origin main
```

When asked for credentials:
- **Username**: `yeswanthsetti-tech`
- **Password**: Paste your **GitHub Personal Access Token** (not your password)

---

## How to Get Your GitHub Token

If you don't have a token yet:

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. **Note**: "TTS App"
4. **Expiration**: 90 days or No expiration
5. **Select scopes**: Check ✅ **`repo`**
6. Click **"Generate token"**
7. **Copy the token immediately** (you won't see it again!)

---

## Quick Command (Copy & Paste)

```powershell
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"
.\create_repo.ps1 -Token "PASTE_YOUR_TOKEN_HERE"
```

**Just replace `PASTE_YOUR_TOKEN_HERE` with your actual token!**
