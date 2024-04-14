$(() => {
    $('#search-form').submit((e) => {
        // Prevent the form from submitting
        e.preventDefault();
        // Format the string as expected by the serverside view.
        const query = $('#search-input').val().replace(/ /g, '+');
        // Redirect with the query in the URL.
        window.location.href = `/search/${encodeURIComponent(query)}`;
    });
})
