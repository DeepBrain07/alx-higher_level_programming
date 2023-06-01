$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, textStatus){
/*	for (const key of Object.keys(data)){
		if (key === "title"){
			$("UL#list_movies").append($("<li></li>").text(data[key]);
		}
	}*/
	for (let i = 0; i < data["results"].length; i++){
		for (const key of Object.keys(data["results"][i])){
			if (key === "title"){
				$("UL#list_movies").append($("<li></li>").html(data["results"][i]["title"]));
			}
		}
	}
})
