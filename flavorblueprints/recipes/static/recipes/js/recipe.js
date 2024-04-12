$(() => {
    const toggleUnits = () => {
        if ($('#metric').prop('checked')) {
            $('.ingredients-metric').removeClass('d-none');
            $('.ingredients-imperial').addClass('d-none');
        } else {
            $('.ingredients-metric').addClass('d-none');
            $('.ingredients-imperial').removeClass('d-none');
        }
    }

    $('#metric').on('click', toggleUnits);
    $('#imperial').on('click', toggleUnits);
})
