/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./assets/scripts/popup.js":
/*!*********************************!*\
  !*** ./assets/scripts/popup.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   popup_success: () => (/* binding */ popup_success),\n/* harmony export */   popup_warning: () => (/* binding */ popup_warning)\n/* harmony export */ });\nlet popup_alert = document.querySelector(\".popup_alert\");\nfunction popup_success(time, text) {\n  popup_alert.querySelector(\"div>div>p\").innerHTML = text;\n  if (popup_alert.classList.contains(\"success\")) popup_alert.classList.remove(\"success\");else {\n    popup_alert.classList.add(\"success\");\n    const timeoutId = setTimeout(() => {\n      popup_alert.classList.remove(\"success\");\n    }, time);\n  }\n}\n;\nfunction popup_warning(time, text) {\n  popup_alert.querySelector(\"div>div>p\").innerHTML = text;\n  if (popup_alert.classList.contains(\"warning\")) popup_alert.classList.remove(\"warning\");else {\n    popup_alert.classList.add(\"warning\");\n    const timeoutId = setTimeout(() => {\n      popup_alert.classList.remove(\"warning\");\n    }, time);\n  }\n}\n;\n\n//# sourceURL=webpack://moshfeghi/./assets/scripts/popup.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The require scope
/******/ 	var __webpack_require__ = {};
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/popup.js"](0, __webpack_exports__, __webpack_require__);
/******/ 	
/******/ })()
;