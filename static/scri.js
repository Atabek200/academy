document.getElementById('register-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = {
        username: formData.get('username'),
        email: formData.get('email'),
        password: formData.get('password'),
    };

    const response = await fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        alert('Registration successful!');
        event.target.reset();
    } else {
        const errorData = await response.json();
        alert('Error: ' + JSON.stringify(errorData));
    }
});
