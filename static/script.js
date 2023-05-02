$(document).ready(function () {
    $('form').submit(function (event) {
        event.preventDefault();
        // Get input question from form
        var question = $('#question').val();

        // Extract option values from form data using name attribute
        var options = $('input[name="choice[]"]:checked').map(function () {
            return $(this).val();
        }).get();

        // Generate new prompt for the question
        var data = {
            "question": question,
            "options": options
        };

        // Make API request to Flask server with the prompt
        $.ajax({
            type: 'POST',
            url: '/',
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: 'json',
            success: function (data) {
                // Update answer section with API response
                $('#answer').text(data.answer);
            },
            error: function () {
                // Handle error case
                alert('Error generating answer.');
            },
        });
    });
});
