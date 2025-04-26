import { popup_success,popup_warning,add_popup_loading,remove_popup_loading } from './popup.js';

import { delete_OrderDetails,delete_OrderDetails_All,sendToOrderDetails,sendAllToOrderDetails } from './Network.js';

import { getCookie } from './index.js';


const csrftoken = getCookie('csrftoken');

// let numberToPersianValue = document.querySelectorAll('.ToPersianValue');
// !================================================================

let remove_items= document.querySelectorAll(".remove_item i")
remove_items.forEach((remove_item,index)=>{
    remove_item.addEventListener("click", function(){
        var delet_orderDetail_id =remove_item.parentElement.querySelector("input").value

        // console.log(remove_item.parentElement.querySelector("input").value)
        add_popup_loading();
                delete_OrderDetails(delet_orderDetail_id, csrftoken).then(data => {
                    if(data.status==204){
                        // numberToPersianValue[index].remove()
                        // console.log(numberToPersianValue[index])
                        remove_item.parentElement.parentElement.remove()
                        popup_success(3000,"محصول مورد نظر حذف شد")
                    }
                    else{
        
                        popup_warning(3000,"مشکلی بوجود امده است");
                    }
                });
                remove_popup_loading();
    })
});
// !==================================================================
let removeAll = document.querySelector(".removeAll");

removeAll.addEventListener("click",function(){
    let content_orders = document.querySelectorAll(".content_order")

    add_popup_loading();

    delete_OrderDetails_All(csrftoken).then(async data => {
        const dataEnd = await data.json();
        console.log(dataEnd)
        console.log(data.status)
        if(data.status==200){
            content_orders.forEach(content_order=>{
                content_order.remove()
            });
            popup_success(3000,"سبد خرید خالی شد.")
        }
        else{

            popup_warning(3000,"مشکلی بوجود امده است");
        }
        remove_popup_loading();
    });
})
// ! =============================================================

let numberToPersianValue = document.querySelectorAll('.ToPersianValue');

let BCups = document.querySelectorAll('.BCup');
let BCdowns = document.querySelectorAll('.BCdown');


numberToPersianValue.forEach(enter=>{
    enter.addEventListener("keypress", function(event){
        if (event.key === "Enter") {
            // Cancel the default action, if needed
            event.preventDefault();
            // Trigger the button element with a click
            // console.log(enter.parentElement.querySelector("div>input").value)
            // console.log(enter.parentElement.querySelector("div>input[type='hidden']").value)
            // console.log(enter.parentElement)
            let count = enter.parentElement.querySelector("div>input").value.toEnglishDigit()
            let id = enter.parentElement.querySelector("div>input[type='hidden']").value

            add_popup_loading();
            sendToOrderDetails(csrftoken,id,count).then(async data => {
                const dataEnd = await data.json();
                // console.log(dataEnd)
                // console.log(data.status)
                if(data.status==200){
                    // BCup.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector(".Prce>span").innerHTML=`${dataEnd.price.toString().toPersinaDigit()} &nbsp;تومان`;
    
                    document.querySelector(".totla_price").innerHTML = `${dataEnd.Total_price_for_all_product_buy.toString().toPersinaDigit()}‎ تومان`
                    document.querySelector(".total").innerHTML = `${dataEnd.Total_price_postPrice.toString().toPersinaDigit()}‎ تومان`
        
                    popup_success(3000,"به روز رسانی انجام شد.");
                    // remove_popup_loading();
                }
                else if(response.status == 201){
                    popup_warning(3000,"این تعداد کالا موجود نیست");
                }
                else{
        
                    popup_warning(3000,"مشکلی بوجود امده است");
                }
            });
            remove_popup_loading();
        }
    });
})

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

BCups.forEach((BCup,i)=>{
    BCup.addEventListener("click", function(){
        let fa_number = numberToPersianValue[i].value;
        let en_number = fa_number.toEnglishDigit();
        ++en_number;
        fa_number =en_number.toString();
        numberToPersianValue[i].value = (fa_number.toPersinaDigit());

        let id = BCup.parentElement.querySelector("input").value;
        let count = BCup.parentElement.parentElement.querySelector("input").value
        console.log(id)
        add_popup_loading();
        sendToOrderDetails(csrftoken,id,count).then(async data => {
            const dataEnd = await data.json();
            // console.log(dataEnd)
            // console.log(data.status)
            if(data.status==200){
                BCup.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector(".Prce>span").innerHTML=`${dataEnd.price.toString().toPersinaDigit()} &nbsp;تومان`;

                document.querySelector(".totla_price").innerHTML = `${dataEnd.Total_price_for_all_product_buy.toString().toPersinaDigit()}‎ تومان`
                document.querySelector(".total").innerHTML = `${dataEnd.Total_price_postPrice.toString().toPersinaDigit()}‎ تومان`
    
                popup_success(3000,"به روز رسانی انجام شد.");
                // remove_popup_loading();
            }
            else if(response.status == 201){
                popup_warning(3000,"این تعداد کالا موجود نیست");
            }
            else{
    
                popup_warning(3000,"مشکلی بوجود امده است");
            }
        });
        remove_popup_loading();
    });
})

BCdowns.forEach((BCdown,i)=>{
    BCdown.addEventListener("click", function(){
        let fa_number = numberToPersianValue[i].value;
        // console.log(fa_number)
        let en_number = fa_number.toEnglishDigit();
        if(en_number > 1)
            --en_number;
        fa_number =en_number.toString();
        numberToPersianValue[i].value = (fa_number.toPersinaDigit());
        
        let id = BCdown.parentElement.querySelector("input").value;
        let count = BCdown.parentElement.parentElement.querySelector("input").value
        console.log(id)
        add_popup_loading();
        sendToOrderDetails(csrftoken,id,count).then(async data => {
            const dataEnd = await data.json();
            // console.log(dataEnd)
            // console.log(data.status)
            if(data.status==200){
                BCdown.parentElement.parentElement.parentElement.parentElement.parentElement.querySelector(".Prce>span").innerHTML=`${dataEnd.price.toString().toPersinaDigit()} &nbsp;تومان`;

                document.querySelector(".totla_price").innerHTML = `${dataEnd.Total_price_for_all_product_buy.toString().toPersinaDigit()}‎ تومان`
                document.querySelector(".total").innerHTML = `${dataEnd.Total_price_postPrice.toString().toPersinaDigit()}‎ تومان`
    
                popup_success(3000,"به روز رسانی انجام شد.")
            }
            else if(response.status == 201){
                popup_warning(3000,"این تعداد کالا موجود نیست");
            }
            else{
    
                popup_warning(3000,"مشکلی بوجود امده است");
            }
        });
        remove_popup_loading();
        // BCdown.classList.add('active');
        // setTimeout(function(){ BCdown.classList.remove('active');}, 100);
    });
});
// !========================================================
let update = document.querySelector(".update button");
update.addEventListener("click", function(){
    // ! bayad be dakhell tabee ravad
    var sendData = []
    let numberToSend = document.querySelectorAll('.ToPersianValue');
    // console.log(numberToPersianValue)
    numberToSend.forEach(ent=>{
        // let id = ent.parentElement.querySelector("div>input[type='hidden']").value
        // console.log(ent)
        // console.log(ent.value.toString().toEnglishDigit());
        let dictionary = {};
        dictionary["id"] = ent.parentElement.querySelector("div>input[type='hidden']").value;
        dictionary["count"] = ent.value.toString().toEnglishDigit();
        // console.log(typeof(dictionary));
        // console.log(dictionary);
        sendData.push(dictionary);
        
        // console.log("===========================")
        
    })
    // console.log(sendData);
    // console.log(typeof(sendData));

    sendAllToOrderDetails(csrftoken,sendData).then(async data => {
        const dataEnd = await data.json();
        let orderDetails = dataEnd
        // console.log(dataEnd)
        // console.log(data.status)
        if(data.status == 200){
            var totalPrice = 0;
            orderDetails.forEach((orderdetail,index)=>{
                if(numberToSend[index] == undefined){
                    location.reload();
                }
                totalPrice = totalPrice + orderdetail.price
                numberToSend[index].value = orderdetail.count.toString().toPersinaDigit()
                // console.log(orderdetail.count.toString().toPersinaDigit()); 
                numberToSend[index].parentElement.parentElement.parentElement.parentElement.querySelector(".Prce>span").innerHTML=`${orderdetail.price.toString().toPersinaDigit()} &nbsp;تومان`;
                // console.log(orderdetail.price);
                // console.log(numberToPersianValue[index] == undefined);
            });
            document.querySelector(".totla_price").innerHTML = `${totalPrice.toString().toPersinaDigit()}‎ تومان`
            let sendPrice =parseInt(document.querySelector(".sendPrice").innerHTML.split(" ")[0].toEnglishDigit())
            // console.log(sendPrice+totalPrice);
            document.querySelector(".total").innerHTML = `${(sendPrice+totalPrice).toString().toPersinaDigit()}‎ تومان`
            // document.querySelector(".total").innerHTML = `${dataEnd.Total_price_postPrice.toString().toPersinaDigit()}‎ تومان`
        }
    });
})
// .update button