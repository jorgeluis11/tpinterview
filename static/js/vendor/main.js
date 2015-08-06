// $(function() {
//     $( "#slider-range" ).slider({
//       range: true,
//       min: 0,
//       max: 1000,
//       values: [ 75, 1000 ],
//       slide: function( event, ui ) {
//         $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
//       }
//     });
//     $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
//       " - $" + $( "#slider-range" ).slider( "values", 1 ) );
//   });
$(document).ready(function(){

  $('#advance-filters-button').click(function(){
    $('#advance-filters-content').slideDown().removeClass('hide');
    $(this).slideUp();
  })

  $(".list-navbar").click(function(){
    $(this).parents(".wines-box").find(".list-navbar").removeClass("active");
    $(this).addClass("active");

    var content = $(this).data("content");
    
    switch(content){
      case "description":
        $(this).parents(".wines-box").find(".list-description-content").show();
        $(this).parents(".wines-box").find(".list-information-content").hide();
        break;
      case "list":
        $(this).parents(".wines-box").find(".list-description-content").hide();
        $(this).parents(".wines-box").find(".list-information-content").show();
        break;
    }
  })
})