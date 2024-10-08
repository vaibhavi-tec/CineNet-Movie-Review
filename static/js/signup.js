document.getElementById('signupform').addEventListener('submit', function(event) {
    event.preventDefault();

    // Gather form data
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;
    const profileImage = document.getElementById('profile').files[0]; // Get the selected file

    // Basic validation
    if (!email || !username || !password || !role) {
        alert('Please fill in all fields.');
        return;
    }

    // Check if a file is selected
    if (profileImage && !['image/jpeg', 'image/png'].includes(profileImage.type)) {
        alert('Please upload a valid image file (.jpg or .png).');
        return;
    }

    // Log the data to the console (for demonstration purposes)
    console.log({
        email,
        username,
        password,
        role,
        profileImage: profileImage ? profileImage.name : 'No file selected'
    });

    // Here, you would typically send this data to the server using FormData for file uploads
    const formData = new FormData();
    formData.append('email', email);
    formData.append('username', username);
    formData.append('password', password);
    formData.append('role', role);
    if (profileImage) {
        formData.append('profile', profileImage);
    }

    // Example of an AJAX request (using Fetch API)
    fetch('/signup-endpoint/', { // Update with your actual endpoint
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle success or failure based on server response
        alert('Signup successfully!');
        // Redirect if needed
        // window.location.href = 'appointment.html'; // Uncomment to redirect
    })
    .catch(error => {
        console.error('Error during signup:', error);
        alert('There was an error during signup. Please try again.');
    });
});
