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

/***/ "./src/index.ts":
/*!**********************!*\
  !*** ./src/index.ts ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _scripts_index__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./scripts/index */ \"./src/scripts/index.ts\");\n\n\n//# sourceURL=webpack://sms_mts/./src/index.ts?");

/***/ }),

/***/ "./src/scripts/index.ts":
/*!******************************!*\
  !*** ./src/scripts/index.ts ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _services_handler_handlerFormSubmit__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./services/handler/handlerFormSubmit */ \"./src/scripts/services/handler/handlerFormSubmit.ts\");\n/***\n * There is a listener of download a page\n */\n\ndocument.removeEventListener(\"DOMContentLoaded\", handlerMain);\ndocument.addEventListener(\"DOMContentLoaded\", handlerMain);\nfunction handlerMain() {\n  /***\n   * This is a function that is the main handler for all handlers. \n   */\n  const formHtml = document.querySelector(\"smsForm\");\n  if (formHtml === null) {\n    return false;\n  }\n  formHtml.removeEventListener(\"mousedown\", _services_handler_handlerFormSubmit__WEBPACK_IMPORTED_MODULE_0__.handlerEventSubmit);\n  formHtml.addEventListener(\"mousedown\", _services_handler_handlerFormSubmit__WEBPACK_IMPORTED_MODULE_0__.handlerEventSubmit);\n  return true;\n}\n\n//# sourceURL=webpack://sms_mts/./src/scripts/index.ts?");

/***/ }),

/***/ "./src/scripts/services/handler/handlerFormSubmit.ts":
/*!***********************************************************!*\
  !*** ./src/scripts/services/handler/handlerFormSubmit.ts ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerEventSubmit: () => (/* binding */ handlerEventSubmit)\n/* harmony export */ });\nasync function handlerEventSubmit(e) {\n  /**\n   * This is a event handler of button press of the type submit.\n   * It is  event of sending sms-massege from form. \n   */\n  if (!e.type || e.type && !e.type.includes(\"mousedown\") || !e.target.type && !e.target.type.includes(\"submit\")) {\n    return false;\n  }\n  ;\n  e.preventDefault();\n  const currentTarget = e.currentTarget;\n  return true;\n}\n\n//# sourceURL=webpack://sms_mts/./src/scripts/services/handler/handlerFormSubmit.ts?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
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
/******/ 	var __webpack_exports__ = __webpack_require__("./src/index.ts");
/******/ 	
/******/ })()
;