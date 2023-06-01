$("DIV#toggle_header").click(function() {
	if ($("header").hasClass("red")) {
		$("header").css("color", "green");
	} 
	if ($("header").hasClass("green")) 
		$("header").css("color", "red");
})	
