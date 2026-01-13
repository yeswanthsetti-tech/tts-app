# Step-by-Step Deployment Guide for yeswanthsetti-tech

## ✅ Step 1: COMPLETED (Already Done!)
- ✅ Git configured with your name and email
- ✅ Code committed locally
- ✅ All files ready to push

---

## 📝 Step 2: Create GitHub Repository

1. **Go to GitHub**: https://github.com/yeswanthsetti-tech
2. **Click the green "New" button** (or go to https://github.com/new)
3. **Repository settings**:
   - **Repository name**: `tts-app` (or any name you like, e.g., `text-to-speech-app`)
   - **Description**: "Text-to-Speech application with CLI and Streamlit web app"
   - **Visibility**: Choose **Public** (for free Streamlit hosting) or **Private**
   - **⚠️ IMPORTANT**: Do NOT check "Add a README file" (we already have one)
   - **Do NOT** add .gitignore or license (we already have .gitignore)
4. **Click "Create repository"**

---

## 🚀 Step 3: Push Your Code to GitHub

After creating the repository, GitHub will show you commands. **Use these exact commands** (I've customized them for you):

### Option A: If repository name is `tts-app`:

```powershell
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"

git remote add origin https://github.com/yeswanthsetti-tech/tts-app.git
git branch -M main
git push -u origin main
```

### Option B: If you chose a different repository name (e.g., `text-to-speech-app`):

```powershell
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"

git remote add origin https://github.com/yeswanthsetti-tech/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

**Replace `YOUR-REPO-NAME` with your actual repository name.**

---

## 🔐 Step 4: Authentication (When Git Asks for Credentials)

When you run `git push`, GitHub will ask for:
- **Username**: `yeswanthsetti-tech`
- **Password**: Use a **Personal Access Token** (NOT your GitHub password)

### How to Get Personal Access Token:

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. **Token settings**:
   - **Note**: "TTS App Deployment"
   - **Expiration**: Choose 90 days or No expiration
   - **Select scopes**: Check ✅ **`repo`** (this gives full repository access)
4. Click **"Generate token"**
5. **⚠️ COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
6. When Git asks for password, **paste this token** (not your GitHub password)

---

## 🌐 Step 5: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**: https://streamlit.io/cloud
2. **Sign in** with your GitHub account (`yeswanthsetti-tech`)
3. **Click "Deploy an app"** or **"New app"**
4. **App settings**:
   - **Repository**: Select `yeswanthsetti-tech/tts-app` (or your repo name)
   - **Branch**: `main`
   - **Main file path**: `web_app.py`
   - **App URL** (optional): Choose a custom name like `tts-app` or leave default
5. **Click "Deploy"**
6. **Wait 2-3 minutes** for deployment
7. **Your app will be live at**: `https://YOUR-APP-NAME.streamlit.app`

---

## 📋 Quick Command Summary

```powershell
# Navigate to project
cd "C:\Users\yeswanth setti\OneDrive\Desktop\task1"

# Connect to GitHub (replace tts-app with your actual repo name)
git remote add origin https://github.com/yeswanthsetti-tech/tts-app.git

# Ensure branch is main
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## ⚠️ Important Notes

1. **If you get "remote already exists" error**:
   ```powershell
   git remote remove origin
   git remote add origin https://github.com/yeswanthsetti-tech/tts-app.git
   ```

2. **If you make changes later and want to push again**:
   ```powershell
   git add .
   git commit -m "Your commit message"
   git push
   ```

3. **Streamlit Cloud Note**: `pyttsx3` may not work on Streamlit Cloud (it needs system audio). If deployment fails, we can switch to `gTTS` (Google Text-to-Speech) which works in the cloud.

---

## 🎯 Your GitHub Profile

Your profile: https://github.com/yeswanthsetti-tech

After pushing, your repository will be visible at:
- https://github.com/yeswanthsetti-tech/tts-app

---

## ✅ Checklist

- [ ] Created GitHub repository
- [ ] Ran `git remote add origin` command
- [ ] Ran `git push -u origin main` command
- [ ] Entered Personal Access Token when prompted
- [ ] Code successfully pushed to GitHub
- [ ] Deployed on Streamlit Cloud
- [ ] App is live and working!

---

**Need help?** If you get stuck at any step, tell me the exact error message and I'll help you fix it!
