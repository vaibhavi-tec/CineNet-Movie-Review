let currentRow;

function editRow(button) {
    // Get the row to edit
    const row = button.parentNode.parentNode;
    currentRow = row;

    // Populate the edit form with the row data
    document.getElementById('editName').value = row.cells[1].innerText.trim();
    document.getElementById('editEmail').value = row.cells[2].innerText;
    document.getElementById('editRole').value = row.cells[3].innerText;

    // Show the popup
    document.getElementById('editPopup').style.display = 'block';
}

function saveEdit() 
{
        // Update the row with the edited data
        var username  = document.getElementById('editName').value;
        var password = document.getElementById('editEmail').value;
        var role = document.getElementById('editRole').value;
        // var appointmentid = document.getElementById('editCondition').value;
    // console.log("id: ",id);
        $.ajax({
            type: "POST",
            url: "/api/edit_user/",
            data: {"username": username, "password": password,"role" : role },
            success: function(e)
            {
                window.location.replace("/adminsite/userview");
            }

        });
        if (!currentRow) return; // Prevent saving if no row is selected


    // Close the popup
    closeEditPopup();
}

function closeEditPopup() {
    document.getElementById('editPopup').style.display = 'none';
}

function deleteRow(button) 
{
    //console.log("username: ",username);
    //$.ajax({
    //    type: "POST",
    //    url: "/api/delete_user/",
    //    data: {"username": username},
    //    success: function(d)
    //    {
    //        window.location.replace("/adminsite/use");
    //    }

    //});

    //Remove the row from the table
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
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
