
import '../styles/homePage.css'
import '../styles/style.css'
import '../styles/product_detail.css'
import '../styles/logIn.css'

import './numberOfPersian.js'
// import * as css from "../styles/homePage.css";
// import '../scripts/homePage'
console.log("gol")

// !==============================
let numberToPersianValue = document.querySelectorAll('.ToPersianValue');

let BCup = document.querySelector('.BCup');
let BCdown = document.querySelector('.BCdown');

for (let val of numberToPersianValue) { // You can use `let` instead of `const` if you like
    let en_numberPer = val.value;
    val.value = en_numberPer.toPersinaDigit();
    let en_number = "";
    val.addEventListener('keyup', function (k) {


        if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
            en_number = val.value;
            var number_buffer;
            let number = en_number.toEnglishDigit();
            number_buffer = parseInt(number, 10);
            number = number_buffer.toString();
            if (isNaN(number))
                number = "0";
            val.value = (number.toPersinaDigit());
        }
        else {
            val.value = (en_number.toPersinaDigit());
        }
    });
}



BCup.addEventListener("click", function(){
    let fa_number = numberToPersianValue[0].value;
    let en_number = fa_number.toEnglishDigit();
    ++en_number;
    fa_number =en_number.toString();
    numberToPersianValue[0].value = (fa_number.toPersinaDigit());

    BCup.classList.add('active');
    setTimeout(function(){ BCup.classList.remove('active');}, 100);
});

BCdown.addEventListener("click", function(){
    let fa_number = numberToPersianValue[0].value;
    console.log(fa_number)
    let en_number = fa_number.toEnglishDigit();
    if(en_number > 1)
        --en_number;
    fa_number =en_number.toString();
    numberToPersianValue[0].value = (fa_number.toPersinaDigit());
    
    BCdown.classList.add('active');
    setTimeout(function(){ BCdown.classList.remove('active');}, 100);
});

// ! ========================================
