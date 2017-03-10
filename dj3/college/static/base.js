$(document).ready(function() {

	$(location).attr('href');

	if (window.location.pathname.split('/')[2]) {
		var attr = '#' + window.location.pathname.split('/')[2];

		$(attr).addClass('active');
	} else {
		$('#home').addClass('active');
	}

});
