async function ytDownload_py() {
    const link = document.getElementById('link').value;
    response = await eel.ytDownload(link)();
    alert('Finished downloading!');
}
