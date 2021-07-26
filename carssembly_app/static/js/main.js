$(document).ready(function () {
	$('#down_profile').click(function () {
		$('#up_profile').show();
		$('#profiles').show();
		$('#logout').show();
		$(this).hide();
	});
	$('#up_profile').click(function () {
		$('#down_profile').show();
		$('#profiles').hide();
		$('#logout').hide();
		$(this).hide();
	});
});
