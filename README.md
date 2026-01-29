# Image to Text OCR - Gemini API

Convert images to text using Google Gemini AI. Simple, fast, and accurate OCR powered by state-of-the-art AI.

## 🌟 Features

- **AI-Powered OCR**: Uses Google Gemini Vision API for high-accuracy text extraction
- **Modern Interface**: Clean, beautiful Streamlit interface
- **Multiple Export Options**: Download as TXT or DOCX
- **Smart Extraction**: Works with printed text, handwritten notes, and complex documents
- **No Setup Required**: No need to install Tesseract or other OCR engines
- **Cloud-Ready**: Easily deployable on Streamlit Cloud or Hugging Face Spaces

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## 🔑 API Key Setup

You can provide your Gemini API key in two ways:

1. **Via Sidebar** (Recommended for local use):
   - Enter your API key in the sidebar when the app starts
   
2. **Via Environment Variable** (Recommended for deployment):
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

## 📖 Usage

1. **Enter your Gemini API key** in the sidebar
2. **Upload an image** (PNG, JPG, JPEG, or WEBP)
3. **Click "Extract Text"** and wait for processing
4. **Review and edit** the extracted text if needed
5. **Download** as TXT or DOCX

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to `app.py`
5. Add `GEMINI_API_KEY` as a secret in the Streamlit Cloud settings
6. Deploy!

### Deploy to Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Select "Streamlit" as the SDK
3. Upload all files from this repository
4. Add `GEMINI_API_KEY` as a secret in Space settings
5. Your app will be live!

**Hugging Face Space Configuration**:
- SDK: Streamlit
- Python version: 3.10
- App file: `app.py`

## 📁 Project Structure

```
img-to-text-OCR/
├── app.py                  # Main Streamlit application
├── gemini_ocr.py          # Gemini OCR service
├── requirements.txt       # Python dependencies
├── packages.txt           # System dependencies (for HF deployment)
├── .streamlit/
│   └── config.toml        # Streamlit configuration
└── README.md              # This file
```

## 🎨 Features in Detail

### Simple Mode
- Quick text extraction
- Clean, formatted output
- Ideal for straightforward documents

### Structured Mode
- Advanced document analysis
- Detects document type and language
- Identifies formatting features
- Best for complex documents

### Export Options
- **TXT**: Plain text file with extracted content
- **DOCX**: Formatted Word document with metadata

## ⚙️ Configuration

### Model Selection
- **gemini-1.5-flash**: Faster processing, good accuracy
- **gemini-1.5-pro**: Slower but more accurate, better for complex documents

### Supported Image Formats
- PNG
- JPG/JPEG
- WEBP

## 🔧 Troubleshooting

### API Key Errors
- Ensure your API key is valid
- Check that you have API quota remaining
- Verify the key is correctly entered (no extra spaces)

### Image Upload Issues
- Ensure image is in supported format (PNG, JPG, JPEG, WEBP)
- Try reducing image size if upload fails
- Check image quality - clearer images produce better results

### Poor OCR Results
- Use higher resolution images
- Ensure good lighting and contrast
- Try using `gemini-1.5-pro` model for better accuracy
- For handwritten text, ensure writing is clear and legible

## 💡 Tips for Best Results

1. **Image Quality**: Use high-resolution, well-lit images
2. **Contrast**: Ensure good contrast between text and background
3. **Orientation**: Upload images in correct orientation
4. **File Size**: Larger files may take longer to process
5. **Complex Layouts**: For complex documents, use Structured mode

## 🔒 Privacy & Security

- Images are processed through Google Gemini API
- No images are stored permanently on our servers
- For sensitive documents, run the app locally or use your own API key
- See Google's privacy policy for Gemini API usage

## 📝 License

This project is open source and available for personal and commercial use.

## 🙏 Credits

- **Google Gemini AI**: Powering the OCR capabilities
- **Streamlit**: Modern web framework for the interface
- **python-docx**: Word document generation

## 📧 Support

For issues, questions, or contributions, please open an issue on GitHub or contact the maintainer.

---

Built with ❤️ using Streamlit and Google Gemini AI
