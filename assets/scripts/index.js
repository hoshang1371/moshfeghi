
import '../styles/homePage.css'
import '../styles/style.css'
import '../styles/product_detail.css'
import '../styles/logIn.css'

import '../styles/product_list.css'

import './numberOfPersian.js'
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
// const csrftoken = getCookie('csrftoken');
// console.log("csrftoken");
// console.log(csrftoken);
//!===================================================

