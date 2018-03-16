// Filter list
var applyFilter = function() {
	var val = '^(?=.*\\b' + $.trim($('#search').val()).split(/\s+/).join(')(?=.*\\b') + ').*$',
	  underRepOnly = $('#underrepresented-countries').prop("checked"),
		resultsList = [],
		$tr,
		text;

	try {
		reg = RegExp(val, 'i');

		$('#results-table tr:gt(0)').show().filter(function(index) {
			// text = "";
			$tr = $(this);
			// concatenate all searchable fields into a single string
			text = $tr.find('.searchable').toArray().map(el => el.textContent.trim()).join(' ');

			if ((underRepOnly && !$tr.find('.under-represented').length) || !reg.test(text))
				return true;
			else
				resultsList.push($tr.find('.profile_id:eq(0)').text());
				return false;
		}).hide();

		$('#search-container').removeClass('has-error');
		$('#search-message').text( $('#results-table tr:gt(0):visible').length + ' entries found');
	}
	catch (e) {
		$('#search-message').text('Error - please enter a valid string');
		$('#search-container').addClass('has-error');
	}
	if (typeof(Storage) !== "undefined")
		window.sessionStorage.setItem("resultsList", JSON.stringify(resultsList));

}

$('#search').keyup($.debounce(400, applyFilter));
$('#underrepresented-countries').change(applyFilter);
$( document ).ready(function() {
	applyFilter();
	//other stuff?
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
