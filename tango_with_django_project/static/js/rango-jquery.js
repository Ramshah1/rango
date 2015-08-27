$(document).ready(function(){

    $("#about-btn").addClass('btn btn-primary').click(function(event){
        alert("You clicked the button using JQuery!!!!!!");
        msgstr = $("#msg").html()
        msgstr = msgstr+ "o"
        $("#msg").html(msgstr)
    });

    $("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'black');
    });


});

//$("#likes").click(function(){
//    alert("You reached rango-ajax file 0");
//   var catid;
//   catid= $(this).attr("data-catid");
//   $.get('/rango/like_category/' ,{category_id : catid}, function(data){
//        alert("You reached rango-ajax file 1");
//        $('#like_count').html(data);
//        $('#likes').hide();
//
//    });
//});