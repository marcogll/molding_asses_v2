/**
 * @file assessmentRoutes.js
 * @description Defines the routes for the employee assessment process.
 */

const express = require('express');
const router = express.Router();
const assessmentController = require('../controllers/assessmentController');

/**
 * @route GET /assessment/:employeeId
 * @description Initiates the assessment for a given employee.
 */
router.get('/:employeeId', assessmentController.validateForAssessment);

module.exports = router;
