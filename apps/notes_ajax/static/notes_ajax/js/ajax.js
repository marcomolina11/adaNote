$(document).ready(function(){

	$('.create_form').submit(function(e){
		e.preventDefault();
		$.ajax({
			url: '/users/notes',
			method: 'post',
			data: $(this).serialize(),
			success: function(serverRespose){
				console.log("Received this from server: ", serverRespose);
				$("#sortable").html(serverRespose);
				$("#sortable").serialize_and_update();
			}
		})
		$('#id_description').val('');
		$('#id_title').val('');
	})

	$(document).on('submit', '.delete_form', function(e){
		e.preventDefault();
		$.ajax({
			url: '/users/delete',
			method: 'post',
			data: $(this).serialize(),
			success: function(serverRespose){
				console.log("Deleted a Note");
				console.log("Received this from server: ", serverRespose);
				$("#sortable").html(serverRespose);
	    		$("#sortable").serialize_and_update();
			}
		})
	})

	$(document).on('submit', '.update_form', function(e){
		e.preventDefault();
		$.ajax({
			url: '/users/update_desc',
			method: 'post',
			data: $(this).serialize(),
			success: function(serverRespose){
				console.log("Updated a Note Description");
				console.log("Received this from server: ", serverRespose);
				$("#sortable").html(serverRespose);
				$("#sortable").serialize_and_update();
			}
		})
	})

	$(document).on('submit', '.title_form', function(e){
		e.preventDefault();
		$.ajax({
			url: '/users/update_title',
			method: 'post',
			data: $(this).serialize(),
			success: function(serverRespose){
				console.log("Updated a Note Title")
				console.log("Received this from server: ", serverRespose);
				$("#sortable").html(serverRespose);
				$("#sortable").serialize_and_update();
			}
		})
	})

	var descriptiontext = '';
	var titletext = '';

	$(document).on('click', '.desc', function() {
		descriptiontext = $(this).text();
    	var input = $("<textarea>", { val: $(this).text(), name: "description", class: "description_textarea", maxlength: "200"});
    	$(this).replaceWith(input);
    	input.select();
	});

	$(document).on('focusout', '.description_textarea', function(){
		var p = $("<p>", { text: descriptiontext, class: 'desc' });
    	$(this).replaceWith(p);
	});

	$(document).on('keypress', '.description_textarea', function(e){
		if (e.which == 13) {
			descriptiontext = $(this).val();
			$(this).submit();
			$(this).blur();
			return false;    //<---- Add this line
		}
	});

	$(document).on('click', '.notetitle', function() {
		titletext = $(this).text();
    	var input = $("<input>", { val: $(this).text(), type: "text", name: "title", class: "title_input", maxlength: "15" });
    	$(this).replaceWith(input);
    	input.select();
	});

	$(document).on('focusout', '.title_input', function(){
		var h = $("<h3>", { text: titletext, class: 'notetitle' });
    	$(this).replaceWith(h);
	});

	$(document).on('keypress', '.title_input', function(e){
		if (e.which == 13) {
		titletext = $(this).val();
		$(this).submit();
		$(this).blur();
		return false;    //<---- Add this line
		}
	});
	// FEATURE: Any keydown opens form 
	// $(document).keydown(function(e){
	// 	if (e.which == 65) {
	// 		if ($('.form_div').css('top') == '10px') {
	// 			return false;
	// 		}
	// 		else{
	// 			$('#plus-icon').hide(200);
	// 			$('.form_div').animate({
	// 	 		top: '10px'
	// 			}, 400);
	// 			$('.notes-wrapper').animate({
	// 			top: '410px'
	// 			}, 400);
	// 			$('#id_title').select();
	// 		}
	// 	}
	// });

	$(document).on('click', '#plus-icon', function() {
		if ($('.form_div').css('top') == '0px') {
			return false;
		}
		else{
			$(this).hide(200);
			$('.form_div').animate({
		 		top: '10px'
			}, 375);
			$('.notes-wrapper').animate({
				top: '410px'
			}, 375);
		}

	});

	$('#minus-icon').click(function(){
		$('.form_div').animate({
			top: '-379px'
		}, 375);
		$('.notes-wrapper').animate({
			top: '100px'
		}, 375);

		$('#plus-icon').show(400);
	});

	$('#menu-icon').click(function(){
		$('.menu_div').animate({
			right: '0px'
		}, 375);
	});

	$('#close-menu-icon').click(function(){
		$('.menu_div').animate({
			right: '-400px'
		}, 375);
	});

	$.fn.complete_sortable = function(){
		this.sortable({
	    	update: function(event, ui){
        		var serial = $(this).sortable('serialize');
        		console.log(serial);
       		
    			$.ajax({
     				url: "/users/update_order",
     				type: "post",
      				data: serial,
      			});
      		},
   		 });
		this.disableSelection();
	};

	$.fn.serialize_and_update = function(){
		var serial = this.sortable('serialize');
		console.log(serial);
		$.ajax({
     		url: "/users/update_order",
     		type: "post",
      		data: serial,
   		});
	};

	//Make notes sortable on page load
	$("#sortable").complete_sortable();
	//Serialize all notes and update db on page load
	$("#sortable").serialize_and_update();
})