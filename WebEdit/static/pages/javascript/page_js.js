$(document).on('click', '.btn-danger', function(){
    return confirm('Delete this page? This action cannot be undone.');
});
$(document).on('click', '.before-run', function(){
    return confirm('Save before running?');
});