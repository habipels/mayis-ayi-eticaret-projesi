
$(document).ready(function(){

    var quantitiy=0;
       $('.button-plus').click(function(e){
            
            // Stop acting like a button
            e.preventDefault();
            // Get the field name
            var quantity = parseInt($('.quantity-field').val());
            
            // If is not undefined
                
                $('.quantity-field').val(quantity + 1);
    
              
                // Increment
            
        });
    
         $('.button-minus').click(function(e){
            // Stop acting like a button
            e.preventDefault();
            // Get the field name
            var quantity = parseInt($('.quantity-field').val());
            
            // If is not undefined
          
                // Increment
                if(quantity>0){
                $('.quantity-field').val(quantity - 1);
                }
        });
        
    });

    // Giriş Butonuna Tıklandığında

    