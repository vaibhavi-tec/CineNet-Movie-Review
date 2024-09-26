let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editName').value = row.cells[1].innerText.trim();
    document.getElementById('editEmail').value = row.cells[2].innerText;
    document.getElementById('editDate').value = row.cells[3].innerText;
    document.getElementById('editFrom').value = row.cells[4].innerText;
    document.getElementById('editTo').value = row.cells[5].innerText;
    document.getElementById('editImage').value = row.cells[0].children[0].src; // Get the image URL

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    currentRow.cells[1].innerText = document.getElementById('editName').value;
    currentRow.cells[2].innerText = document.getElementById('editEmail').value;
    currentRow.cells[3].innerText = document.getElementById('editDate').value;
    currentRow.cells[4].innerText = document.getElementById('editFrom').value;
    currentRow.cells[5].innerText = document.getElementById('editTo').value;
    currentRow.cells[0].children[0].src = document.getElementById('editImage').value; // Update the image URL

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

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById('MovielistTable').getElementsByTagName('tbody')[0];
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


