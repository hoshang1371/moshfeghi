
import '../styles/homePage.css'
import '../styles/style.css'
import '../styles/product_detail.css'
import '../styles/logIn.css'

import '../styles/product_list.css'

import './numberOfPersian.js'
import { popup_success,popup_warning } from './popup.js';

import { delete_OrderDetails } from './Network.js';
const csrftoken = getCookie('csrftoken');
// import './homePage.js'

// import * as css from "../styles/homePage.css";
// import '../scripts/homePage'

//! get csrf token =======================================
// const csrftoken11 = getCookie('csrftoken');
export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
//!===================================================
var cateNavs= document.querySelectorAll(".sub-menu>li>.right>a");
var cateNavlefts= document.querySelectorAll(".sub-menu>li>.left");
cateNavs.forEach(cateNav=>{
    cateNav.addEventListener("mouseover", function(){
        var cateId = cateNav.querySelector("input").value
        cateNavlefts.forEach(cateNavleft=>{
            var cateNavleftsId = cateNavleft.querySelector("input").value
            if(cateId == cateNavleftsId){
                cateNavleft.style.display = 'grid';
            }
            else{
                cateNavleft.style.display = 'none';
            }
        })
    });
});
//!===================================================
var header_cart= document.querySelector(".header_cart>a");
var popup_order= document.querySelector(".popup_order");
var popup_order_right= document.querySelector(".popup_order_right");
var popup_order_close= document.querySelector(".popup_order_left_top>i");
header_cart.addEventListener("click", function(e){
    e.stopPropagation()
    popup_order.classList.remove("popup_order_none")
    popup_order.classList.add("popup_order_block")
}, false);
popup_order_right.addEventListener("click", function(e){
    e.stopPropagation()
    popup_order.classList.remove("popup_order_block")
    popup_order.classList.add("popup_order_none")  
}, false);

popup_order_close.addEventListener("click", function(e){
    e.stopPropagation()
    popup_order.classList.remove("popup_order_block")
    popup_order.classList.add("popup_order_none")  
}, false);

//!===================================================

var product_order_comps_delete = document.querySelectorAll(".product_order_comp>div>i")
product_order_comps_delete.forEach(product_order_comp=>{
    product_order_comp.addEventListener("click", function(){
        var delet_orderDetail_id =product_order_comp.parentElement.querySelector("input").value
        // console.log(product_order_comp.parentElement.parentElement.remove())

        delete_OrderDetails(delet_orderDetail_id, csrftoken).then(data => {
            if(data.status==204){
                product_order_comp.parentElement.parentElement.remove()
                popup_success(3000,"محصول مورد نظر حذف شد")
            }
            else{

                popup_warning(3000,"مشکلی بوجود امده است");
            }
        });
    });
})
