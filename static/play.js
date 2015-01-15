 $(document).ready(function(){
      	$(".play").click(function(){
		var whatsIn = $(".play").text()
		console.log(whatsIn)
		if (whatsIn = "&#9654;"){
	 	   $(this).replaceWith("<div class='play' id='pause'>&#9616;&#9616;<div>");
		}
		else{
	 	   $(this).replaceWith("<div class='play'>&#9654;<div>");
		}
   	});
	});
