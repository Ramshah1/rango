/**
 * Created with PyCharm.
 * User: ramshahjahangir
 * Date: 8/25/15
 * Time: 3:18 PM
 * To change this template use File | Settings | File Templates.
 */
console.log("hello");
$('#likes').click(function(){
    //alert("You reached rango-ajax file 0");
   var catid;
   catid= $(this).attr("data-catid");
   $.get('/rango/like_category/' ,{category_id : catid}, function(data){
        //alert("You reached rango-ajax file 1");
        $('#like_count').html(data);
        $('#likes').hide();

    });
});

$('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get('/rango/suggest_category/', {suggestion:query}, function(data){
        $('#cats').html(data);
    });
});





