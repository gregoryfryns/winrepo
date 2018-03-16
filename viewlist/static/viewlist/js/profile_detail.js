$( document ).ready(function() {
	var profileId = $('#profile-id').text(),
		resultsList,
		resultIndex;
		
	if (typeof(Storage) !== "undefined" && window.sessionStorage.getItem("resultsList"))
		resultsList = JSON.parse(window.sessionStorage.getItem("resultsList"));
	if (resultsList)
		resultIndex = resultsList.indexOf(profileId);
	
	if (resultIndex >= 0 && resultIndex < resultsList.length-1)
		$('#next-btn').removeClass('disabled').attr('href',document.location.origin + '/list/' + resultsList[resultIndex+1]);	
	if (resultIndex > 0)
		$('#previous-btn').removeClass('disabled').attr('href',document.location.origin + '/list/' + resultsList[resultIndex-1]);
		$('#page-number').text('Result ' + (resultIndex+1) + ' of ' + resultsList.length);
	
});
