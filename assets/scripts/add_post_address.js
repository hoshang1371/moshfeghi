import { popup_success,popup_warning,add_popup_loading,remove_popup_loading } from './popup.js';

import { sendSmsForVarify } from './Network.js';

import { getCookie } from './index.js';


const csrftoken = getCookie('csrftoken');


var buttonEdite = document.querySelector(".buttonEdite span");
var display = document.querySelector(".buttonEdite p");

// console.log(display);
function startTimer(duration, display) {
    display.style.display = "block";
    var timer = duration, minutes, seconds;
    // buttonEdite.setAttribute('disabled', "");
    let myVar =  setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = minutes.toPersinaDigit() + ":" + seconds.toString().toPersinaDigit();
        if (--timer < 0) {
            timer = duration;
            clearInterval(myVar);
            // buttonEdite.removeAttribute('disabled');
            display.style.display = "none";
            buttonEdite.style.opacity = '1';
            buttonEdite.innerText  = 'ارسال کد تایید';
            buttonEdite.style.cursor = 'pointer';
            // buttonEdite.classList.add('varifyMobileHover');
            // timerCountDown.classList.remove('countdownTimerDisplayFlex');
            // timerCountDown.classList.add('countdownTimerDisplayNone');
            buttonEdite.addEventListener('click',send_codeFunctionClick);
        }
    }, 1000);
}

// startTimer(120, display);

buttonEdite.addEventListener('click',send_codeFunctionClick);

function send_codeFunctionClick(){
    var mobNumber = document.querySelector('.mobNumber');
    console.log(mobNumber.value);
    console.log(buttonEdite);
        sendSmsForVarify(csrftoken,mobNumber.value).then(async (data) => {
        console.log('data.status=',data.status);
        console.log('data.body',data.body); 
        const dataEnd = await data.json();
        // console.log(data.json());
        console.log(dataEnd);
        // console.log(data.json().Object);
        // console.log(dataEnd.mobNum);
        // if(data.mobNum == 'ok'){
        //     console.log('kos nant') 
        // }
        if((data.status == 200)){
            console.log("it's ok");
            // timerCountDown.classList.remove('countdownTimerDisplayNone');
            // send_code.classList.remove('varifyMobileHover');
            // timerCountDown.classList.add('countdownTimerDisplayFlex');

            // buttonEdite.setAttribute('disabled', "");

            startTimer(60*2, display);

            buttonEdite.style.opacity = '0.5';
            buttonEdite.innerText="کد تایید ارسال شد";
            buttonEdite.style.cursor = 'auto';
            buttonEdite.removeEventListener("click", send_codeFunctionClick);
        }
        // else if(dataEnd.mobNum == 'not ok'){
        else if((data.status == 201)){
            alert("شماره موبایل خود را وارد کنید");
        }

    });

};