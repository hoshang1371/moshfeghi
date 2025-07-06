import { popup_success,popup_warning,add_popup_loading,remove_popup_loading } from './popup.js';

import { delete_listOfPostAddress } from './Network.js';

import { getCookie } from './index.js';


const csrftoken = getCookie('csrftoken');

var EditePostAll = document.querySelectorAll(".EditePost");

EditePostAll.forEach(EditePost=>{
    EditePost.addEventListener("click",function(){
        // console.log(EditePost.previousElementSibling.value);
        // console.log(window.location.href);
        window.location.href = `/post_info/edit_post_add_address_account/${EditePost.previousElementSibling.value}`
        
    });
});

var DeletePostAdressAll = document.querySelectorAll(".DeletePostAdress");

DeletePostAdressAll.forEach(DeletePostAdress=>{
    DeletePostAdress.addEventListener("click",function(){
        var id = DeletePostAdress.parentElement.querySelector("input").value
        // console.log(id)
        add_popup_loading();
        delete_listOfPostAddress(id, csrftoken).then(data => {
            // console.log("it's ok");
            // console.log(data.status);
            if (data.status == 204) {
                DeletePostAdress.parentElement.parentElement.parentElement.remove()
                popup_success(3000,"آدرس مورد نظر حذف شد")
            }
            else{
        
                popup_warning(3000,"مشکلی بوجود امده است");
            }
        });
        remove_popup_loading();
        // console.log(DeletePostAdress.parentElement.parentElement.parentElement.remove())
    });
});

var buttonEdite = document.querySelector(".buttonEdite");

buttonEdite.addEventListener("click",function(){
    console.log(window.location.hostname); 
    window.location.href = '/post_info/post_add_address'
});
