$(() => {
    $('#search-form').submit((e) => {
        // Prevent the form from submitting
        e.preventDefault();
        const query = $('#search-input').val();
        // Redirect with the query in the URL.
        window.location.href = `/search/${encodeURIComponent(query)}`;
    });
})
