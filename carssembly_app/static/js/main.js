$(document).ready(function () {
	$('#down_profile').click(function () {
		$('#drop_menu').slideToggle(1000);
		$(this).hide();
		$('#up_profile').show();
	});
	$('#up_profile').click(function () {
		$('#drop_menu').slideUp();
		$(this).hide();
		$('#down_profile').show();
	});
});
