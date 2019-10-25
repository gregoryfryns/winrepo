(function() {
    $('#download-slide').click(function() {
        var link = $(this).attr('href');
        gtag('event', 'resources', { 'event_category' : 'Resources', 'event_action' : 'Home - Download Slide', 'event_label' : link});
        return true;
    });
})();