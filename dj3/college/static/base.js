$(document).ready(function() {
	$("input,textarea").removeClass("form-control").addClass("form-control");
	$("input:checkbox").removeClass("form-control");
	$(location).attr("href");

	if (window.location.pathname.split('/')[2] + "") {
		var attr = "#" + window.location.pathname.split('/')[2];

		$(attr).addClass('active');
	} else {
		$("#home").addClass("active");
	}

});