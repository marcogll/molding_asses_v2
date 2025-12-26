/**
 * @file assessmentController.js
 * @description Controller for the employee assessment process.
 */

const employeeService = require('../services/employeeService');
const assessmentService = require('../services/assessmentService');

/**
 * Validates an employee and renders their assigned assessment.
 * @param {object} req - Express request object.
 * @param {object} res - Express response object.
 * @param {function} next - Express next middleware function.
 */
const validateForAssessment = async (req, res, next) => {
  try {
    const { employeeId } = req.params;
    const employee = await employeeService.validateEmployee(employeeId);

    if (!employee) {
      res.status(404);
      return res.render('error', {
        title: 'Acceso no Autorizado',
        message: 'El número de empleado que ingresaste no es válido o no tiene permiso para realizar esta evaluación.',
        employeeId,
      });
    }

    const surveyId = assessmentService.getSurveyIdForEmployee(employee);

    if (!surveyId) {
      res.status(404);
      return res.render('error', {
        title: 'Evaluación no Asignada',
        message: 'No se ha encontrado una evaluación asignada para tu rol. Por favor, contacta a tu supervisor.',
        employeeId: employee.employee_id,
      });
    }

    res.render('assessment', {
      employeeId: employee.employee_id,
      surveyId,
      formbricksUrl: process.env.FORMBRICKS_URL,
      environmentId: process.env.FORMBRICKS_ENVIRONMENT_ID,
    });
  } catch (error) {
    next(error);
  }
};

module.exports = {
  validateForAssessment,
};
