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

/***/ "./assets/scripts/change_pass.js":
/*!***************************************!*\
  !*** ./assets/scripts/change_pass.js ***!
  \***************************************/
/***/ (() => {

eval("const pass_field = document.querySelectorAll('.password');\nconst show_btns = document.querySelectorAll('.show');\nconsole.log(pass_field);\nconsole.log(show_btns);\nshow_btns.forEach((show_btn, i) => {\n  show_btn.addEventListener('click', function () {\n    if (pass_field[i].type === \"password\") {\n      pass_field[i].type = \"text\";\n      show_btn.style.color = \"#3498db\";\n      show_btn.textContent = \"عدم نمایش\";\n    } else {\n      pass_field.type = \"password\";\n      show_btn.style.color = \"#222\";\n      show_btn.textContent = \"نمایش\";\n    }\n  });\n});\n// for(let i=0; i<show_btn.length; i++){\n//     show_btn[i].addEventListener('click', function () {\n//         if (pass_field[i].type === \"password\") {\n//             pass_field[i].type = \"text\";\n//             show_btn[i].style.color = \"#3498db\";\n//             show_btn[i].textContent = \"عدم نمایش\";\n//         } else {\n//             pass_field[i].type = \"password\";\n//             show_btn[i].style.color = \"#222\";\n//             show_btn[i].textContent = \"نمایش\";\n//         }\n//     })\n// }\n\n//# sourceURL=webpack://moshfeghi/./assets/scripts/change_pass.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/change_pass.js"]();
/******/ 	
/******/ })()
;