/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./assets/scripts/paymentMethod.js":
/*!*****************************************!*\
  !*** ./assets/scripts/paymentMethod.js ***!
  \*****************************************/
/***/ (() => {

eval("var rules = document.querySelector(\".rules\");\nvar ruleClose = document.querySelector(\".rules i\");\nvar ruleOpen = document.querySelector(\".RuleOpen\");\nruleClose.addEventListener(\"click\", function () {\n  if (rules.classList.contains(\"RuleShow\")) {\n    rules.classList.add(\"RuleNone\");\n    rules.classList.remove(\"RuleShow\");\n  }\n});\nruleOpen.addEventListener(\"click\", function () {\n  if (rules.classList.contains(\"RuleNone\")) {\n    rules.classList.add(\"RuleShow\");\n    rules.classList.remove(\"RuleNone\");\n  }\n});\n\n//# sourceURL=webpack://moshfeghi/./assets/scripts/paymentMethod.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/paymentMethod.js"]();
/******/ 	
/******/ })()
;