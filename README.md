# Notes Maker Chrome Extension

A powerful Chrome extension that allows users to extract text from selected content or an entire webpage, summarize it using an LLM API, and generate a downloadable PDF. Users can also email the summarized content.

## 🚀 Features
- Extract selected text from a webpage
- Extract full-page text
- Summarize text using an LLM API
- Generate a PDF of the summarized content
- Option to email the summary

## 📂 Folder Structure
```
notes-maker/
│── manifest.json
│── popup.html
│── popup.js
│── background.js
│── content.js
│── popup.css
│── server.py
│── summarizer.py
│── pdf_generator.py
│── README.md
```

## 🔧 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/notes-maker.git
   cd notes-maker
   ```
2. Load the extension in Chrome:
   - Open **chrome://extensions/** in your browser.
   - Enable **Developer mode** (toggle in the top-right corner).
   - Click **Load unpacked** and select the project folder.
3. Install dependencies for the backend (Flask server):
   ```sh
   cd server
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file inside the `server/` folder.
   - Add the following:
     ```sh
     API_KEY=your-secret-api-key
     ```

## 🖥️ Usage
1. Click the extension icon in Chrome.
2. Choose **Extract Selected** or **Extract Full Page**.
3. The extension sends the text to the backend for summarization.
4. The summarized text appears with options to **Download PDF** or **Send Email**.

## 🔑 API Key Handling
To keep your API key secure:
- **Do not commit `.env`** (it is in `.gitignore`).
- Manually set the API key in your deployment environment if hosting the server online.
- Use `os.getenv("API_KEY")` in `app.py` to access the key securely.

## 📜 Manifest.json Overview
The `manifest.json` file defines permissions and scripts:
```json
{
  "manifest_version": 3,
  "name": "Notes Maker",
  "version": "1.0",
  "permissions": ["scripting", "activeTab", "storage"],
  "background": { "service_worker": "background.js" },
  "action": { "default_popup": "popup.html" },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ]
}
```

## 💡 Contributing
1. Fork the repo.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Commit changes and push:
   ```sh
   git commit -m "Added new feature"
   git push origin feature-branch
   ```
4. Submit a pull request!

## 🛠️ Troubleshooting
- If the extension does not work, check Chrome's **Developer Console** (`Ctrl + Shift + I` > Console).
- Ensure the Flask server is running before testing the extension.
- API key-related issues? Check `.env` setup and Flask logs.

---

### 🔗 Connect with Me
- GitHub: [yourusername](https://github.com/kamalesh-2003)
- LinkedIn: [Your Name](https://linkedin.com/in/kamalesh-arugunt)

