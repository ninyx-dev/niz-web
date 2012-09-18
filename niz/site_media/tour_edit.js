function tour_edit() {
	var item = $(this).parent();
	var url = item.find(".title").attr("href");
	item.load("/save/?ajax&url=" + escape(url), null, function() 
	{
		$("#save-form").submit(tour_save);
	}
	);
	return false;
};

function tour_save()
{	
	var item = $(this).parent();
	var data = {
		url:item.find("#id_url").val(),
		title:itme.find("#id_title").val(),
		tags:item.find("#id_tags").val(),
		share:item.find("#id_share").val(),
		ajax:''
	};
	
	$.post("/save/?ajax&url=sdf", data,function(result){
		if(result != 'failure')
		{
			item.before($("li", result).get(0));
			item.remove();
			$("ul.tours .edit").click(tour_edit);
		}else{
			alert("Failed to validate bookmark before saving.");
		}
	});
	return false;
}


$(document).ready(function() {
	$("ul.tours .edit").click(tour_edit);
	
	// alert( "Size: " + $("ul.tours .edit").size() );

});
