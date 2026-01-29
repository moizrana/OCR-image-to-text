# Quick Deployment Guide

## 🚀 Deploy to Streamlit Cloud

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Gemini API OCR Application"
git branch -M main

# Create a repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Sign in with GitHub
3. Click **"New app"**
4. Fill in:
   - Repository: `YOUR_USERNAME/YOUR_REPO`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **"Advanced settings"**
6. Add secret:
   ```
   GEMINI_API_KEY = "AIzaSyBaW0Lo4ROcleus_T1qJNKZp6zdFzAUccM"
   ```
7. Click **"Deploy!"**
8. Your app will be live at `https://YOUR_APP.streamlit.app`

---

## 🤗 Deploy to Hugging Face Spaces

### Step 1: Create Space
1. Go to **[huggingface.co/new-space](https://huggingface.co/new-space)**
2. Fill in:
   - Space name: `image-to-text-ocr`
   - License: Your choice
   - SDK: **Streamlit**
   - Hardware: **CPU basic** (free)
3. Click **"Create Space"**

### Step 2: Upload Files
Upload these files to your Space:
- ✅ `app.py`
- ✅ `gemini_ocr.py`
- ✅ `requirements.txt`
- ✅ `packages.txt`
- ✅ `README.md`
- ✅ `.streamlit/config.toml` (create `.streamlit` folder first)

### Step 3: Add API Key Secret
1. Go to your Space **Settings** tab
2. Scroll to **"Repository secrets"**
3. Click **"New secret"**
4. Add:
   - Name: `GEMINI_API_KEY`
   - Value: `AIzaSyBaW0Lo4ROcleus_T1qJNKZp6zdFzAUccM`
5. Click **"Save"**

### Step 4: Wait for Build
- Space will automatically build and deploy
- Check the **"Logs"** tab for build progress
- Once complete, your app will be live!

---

## 📝 Alternative: Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Open browser to http://localhost:8501
```

---

## 🔑 API Key Management

### For Local Development
Option 1: Enter in sidebar when app starts  
Option 2: Set environment variable
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="AIzaSyBaW0Lo4ROcleus_T1qJNKZp6zdFzAUccM"

# Windows CMD
set GEMINI_API_KEY=AIzaSyBaW0Lo4ROcleus_T1qJNKZp6zdFzAUccM

# Linux/Mac
export GEMINI_API_KEY="AIzaSyBaW0Lo4ROcleus_T1qJNKZp6zdFzAUccM"
```

### For Production Deployment
- **Streamlit Cloud**: Use Secrets management in dashboard
- **Hugging Face**: Use Repository secrets in Settings
- **Never commit** API keys to git!

---

## ✅ Deployment Checklist

- [ ] Push code to GitHub
- [ ] Choose deployment platform (Streamlit Cloud or Hugging Face)
- [ ] Create new app/space
- [ ] Configure API key as secret
- [ ] Wait for deployment
- [ ] Test the deployed app
- [ ] Share the URL!

---

## 🎯 Success Criteria

Your deployment is successful when:
1. ✅ App loads without errors
2. ✅ You can upload an image
3. ✅ Text extraction works (requires valid API key)
4. ✅ You can download TXT and DOCX files
5. ✅ App is publicly accessible via URL

---

## 🐛 Troubleshooting

### Build Fails
- Check `requirements.txt` syntax
- Verify all files are uploaded
- Check build logs for specific errors

### API Key Issues
- Verify secret name is exactly `GEMINI_API_KEY`
- Check there are no extra spaces in the key
- Ensure key is valid at [Google AI Studio](https://makersuite.google.com/app/apikey)

### App Crashes
- Check app logs in platform dashboard
- Verify all dependencies installed correctly
- Test locally first to isolate issues

---

**That's it! Your OCR app is now ready for the world! 🌍**
