/**
 * @file surveyRoutes.js
 * @description Defines API routes for Formbricks survey data.
 */

const express = require('express');
const router = express.Router();
const surveyController = require('../controllers/surveyController');

/**
 * @route GET /api/surveys
 * @description Retrieves a list of all available surveys.
 */
router.get('/', surveyController.getAllSurveys);

module.exports = router;
