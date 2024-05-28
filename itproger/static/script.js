document.getElementById('wizard-form').addEventListener('submit', function(event) {
    event.preventDefault();
    document.getElementById('step-3').style.display = 'none';
    document.getElementById('success-message').style.display = 'block';
});

function nextStep(step) {
    var steps = document.getElementsByClassName('step');
    for (var i = 0; i < steps.length; i++) {
        steps[i].style.display = 'none';
    }
    document.getElementById('step-' + step).style.display = 'block';

    if (step === 3) {
        document.getElementById('review-name').innerText = document.getElementById('name').value;
        document.getElementById('review-email').innerText = document.getElementById('email').value;
    }
}
