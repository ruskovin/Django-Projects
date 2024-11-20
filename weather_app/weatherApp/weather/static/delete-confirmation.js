
var deleteButtons = document.querySelectorAll('.delete-button');
deleteButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var confirmation = confirm('Are you sure you want to delete this item?');
        if (confirmation) {
            var id = button.getAttribute('data-id');
            fetch('/delete/' + id, {
                method: 'DELETE'
            }).then(function(response) {
                window.location.reload();
            });
        }
    });
});