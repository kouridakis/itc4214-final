$(() => {
    const inputFields = $('#target-form input');
    inputFields.prop('disabled', true);

    const enableForm = (bool) => {
        inputFields.prop('disabled', !bool);
        $('#cancel-button').prop('hidden', !bool);
        $('#save-button').prop('hidden', !bool);
        $('#edit-button').prop('hidden', bool);
    }

    $('#edit-button').on('click', () => {
        enableForm(true);
    });

    $('#cancel-button').on('click', () => {
        enableForm(false);
    });
})
