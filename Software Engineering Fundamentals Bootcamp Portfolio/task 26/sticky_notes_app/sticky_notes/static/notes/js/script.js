document.addEventListener('DOMContentLoaded', function() {
    const noteItems = document.querySelectorAll('.note-item');  // Select all elements with the class 'note-item'
    noteItems.forEach(function(item) {
        const noteDetails = item.querySelector('.note-details');  // Select the '.note-details' element within the current 'note-item'
        const toggleButton = item.querySelector('.note-toggle');  // Select the '.note-toggle' button within the current 'note-item'

        toggleButton.addEventListener('click', function(event) {
            event.preventDefault();  // Prevent the default action (form submission)
            noteDetails.classList.toggle('active');  // Toggle the 'active' class on the '.note-details' element

            // Toggle visibility in the grid view
            const noteId = item.dataset.noteId;  // Get the note ID from the data attribute
            const gridNote = document.querySelector(`.grid-note[data-note-id="${noteId}"]`);  // Select the corresponding grid note element
            if (gridNote) {
                gridNote.style.display = noteDetails.classList.contains('active') ? 'none' : 'block';  // Toggle the display based on the 'active' class
            }
        });
    });

    // AJAX form submission for editing a note
    const editForms = document.querySelectorAll('.edit-note-form');  // Select all forms with the class 'edit-note-form'
    editForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent the default form submission
            const formData = new FormData(form);  // Create a FormData object from the form
            const noteId = form.dataset.noteId;  // Get the note ID from the data attribute
            const url = form.action;  // Get the form action URL

            fetch(url, {
                method: 'POST',
                body: formData,  // Send the form data
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),  // Include the CSRF token in the headers
                },
            })
            .then(response => response.json())  // Parse the JSON response
            .then(data => {
                if (data.success) {
                    alert('Note updated successfully!');  // Show a success message
                    document.getElementById('popupFormEdit_' + noteId).style.display = 'none';  // Hide the edit form popup
                    location.reload();  // Reload the page to reflect changes
                } else {
                    alert('Failed to update note: ' + JSON.stringify(data.errors));  // Show an error message with details
                }
            })
            .catch(error => {
                console.error('Error:', error);  // Log any errors to the console
            });
        });
    });
});
