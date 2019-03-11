// Filter list
var applyFilter = function() {
	var val = '^(?=.*\\b' + $.trim($('#search').val()).split(/\s+/).join(')(?=.*\\b') + ').*$',
		underRepOnly = $('#underrepresented-only').prop("checked"),
		seniorOnly = $('#senior-only').prop("checked"),
		resultsList = [],
		$tr,
		text;

	try {
		reg = RegExp(val, 'i');

		$('#results-table div.table-entry').show().filter(function() {
			$tr = $(this);
			// concatenate all searchable fields into a single string
			text = $tr.find('.searchable').toArray().map(el => el.textContent.trim()).join(' ');

			if ((underRepOnly && !$tr.find('.under-represented').length)
					|| (seniorOnly && !$tr.find('.senior').length)
					|| !reg.test(text)) {
				return true; // row will be hidden
			}
			else {
				resultsList.push($tr.find('.profile_id:eq(0)').text());
				return false;
			}
		}).hide();

		$('input#search').removeClass('is-invalid');
		$('#search-message').removeClass('text-danger')
			.html('<span class="text-secondary font-weight-bold">' + $('#results-table div.table-entry:visible').length + '</span> entries found');
	}
	catch (e) {
		$('input#search').addClass('is-invalid');
		$('#search-message').addClass('text-danger')
							.text('Please enter a valid string');
	}
	if (typeof(Storage) !== "undefined") {
		window.sessionStorage.setItem("resultsList", JSON.stringify(resultsList));
		window.sessionStorage.setItem("searchTerms", ($('#search').val()));
	}
}

// $('#search').keyup($.debounce(400, applyFilter));
// $('#underrepresented-countries').change(applyFilter);
// $('#senior-only').change(applyFilter);

$( document ).ready(function() {
	if (typeof(Storage) !== "undefined" && window.sessionStorage.getItem("searchTerms")) {
		$('#search').val(window.sessionStorage.getItem("searchTerms"));
	}
	// applyFilter();
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
