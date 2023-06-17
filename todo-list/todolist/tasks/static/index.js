const checkboxes = document.querySelectorAll('input[type=checkbox]');
const texts = document.querySelectorAll('h5');

// Add event listener to each checkbox
for (let i = 0; i < checkboxes.length; i++) {
    let checkbox = checkboxes[i];
    let text = texts[i];

    checkbox.addEventListener('change', function() {
        // If checkbox is checked, add strikethrough style to text
        if (this.checked) {
            text.classList.add('text-decoration-line-through')
        } else { // Otherwise, remove the strikethrough style from text 
            text.classList.remove("text-decoration-line-through");
        }
    });
}