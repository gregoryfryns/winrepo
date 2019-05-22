$('a.email-btn').click(function() {
    var emaillink = $(this).attr('href');
    gtag('event', 'contact', { 'event_category' : 'Contact', 'event_action' : 'Send Email', 'event_label' : emaillink});
    return true;
});

$('a.webpage-btn').click(function() {
    var pageLink =$(this).attr('href');
    gtag('event', 'contact', { 'event_category' : 'Contact', 'event_action' : 'View Webpage', 'event_label' : pageLink});
    return true;
});
