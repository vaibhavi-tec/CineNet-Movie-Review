let currentRow;


function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(username) 
{
    console.log("username: ",username);
    $.ajax({
        type: "POST",
        url: "/adminsite/api/delete_user/",
        data: {"username": username},
        success: function(d)
        {
            window.location.replace("/adminsite/userview");
        }

    });

    //Remove the row from the table
    // const row = button.parentNode.parentNode;
    // row.parentNode.removeChild(row);
}

document.getElementById('filterBtn').addEventListener('click', function() {
    const filterOptions = document.getElementById('filterOptions');
    filterOptions.style.display = filterOptions.style.display === 'none' ? 'block' : 'none';
});

function sortTable(column, order) {
    const table = document.getElementById("UserviewTable");
    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));

    // Define column indices for sorting
    const columnIndex = {
        'name': 1,  // Patient Name
        'date': 3   // Date of Appointment
    }[column];

    rows.sort((a, b) => {
        let valA, valB;

        // Extract values for comparison
        if (column === 'date') {
            // Convert date strings to Date objects for comparison
            valA = new Date(a.cells[columnIndex].innerText);
            valB = new Date(b.cells[columnIndex].innerText);
        } else {
            // For text-based sorting
            valA = a.cells[columnIndex].innerText.trim().toLowerCase();
            valB = b.cells[columnIndex].innerText.trim().toLowerCase();
        }

        if (order === 'asc') {
            if (valA < valB) return -1;
            if (valA > valB) return 1;
            return 0;
        } else {
            if (valA < valB) return 1;
            if (valA > valB) return -1;
            return 0;
        }
    });

    // Re-append sorted rows to the table body
    rows.forEach(row => tbody.appendChild(row));
}

function openCreatePopup() {
    document.getElementById('createPopup').style.display = 'block';
}

function saveCreate() {
    const table = document.getElementById('UserviewTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    
    newRow.insertCell(0).innerText  = document.getElementById('email').value;
    newRow.insertCell(1).innerText = document.getElementById('username').value;
    newRow.insertCell(2).innerText  = document.getElementById('password').value;
    newRow.insertCell(3).innerText  = document.getElementById('role').value;
    newRow.insertCell(4).innerText  = document.getElementById('profile').files[0]; // Get the selected file
    
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


