$(() => {
    // Add Bootstrap classes to all form elements

    $('label').each((_, label) => {
        $(label).addClass('form-label pt-3');
    });

    $('input').each((_, input) => {
        $(input).addClass('form-control m-0');
    });

    $('.errorlist').each((_, errorlist) => {
        $(errorlist).addClass('form-text text-danger m-0 p-0 ps-4');
        // Moving any errorlists BEFORE moving helptexts is important,
        // as otherwise the helptext will end up under the errorlist.
        $(errorlist).insertAfter($(errorlist).next());
    });

    $('.helptext').each((_, helptext) => {
        $(helptext).addClass('form-text fst-italic m-0 p-0 ps-1');
        // Move supporting text to be under each input.
        $(helptext).insertAfter($(helptext).next());
    });
})
