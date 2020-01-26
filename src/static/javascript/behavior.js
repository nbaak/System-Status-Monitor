$(document).ready(function(){
	
	console.log("ready!!");

	// Barcolor
	$(".warning").each(function() {
		// dunno why it's the 0th element.. I don't like JS
		var current = parseInt($(this)[0].getAttribute("aria-valuenow"));
	    var max     = parseInt($(this)[0].getAttribute("aria-valuemax"));
		
		console.log(current);
		console.log(max);
		
		if (current >= 0.95 * max){
			$(this).css("background-color", "#ff0000");
		} else if ( current >= 0.75 * max) {
			$(this).css("background-color", "#ffd700");
		}else {
			$(this).css("background-color", "#007bff");
		}
	});

});

