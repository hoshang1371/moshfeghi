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

/***/ "./assets/scripts/cartToCartPeyment.js":
/*!*********************************************!*\
  !*** ./assets/scripts/cartToCartPeyment.js ***!
  \*********************************************/
/***/ (() => {

eval("var clickTable = document.querySelector(\".continue\");\nvar bill = document.querySelector(\".bill\");\nclickTable.addEventListener(\"click\", function () {\n  if (bill.classList.contains(\"table_None\")) {\n    bill.classList.add(\"table_Block\");\n    bill.classList.remove(\"table_None\");\n  } else if (bill.classList.contains(\"table_Block\")) {\n    bill.classList.add(\"table_None\");\n    bill.classList.remove(\"table_Block\");\n  }\n});\n\n//# sourceURL=webpack://moshfeghi/./assets/scripts/cartToCartPeyment.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/cartToCartPeyment.js"]();
/******/ 	
/******/ })()
;