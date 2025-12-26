/**
 * @file assessmentService.js
 * @description Service for assessment assignment logic.
 */

const surveyMap = {
  Operator: 'cmjlxk0dg000do501jm3nn416',
  Technician: 'cmjlxk143000eo501osrugdq1',
  Supervisor: 'cmjlxk1ye000fo501tdxgk2ls',
  Inspector: 'cmjlxk0dg000do501jm3nn416',
};

/**
 * Gets the survey ID for an employee based on their role.
 * @param {object} employee - The employee object.
 * @returns {string|null} The survey ID or null.
 */
const getSurveyIdForEmployee = (employee) => {
  if (!employee || !employee.role) {
    return null;
  }
  return surveyMap[employee.role] || null;
};

module.exports = {
  getSurveyIdForEmployee,
};
