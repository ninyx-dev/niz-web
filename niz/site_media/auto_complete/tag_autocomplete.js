$(document).ready(function () {
//alert($("#id_tags").size());
  $("#id_tags").autocomplete('/ajax/tag/autocomplete/', 
  {multiple: true, multipleSeparator: ' '});
});
