let popup_alert = document.querySelector(".popup_alert")
let popup_loading = document.querySelector(".popup_loading")
export function popup_success(time,text){
    popup_alert.querySelector("div>div>p").innerHTML = text
    if (popup_alert.classList.contains("success"))
        popup_alert.classList.remove("success")
    else{
        popup_alert.classList.add("success")
        const timeoutId = setTimeout(() => {
            popup_alert.classList.remove("success")
        }, time);
    }
};
export function popup_warning(time,text){
    popup_alert.querySelector("div>div>p").innerHTML = text
    if (popup_alert.classList.contains("warning"))
        popup_alert.classList.remove("warning")
    else{
        popup_alert.classList.add("warning")
        const timeoutId = setTimeout(() => {
            popup_alert.classList.remove("warning")
        }, time);
    }
};

export function add_popup_loading(){
        popup_loading.classList.add("active");
};

export function remove_popup_loading(){
    // if (popup_loading.classList.contains("active"))
    popup_loading.classList.remove("active");
};