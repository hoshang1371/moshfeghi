var clickTable = document.querySelector(".continue");
var bill =document.querySelector(".bill");
clickTable.addEventListener("click",function(){
        if(bill.classList.contains("table_None")){
            bill.classList.add("table_Block");
            bill.classList.remove("table_None");
        }
        else if(bill.classList.contains("table_Block")){
            bill.classList.add("table_None");
            bill.classList.remove("table_Block");
        }
})