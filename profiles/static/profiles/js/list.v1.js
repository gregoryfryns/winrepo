$(document).ready(function() {
    // Trigger search when checking/unchecking boxes in form
    $('#underrepresented-only, #senior-only').change(function() {
        $('#search-btn').click();
    });

    // Back to top button
    if ($('#back-to-top').length) {
        var scrollTrigger = 600, // px
            backToTop = function () {
                var scrollTop = $(window).scrollTop();
                if (scrollTop > scrollTrigger) {
                    $('#back-to-top').addClass('show');
                } else {
                    $('#back-to-top').removeClass('show');
                }
            };
        backToTop();
        $(window).on('scroll', function () {
            backToTop();
        });
        $('#back-to-top').on('click', function (e) {
            e.preventDefault();
            $('html,body').animate({
                scrollTop: 0
            }, 700);
        });
    }

    // infinite scroll
    // from https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html
    var infinite = new Waypoint.Infinite({
        element: $('.infinite-container')[0],
        onBeforePageLoad: function () {
        $('.loading').show();
        },
        onAfterPageLoad: function ($items) {
        $('.loading').hide();
        },
        offset: 150
    });
});

