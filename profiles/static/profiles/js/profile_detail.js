$( document ).ready(function() {
	var profileId = $('#profile-id').text(),
		resultsList,
		resultIndex;
		
	if (typeof(Storage) !== "undefined" && window.sessionStorage.getItem("resultsList"))
		resultsList = JSON.parse(window.sessionStorage.getItem("resultsList"));
	if (resultsList)
		resultIndex = resultsList.indexOf(profileId);
	
	if (resultIndex >= 0 && resultIndex < resultsList.length-1)
		$('#next-btn').attr('href',document.location.origin + '/list/' + resultsList[resultIndex+1]).removeClass('disabled');
	if (resultIndex > 0)
		$('#previous-btn').attr('href',document.location.origin + '/list/' + resultsList[resultIndex-1]).removeClass('disabled');
	
	$('#current-result').text(resultIndex+1);
	$('#total-results').text(resultsList.length);
	
	if (resultIndex < 0)
		$('#filtered-list-navigation').hide();
	else
		$('#filtered-list-navigation').show();

});
