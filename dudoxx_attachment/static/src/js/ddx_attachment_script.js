document.addEventListener('DOMContentLoaded', function () {
    // Button click listener for recalculating hash code
    const recalculateButton = document.querySelector('.ddx_attachment_btn');
    if (recalculateButton) {
        recalculateButton.addEventListener('click', () => {
            alert('Hash code recalculated!');
            // Insert logic for recalculating hash code
        });
    }
});
