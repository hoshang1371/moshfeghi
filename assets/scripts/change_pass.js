const pass_field = document.querySelectorAll('.password');
const show_btns = document.querySelectorAll('.show');

console.log(pass_field)
console.log(show_btns)



show_btns.forEach((show_btn,i) => {
        show_btn.addEventListener('click', function () {
            if (pass_field[i].type === "password") {
                pass_field[i].type = "text";
                show_btn.style.color = "#3498db";
                show_btn.textContent = "عدم نمایش";
            } else {
                pass_field.type = "password";
                show_btn.style.color = "#222";
                show_btn.textContent = "نمایش";
            }
        })
});
// for(let i=0; i<show_btn.length; i++){
//     show_btn[i].addEventListener('click', function () {
//         if (pass_field[i].type === "password") {
//             pass_field[i].type = "text";
//             show_btn[i].style.color = "#3498db";
//             show_btn[i].textContent = "عدم نمایش";
//         } else {
//             pass_field[i].type = "password";
//             show_btn[i].style.color = "#222";
//             show_btn[i].textContent = "نمایش";
//         }
//     })
// }