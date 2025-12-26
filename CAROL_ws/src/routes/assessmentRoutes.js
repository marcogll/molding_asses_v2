// Import the Express module to create a router
const express = require('express');
const router = express.Router();

// Import the assessment controller
const assessmentController = require('../controllers/assessmentController');

// Define the route for validating an employee for an assessment
// GET /assessment/:employeeId
router.get('/:employeeId', assessmentController.validateForAssessment);

// Export the router to be used in the main application file
module.exports = router;
