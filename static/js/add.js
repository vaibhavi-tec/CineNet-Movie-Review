function openAddCastPopup() {
    document.getElementById('addCastPopup').style.display = 'flex';
}

function closeAddCastPopup() {
    document.getElementById('addCastPopup').style.display = 'none';
    document.getElementById('castName').value = '';
    document.getElementById('castImagePreview').style.display = 'none';
}

function previewCastImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const img = document.getElementById('castImagePreview');
        img.src = e.target.result;
        img.style.display = 'block';
    }

    if (file) {
        reader.readAsDataURL(file);
    }
}

function addCastMember() {
    const name = document.getElementById('castName').value;
    const imgSrc = document.getElementById('castImagePreview').src;

    if (!name || !imgSrc) {
        alert('Please provide both a name and an image.');
        return;
    }

    const castList = document.querySelector('.cast-list');

    const castItem = document.createElement('div');
    castItem.className = 'cast-item';
    castItem.innerHTML = `
        <img alt="${name}" height="100" src="${imgSrc}" width="100"/>
        <p>${name}</p>
        <div class="cast-actions">
            <button onclick="editCast(this)">
                <i class="fas fa-edit"></i>
            </button>
            <button onclick="deleteCast(this)">
                <i class="fas fa-trash"></i>
            </button>
        </div>
    `;
    
    castList.appendChild(castItem);
    closeAddCastPopup();
}

// You can add the functions editCast and deleteCast based on your requirements.
function deleteRow(button) {
    // Remove the row from the table
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}