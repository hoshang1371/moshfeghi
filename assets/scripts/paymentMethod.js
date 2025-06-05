
var rules = document.querySelector(".rules");
var ruleClose = document.querySelector(".rules i");
var ruleOpen = document.querySelector(".RuleOpen");

ruleClose.addEventListener("click", function(){
    if(rules.classList.contains("RuleShow")){
        rules.classList.add("RuleNone");
        rules.classList.remove("RuleShow");
    }
})
ruleOpen.addEventListener("click", function(){
    if(rules.classList.contains("RuleNone")){
        rules.classList.add("RuleShow");
        rules.classList.remove("RuleNone");
    }
})