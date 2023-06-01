document.addEventListener('DOMContentLoaded', function(){
	$.get("https://hellosalut.stefanbohacek.dev/?lang=f", function(data, textStatus){
		$("DIV#hello").html(data["hello"]);
	})
})
