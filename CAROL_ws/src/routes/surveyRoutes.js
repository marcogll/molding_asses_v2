// Import the Express module to create a router
const express = require('express');
const router = express.Router();

// Import the survey controller
const surveyController = require('../controllers/surveyController');

// Define the route for getting all surveys
// GET /api/surveys
router.get('/', surveyController.getAllSurveys);

// Export the router to be used in the main application file
module.exports = router;
