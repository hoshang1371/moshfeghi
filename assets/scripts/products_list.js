

var cateId = document.querySelector(".index-scope>input").value
var cateIdNavs = document.querySelectorAll(".menu_mobile>option")
let firstOption = document.querySelector(".menu_mobile>option")

// console.log(cateId)
cateIdNavs.forEach(cateIdNav=>{
    var allCateId = cateIdNav.getAttribute("fooData")
    if( allCateId != null )
        if(allCateId == cateId){
            firstOption.removeAttribute("selected");
            // console.log(`${allCateId} =${allCateId == cateId}`)
            // console.log(cateIdNav.parentElement) .setAttribute("step","any");
            cateIdNav.parentElement.selectedIndex = allCateId;
            cateIdNav.setAttribute("selected","selected");
        }
})

// !=============================================================
let rActiveItenNav = document.querySelectorAll(".sf-menu>li")
rActiveItenNav[0].classList.remove("active")
rActiveItenNav[1].classList.add("active")
// !=============================================================
