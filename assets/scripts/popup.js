let popup_alert = document.querySelector(".popup_alert")
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