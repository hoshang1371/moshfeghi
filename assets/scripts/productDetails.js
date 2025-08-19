import { getCookie } from './index.js';
import { delete_comment,add_comment,liked_comment } from './Network.js';
import { popup_success,popup_warning } from './popup.js';


const csrftoken = getCookie('csrftoken');
// console.log(csrftoken)
let product_id = document.querySelector('.product-scope>input');
// !==============================
let notAuth = document.querySelector('.notAuth')
if(notAuth != null){
    notAuth.addEventListener('click',function(){
        popup_warning(3000,"لطفاً وارد شوید");
    })
}
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
    // console.log(fa_number)
    let en_number = fa_number.toEnglishDigit();
    if(en_number > 1)
        --en_number;
    fa_number =en_number.toString();
    numberToPersianValue[0].value = (fa_number.toPersinaDigit());
    
    BCdown.classList.add('active');
    setTimeout(function(){ BCdown.classList.remove('active');}, 100);
});


//!==================================================
let answers = document.querySelectorAll(".answer")
let removeComments = document.querySelectorAll(".removeComment")
//!=======================comment===========================

removeComments.forEach(removeComment=>{
    removeComment.addEventListener("click", function(){ 
        // console.log()
        let id = removeComment.parentElement.querySelector("input").value
        // console.log(csrftoken)
        // 
        // const apiUrl = 'http://127.0.0.1:8000/products/api/DeleteCustomerComment/10/';

        
        delete_comment(id, csrftoken).then(data => {
            if(data.status==204){
                removeComment.parentElement.parentElement.parentElement.remove()
                popup_success(3000,"نظر شما حذف شد")
            }
            else{
                popup_warning(3000,"مشکلی بوجود امده است");
            }
        });

    });
})

answers.forEach(answer=>{
    answer.addEventListener("click", function(){ 
        // let id = removeComment.parentElement.querySelector("input").value add_comment
        let answer_Post = answer.parentElement.parentElement.parentElement.querySelector(".add-comment-section")
        if(answer_Post.textContent.trim() === ''){
            answer_Post.innerHTML='<input  type="text" class="form-control me-3 border-bottom" placeholder="افزودن نظر"> <button class="btn btn-primary me-3" type="button">ارسال</button>';
            answer_Post.querySelector("button").addEventListener("click",function(){

                console.log(product_id.value)
                let text =answer_Post.querySelector("input").value
                let parent = answer.parentElement.querySelector("input").value
                
                add_comment(csrftoken,product_id.value,text,parent).then(data => {
                    // console.log(data.status)
                    if(data.status == 200){
                        popup_success(3000,"نظر شما پس از تایید ثبت می شود");
                    }
                    else{
                        popup_warning(3000,"مشکلی بوجود امده است");
                    }
                });

            });
        }
        else
            answer_Post.innerHTML= ""
    });
})

let as_Comment = document.querySelector(".add-comment-section_asli")
as_Comment.querySelector("button").addEventListener("click",function(){
    let text = as_Comment.querySelector("input").value
    add_comment(csrftoken,product_id.value,text,parent=null).then(data => {
        // console.log(data.status)
        if(data.status == 200){
            popup_success(3000,"نظر شما پس از تایید ثبت می شود");
        }
        else{
            popup_warning(3000,"مشکلی بوجود امده است");
        }
    });
})

//!=========================likeComment===================

let likeComments = document.querySelectorAll(".voting-icons>.svgAuth  ")
// console.log(likeComments)
likeComments.forEach(likeComment=>{
    likeComment.addEventListener("click",function(){
    
        // console.log(likeComment.parentElement.querySelector("input").value)
        let comment_id = likeComment.parentElement.querySelector("input").value
        let likeds= likeComment.parentElement.querySelectorAll("svg")
        likeds.forEach(liked=>{
            let numberLike= likeComment.parentElement.querySelector(".numberLike")
            // console.log('numberLike',numberLike)
            if(liked.classList.contains("activeSvg")){
                liked_comment(csrftoken,comment_id).then(async data =>{
                    const dataEnd = await data.json();
                    console.log(dataEnd)
                    numberLike.innerHTML = dataEnd.numberLike
                });
                liked.classList.add("deactiveSvg")
                liked.classList.remove("activeSvg")
            }
            else if(liked.classList.contains("deactiveSvg")){
                // liked_comment(csrftoken,comment_id).then(async data =>{
                //     const dataEnd = await data.json();
                //     console.log(dataEnd)
                //     numberLike.innerHTML = dataEnd.numberLike
                // });
                liked.classList.add("activeSvg")
                liked.classList.remove("deactiveSvg")
            }
        });
    })
    //!
    // let svgIcon = likeComment.querySelector("svg")
    // svgIcon.addEventListener("click",function(){
    //     console.log(svgIcon)
    // });
})
//!=======================================================
