// Listener for messages from the popup or background script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "summarize") {
        let selectedText = window.getSelection().toString().trim();
        let textToSummarize = selectedText || document.body.innerText; // Use selected text or full page

        // Send extracted text to the backend API
        fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: textToSummarize }),
        })
        .then(response => response.json())
        .then(data => {
            // Send the summarized text back to the popup.js to display
            chrome.runtime.sendMessage({ action: "showSummary", summary: data.summary });
        })
        .catch(error => console.error("Error:", error));
    }
});
