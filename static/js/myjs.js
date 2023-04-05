$('#id_line_one_quantity, #id_line_one_unit_price, #id_line_two_quantity, #id_line_two_unit_price, #id_line_three_quantity, #id_line_three_unit_price, #id_line_four_quantity, #id_line_four_unit_price, #id_line_five_quantity, #id_line_five_unit_price, #id_line_six_quantity, #id_line_six_unit_price, #id_line_seven_quantity, #id_line_seven_unit_price, #id_line_eight_quantity, #id_line_eight_unit_price #id_line_nine_quantity, #id_line_nine_unit_price, #id_line_ten_quantity, #id_line_ten_unit_price').keyup(function(){
  var line_one_quantity_text = $('#id_line_one_quantity').val();
  var line_one_unit_price_text = $('#id_line_one_unit_price').val();
  var line_one_total = line_one_quantity_text * line_one_unit_price_text

  var line_two_quantity_text = $('#id_line_two_quantity').val();
  var line_two_unit_price_text = $('#id_line_two_unit_price').val();
  var line_two_total = line_two_quantity_text * line_two_unit_price_text

  var line_three_quantity_text = $('#id_line_three_quantity').val();
  var line_three_unit_price_text = $('#id_line_three_unit_price').val();
  var line_three_total = line_three_quantity_text * line_three_unit_price_text
  
  var line_four_quantity_text = $('#id_line_four_quantity').val();
  var line_four_unit_price_text = $('#id_line_four_unit_price').val();
  var line_four_total = line_four_quantity_text * line_four_unit_price_text

  var line_five_quantity_text = $('#id_line_five_quantity').val();
  var line_five_unit_price_text = $('#id_line_five_unit_price').val();
  var line_five_total = line_five_quantity_text * line_five_unit_price_text

  

  var total = line_one_total + line_two_total + line_three_total + line_four_total + line_five_total

  $('#id_line_one_total_price').val(line_one_total);
  $('#id_line_two_total_price').val(line_two_total);
  $('#id_line_three_total_price').val(line_three_total);
  $('#id_line_four_total_price').val(line_four_total);
  $('#id_line_five_total_price').val(line_five_total);
  $('#id_total').val(total);
});
