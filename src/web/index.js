function ytDownload_py() {
    const link = document.getElementById('link').value;
    response = eel.ytDownload(link);
    if (response) {
        alert('Finished downloading!');
    }
}
