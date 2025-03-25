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

/***/ "./assets/scripts/homePage.js":
/*!************************************!*\
  !*** ./assets/scripts/homePage.js ***!
  \************************************/
/***/ (() => {

eval("// window.addEventListener('load', () => {\n//     document.getElementById('message').textContent = 'rr!';\n// }); \n\nlet comps = document.querySelectorAll(\".product>div\");\ncomps.forEach(comp => {\n  // console.log(comp)\n  let id = comp.querySelector(\"input\").value;\n  let title = comp.querySelector(\".productTitle\").textContent.replace(\" \", \"-\");\n  comp.addEventListener(\"mousedown\", function (e) {\n    e.stopPropagation();\n    if (e.button == 0) {\n      if (e.ctrlKey) {\n        window.open(`products/${id}/${title}`, '_blank');\n      } else {\n        window.location = `products/${id}/${title}`;\n      }\n    } else if (e.button == 1) {\n      window.open(`products/${id}/${title}`, '_blank');\n    }\n  });\n});\n\n//# sourceURL=webpack://moshfeghi/./assets/scripts/homePage.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/homePage.js"]();
/******/ 	
/******/ })()
;