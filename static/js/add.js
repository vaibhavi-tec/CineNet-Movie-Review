
// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
    // Event listener for the publish button
    // Function to update the displayed star rating based on selected review
    function updateStars() {
        const rating = document.getElementById('rating').value;
        console.log('Selected rating:', rating);
        // Add logic to update stars based on the rating selected
    }
    

    // Function to handle file input click for movie poster and banner
    function triggerFileUpload(inputId) {
        document.getElementById(inputId).click();
    }

    // Function to handle adding a new cast member (this is a placeholder)
    function openAddCastPopup() {
        alert("Open popup to add a new cast member.");
    }

    // Function to delete a cast member row
    function deleteRow(button) {
        const castItem = button.closest('.cast-item');
        if (castItem) {
            castItem.remove();
        }
    }

    document.getElementById('my-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const title = document.getElementById('movie-title').value;
        console.log('Movie Title:', title);
        const duration = document.getElementById('movie-duration').value;
        const language = document.getElementById('language-used').value;
        const year = document.getElementById('year-of-release').value;
        const director = document.getElementById('Director-used').value;
        const writer = document.getElementById('Writer').value;
        const stars = document.getElementById('stars').value;
        
        const ratingElement = document.getElementById('rating');
        const reviews = ratingElement ? ratingElement.value : '';
        const description = document.getElementById('movie-description').value;
        const category = document.getElementById('movie-category').value;
        const videoLink = document.getElementById('movie-video').value;

        // Create a new row in the movies table
        const moviesTable = document.getElementById('MovielistTable');
        const newRow = moviesTable.insertRow();

        // Insert cells with movie data
        newRow.insertCell(0).innerText = title;
        newRow.insertCell(1).innerText = duration;
        newRow.insertCell(2).innerText = language;
        newRow.insertCell(3).innerText = year;
        newRow.insertCell(4).innerText = director;
        newRow.insertCell(5).innerText = writer;
        newRow.insertCell(6).innerText = stars;
        newRow.insertCell(7).innerText = reviews;
        newRow.insertCell(8).innerText = description;
        newRow.insertCell(9).innerText = category;
        newRow.insertCell(10).innerText = videoLink;

        // Create actions cell
        const actionsCell = newRow.insertCell(11);
        actionsCell.innerHTML = `
            <div class="actions">
                <button class="edit" onclick="editRow(this)">Edit</button>
                <button class="delete" onclick="deleteRow(this)"><i class="fas fa-trash"></i></button>
            </div>
        `;

        // Clear form fields after submission
        document.getElementById('movie-title').value = '';
        document.getElementById('movie-duration').value = '';
        document.getElementById('language-used').value = '';
        document.getElementById('year-of-release').value = '';
        document.getElementById('Director-used').value = '';
        document.getElementById('Writer').value = '';
        if (starsElement) starsElement.value = ''; // Clear if exists
        document.getElementById('movie-description').value = '';
        document.getElementById('movie-category').selectedIndex = 0; // Reset to first option
        document.getElementById('movie-video').value = '';
    });

    // Other functions and event listeners can go here
});


















function openAddCastPopup() {
    document.getElementById('addCastPopup').style.display = 'flex';
}

function closeAddCastPopup() {
    document.getElementById('addCastPopup').style.display = 'none';
    document.getElementById('castName').value = '';
    document.getElementById('castImage').value = ''; // Clear the file input
    document.getElementById('castImagePreview').style.display = 'none';
}

function previewCastImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const img = document.getElementById('castImagePreview');
        img.src = e.target.result;
        img.style.display = 'block';
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}


function displayCastMember(name, imageFile) {
    const castList = document.querySelector('.cast-list');
    const reader = new FileReader();

    reader.onload = function(e) {
        const castItem = document.createElement('div');
        castItem.className = 'cast-item';
        castItem.innerHTML = `
            <img alt="${name}" height="100" width="100" src="${e.target.result}"/>
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
    };

    reader.readAsDataURL(imageFile); // Read the image as a data URL
}

function deleteCast(button) {
    const castItem = button.parentElement.parentElement.parentElement;
    const castIndex = Array.from(castItem.parentElement.children).indexOf(castItem);
    castMembers.splice(castIndex, 1); // Remove from the array
    castItem.remove(); // Remove from the UI
}

function editCast(button) {
    const castItem = button.parentElement.parentElement.parentElement;
    const castIndex = Array.from(castItem.parentElement.children).indexOf(castItem);

    // Retrieve the current name and image source
    const currentName = castItem.querySelector('p').textContent;
    const currentImageSrc = castItem.querySelector('img').src;

    // Populate the input fields in the popup
    document.getElementById('castName').value = currentName;
    const castImageInput = document.getElementById('castImage');
    castImageInput.value = ''; // Clear current value to trigger change event
    document.getElementById('castImagePreview').src = currentImageSrc;
    document.getElementById('castImagePreview').style.display = 'block';

    // Show the popup
    openAddCastPopup();

    // Override the add function to update the existing cast member
    document.getElementById('addCastButton').onclick = function() {
        updateCastMember(castIndex);
    };
}

function updateCastMember(index) {
    const name = document.getElementById('castName').value;
    const imgFile = document.getElementById('castImage').files[0];

    if (!name || (imgFile && !imgFile.name)) {
        alert('Please provide both a name and an image.');
        return;
    }

    // Update the cast member in the array
    castMembers[index] = { name: name, image: imgFile || castMembers[index].image };

    // Update the displayed cast member
    const castList = document.querySelector('.cast-list');
    const castItem = castList.children[index];

    // Update the name
    castItem.querySelector('p').textContent = name;

    // Update the image if a new one is uploaded
    if (imgFile) {
        const reader = new FileReader();
        reader.onload = function(e) {
            castItem.querySelector('img').src = e.target.result;
        };
        reader.readAsDataURL(imgFile);
    }

    closeAddCastPopup();
}

