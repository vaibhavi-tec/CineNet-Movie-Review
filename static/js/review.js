let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.closest('tr'); // Use closest to ensure it gets the row
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editID').value = row.cells[0].innerText;
    document.getElementById('editDate').value = new Date(row.cells[1].innerText).toISOString().substr(0, 10);
    document.getElementById('editMovie').value = row.cells[2].innerText;
    document.getElementById('editMessage').value = row.cells[4].innerText;

    // Set the rating stars based on current value
    const ratingSelect = document.getElementById('editRating');
    const starCount = row.cells[3].querySelectorAll('.fas').length;
    ratingSelect.value = starCount; // Set the selected value based on the number of filled stars

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}


function saveEdit() {
    // Update the row with the edited data
    currentRow.cells[0].innerText = document.getElementById('editID').value;
    currentRow.cells[1].innerText = new Date(document.getElementById('editDate').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    currentRow.cells[2].innerText = document.getElementById('editMovie').value;
    currentRow.cells[4].innerText = document.getElementById('editMessage').value;

    const ratingSelect = document.getElementById('editRating');
    const starCount = ratingSelect.value;

    // Update star icons in the table cell
    const starCell = currentRow.cells[3];
    starCell.innerHTML = ''; // Clear existing stars
    for (let i = 0; i < starCount; i++) {
        starCell.innerHTML += '<i class="fas fa-star review-rating"></i>';
    }
    for (let i = starCount; i < 5; i++) {
        starCell.innerHTML += '<i class="far fa-star review-rating"></i>';
    }


    // Close the popup
    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(button) {
    // Remove the row from the table
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

function openCreatePopup() {
    document.getElementById('createPopup').style.display = 'block';
}

function saveCreate() {
    const table = document.getElementById('CategoriesTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.insertCell(0).innerText = document.getElementById('createID').value;
    newRow.insertCell(1).innerText = new Date(document.getElementById('createDate').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    newRow.insertCell(2).innerText = document.getElementById('createMovie').value;
    const rating = document.getElementById('createRating').value;
    newRow.insertCell(3).innerHTML = generateStarsHTML(rating);
    newRow.insertCell(4).innerText = document.getElementById('createMessage').value;

    const actionsCell = newRow.insertCell(5);
    actionsCell.innerHTML = `
        <div class="actions">
            <button class="edit" onclick="editRow(this)">Edit</button>
            <button class="delete" onclick="deleteRow(this)"><i class="fas fa-trash"></i></button>
        </div>
    `;

    closeCreatePopup();
}



function closeCreatePopup() {
    document.getElementById('createPopup').style.display = 'none';
}

function generateStarsHTML(rating) {
    let starsHTML = '';
    for (let i = 1; i <= 5; i++) {
        starsHTML += `<i class="fas fa-star" style="color: ${i <= rating ? '#f5c518' : '#b0b3b8'}"></i>`;
    }
    return starsHTML;
}


function updateStars(starContainerId, rating) {
    const stars = document.querySelectorAll(`#${starContainerId} .fa-star`);
    stars.forEach((star, index) => {
        star.style.color = index < rating ? '#f5c518' : '#b0b3b8';
    });
}

function setRating(value, popupType) {
    document.getElementById(`${popupType}Rating`).value = value;
    updateStars(`${popupType}Stars`, value);
}

// Event listeners for creating and editing stars
document.querySelectorAll('.create-rating .fa-star').forEach(star => {
    star.addEventListener('click', function() {
        setRating(this.dataset.value, 'create');
    });
});

document.querySelectorAll('.edit-rating .fa-star').forEach(star => {
    star.addEventListener('click', function() {
        setRating(this.dataset.value, 'edit');
    });
});

function sortTable(column, order) {
    const table = document.getElementById('CategoriesTable').getElementsByTagName('tbody')[0];
    const rows = Array.from(table.rows);

    rows.sort((a, b) => {
        let valA = '';
        let valB = '';

        switch (column) {
            case 'name':
                valA = a.cells[1].innerText.trim().toLowerCase();
                valB = b.cells[1].innerText.trim().toLowerCase();
                break;
            case 'date':
                valA = new Date(a.cells[3].innerText);
                valB = new Date(b.cells[3].innerText);
                break;
        }

        if (order === 'asc') {
            return valA > valB ? 1 : -1;
        } else {
            return valA < valB ? 1 : -1;
        }
    });

    rows.forEach(row => table.appendChild(row));
}

