var applyFilter = function() {
	var val = '^(?=.*\\b' + $.trim($('#search').val()).split(/\s+/).join(')(?=.*\\b') + ').*$',
	  underRepOnly = $('#underrepresented-countries').prop("checked"),
		$tr,
		text;

	try {
		reg = RegExp(val, 'i');

		$('#results-table tr:gt(0)').show().filter(function(index) {
			text = "";
			$tr = $(this);
			// concatenate all searchable fields into text variable
			$tr.find('.searchable').each(function(){
               text += " " + $.trim($(this).text());
            });
			return (underRepOnly && !$tr.find('td.under-represented').length) || !reg.test(text);
		}).hide();

		$('#search-container').removeClass('has-error');
		$('#search-message').text( $('#results-table tr:gt(0):visible').length + ' entries found');
	}
	catch (e) {
		$('#search-message').text('Error - please enter a valid string - ' + val);
		$('#search-container').addClass('has-error');
	}
}

$('#search').keyup($.debounce(400, applyFilter));
$('#underrepresented-countries').change(applyFilter);

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