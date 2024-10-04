document.getElementById('signupform').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    // Basic validation (optional, you can customize this)
    if (!email ||!username || !password || !role) {
        alert('Please fill in all fields.');
        return;
    }

    // Normally, you would send this data to the server with an AJAX request or similar
    // Here, we'll just log it to the console
    console.log({
        email,
        username,
        password,
        role
    });

    // Show success message or redirect
    alert('Signup successfully!');
    // window.location.href = 'appointment.html'; // Uncomment to redirect
});
