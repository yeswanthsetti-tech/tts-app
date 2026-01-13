# GitHub Deployment Guide

## Step 1: Configure Git (One-time setup)

Run these commands in PowerShell (replace with YOUR info):

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com and sign in
2. Click the **"+"** icon → **"New repository"**
3. Repository name: `tts-app` (or any name you like)
4. Choose **Public** or **Private**
5. **DO NOT** check "Initialize with README" (we already have files)
6. Click **"Create repository"**

## Step 3: Connect and Push to GitHub

After creating the repo, GitHub will show you commands. Use these:

```powershell
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"

# Add your GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/tts-app.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Note:** When you run `git push`, GitHub will ask for your username and password. 
- **Username:** Your GitHub username
- **Password:** Use a **Personal Access Token** (not your GitHub password)
  - Get token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
  - Give it `repo` permissions
  - Copy the token and use it as your password

## Step 4: Deploy on Streamlit Cloud

1. Go to https://streamlit.io
2. Sign in with GitHub
3. Click **"Deploy an app"** or **"New app"**
4. Select:
   - **Repository:** `YOUR_USERNAME/tts-app`
   - **Branch:** `main`
   - **Main file path:** `web_app.py`
5. Click **"Deploy"**

Wait a few minutes, then you'll get a public URL like: `https://your-app-name.streamlit.app`

---

## Quick Commands Summary

```powershell
# 1. Set your identity (one-time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 2. Commit your code (already done, but if you make changes later)
git add .
git commit -m "Your commit message"

# 3. Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/tts-app.git
git branch -M main
git push -u origin main
```
