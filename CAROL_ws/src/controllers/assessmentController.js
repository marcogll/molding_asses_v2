// Import the employee validation service
const employeeService = require('../services/employeeService');

/**
 * Controller to handle the employee validation for an assessment.
 * It uses the employee service to validate the employeeId from the URL parameters.
 *
 * @param {object} req - The Express request object, containing the employeeId.
 * @param {object} res - The Express response object.
 */
const validateForAssessment = async (req, res) => {
  try {
    const { employeeId } = req.params;

    // Validate the employee using the service
    const employee = await employeeService.validateEmployee(employeeId);

    // If the employee is not found or not active, return a 404 Not Found response
    if (!employee) {
      return res.status(404).json({
        message: 'Employee not found or not authorized for assessment.',
        employeeId,
      });
    }

    // If the employee is valid, return a 200 OK response with their data
    // In the future, this will trigger rendering the assessment
    res.status(200).json({
      message: 'Employee is authorized.',
      employee,
    });
  } catch (error) {
    // If an unexpected error occurs, return a 500 Internal Server Error response
    res.status(500).json({
      message: 'An error occurred during employee validation.',
      error: error.message,
    });
  }
};

module.exports = {
  validateForAssessment,
};
