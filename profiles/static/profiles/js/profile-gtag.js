(() => {
    var profileId = $('#profile-id').text() || '';
    $('a.email-btn').click(function() {
        // var emaillink = $(this).attr('href');
        gtag('event', 'contact', { 'event_category' : 'Contact', 'event_action' : 'Profile - Send Email', 'event_label' : profileId});
        return true;
    });

    $('a.webpage-btn').click(function() {
        // var pageLink =$(this).attr('href');
        gtag('event', 'contact', { 'event_category' : 'Contact', 'event_action' : 'Profile - View Webpage', 'event_label' : profileId});
        return true;
    });
})();
