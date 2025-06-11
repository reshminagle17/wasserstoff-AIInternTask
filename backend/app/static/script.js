async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('uploadResponse').innerText = result.message || JSON.stringify(result);
}

async function askQuery() {
    const queryInput = document.getElementById('queryInput');
    const query = queryInput.value;

    const response = await fetch(`http://127.0.0.1:8000/query/?query=${encodeURIComponent(query)}`);
    const result = await response.json();

    document.getElementById('queryResponse').innerText = JSON.stringify(result, null, 2);
}
