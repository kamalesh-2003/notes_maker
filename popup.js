document.getElementById("extract-selected").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: getSelectedText
        }, (results) => {
            processText(results[0].result);
        });
    });
});

document.getElementById("extract-page").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: getFullPageText
        }, (results) => {
            processText(results[0].result);
        });
    });
});

function processText(text) {
    

    fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text, email: email })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Log the response to inspect the data

        // Check if the PDF URL is valid
        if (data.pdf_url && data.pdf_url.startsWith('http')) {
            let downloadBtn = document.getElementById("download");
            downloadBtn.onclick = () => {
                // Create an anchor element to handle the download
                const a = document.createElement("a");
                a.href = data.pdf_url;
                a.download = "summary_content.pdf"; // Set the name of the PDF
                a.click(); // Trigger the download
            };
            downloadBtn.style.display = "block"; // Show the download button
        } else {
            document.getElementById("status").innerText = "Invalid PDF URL or email sent!";
        }
    });
    
}

function getSelectedText() {
    return window.getSelection().toString();
}

function getFullPageText() {
    return document.body.innerText;
}
