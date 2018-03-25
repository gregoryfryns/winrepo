$( document ).ready(function() {
	var profileId = $('#profile-id').text(),
		resultsList,
		resultIndex;
		
	if (typeof(Storage) !== "undefined" && window.sessionStorage.getItem("resultsList"))
		resultsList = JSON.parse(window.sessionStorage.getItem("resultsList"));
	if (resultsList)
		resultIndex = resultsList.indexOf(profileId);
	
	if (resultIndex >= 0 && resultIndex < resultsList.length-1)
		$('#next-btn').attr('href',document.location.origin + '/list/' + resultsList[resultIndex+1]).parent().removeClass('disabled');
	if (resultIndex > 0)
		$('#previous-btn').attr('href',document.location.origin + '/list/' + resultsList[resultIndex-1]).parent().removeClass('disabled');
	
	$('#page-number').text('Result ' + (resultIndex+1) + ' of ' + resultsList.length);
	
	if (resultIndex < 0)
		$('#filtered-list-navigation').hide();

});
