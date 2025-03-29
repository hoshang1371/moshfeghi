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

/***/ "./assets/scripts/products_list.js":
/*!*****************************************!*\
  !*** ./assets/scripts/products_list.js ***!
  \*****************************************/
/***/ (() => {

eval("var cateId = document.querySelector(\".index-scope>input\").value;\nvar cateIdNavs = document.querySelectorAll(\".menu_mobile>option\");\nlet firstOption = document.querySelector(\".menu_mobile>option\");\n\n// console.log(cateId)\ncateIdNavs.forEach(cateIdNav => {\n  var allCateId = cateIdNav.getAttribute(\"fooData\");\n  if (allCateId != null) if (allCateId == cateId) {\n    firstOption.removeAttribute(\"selected\");\n    // console.log(`${allCateId} =${allCateId == cateId}`)\n    // console.log(cateIdNav.parentElement) .setAttribute(\"step\",\"any\");\n    cateIdNav.parentElement.selectedIndex = allCateId;\n    cateIdNav.setAttribute(\"selected\", \"selected\");\n  }\n});\n\n// !=============================================================\nlet rActiveItenNav = document.querySelectorAll(\".sf-menu>li\");\nrActiveItenNav[0].classList.remove(\"active\");\nrActiveItenNav[1].classList.add(\"active\");\n// !=============================================================\n\n//# sourceURL=webpack://moshfeghi/./assets/scripts/products_list.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/products_list.js"]();
/******/ 	
/******/ })()
;