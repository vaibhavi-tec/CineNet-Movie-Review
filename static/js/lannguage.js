let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.closest('tr'); // Use closest to ensure it gets the row
    currentRow = row;
    

    // Populate the edit form with the row data
    document.getElementById('editName').value = row.cells[0].innerText;
    document.getElementById('editEmail').value = new Date(row.cells[1].innerText).toISOString().substr(0, 10);
    document.getElementById('editDate').value = row.cells[2].innerText;
    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() {
    // Update the row with the edited data
    currentRow.cells[0].innerText = document.getElementById('editName').value;
    currentRow.cells[1].innerText = new Date(document.getElementById('editEmail').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    currentRow.cells[2].innerText = document.getElementById('editDate').value;

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

function openCreatePopup() {
    document.getElementById('createPopup').style.display = 'block';
}

function saveCreate() {
    const table = document.getElementById('CategoriesTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    
    newRow.insertCell(0).innerText = document.getElementById('createID').value;
    newRow.insertCell(1).innerText = new Date(document.getElementById('createDate').value).toLocaleDateString('en-US', { day: '2-digit', month: 'short', year: 'numeric' });
    newRow.insertCell(2).innerText = document.getElementById('createTitle').value;
    
    const actionsCell = newRow.insertCell(3);
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


