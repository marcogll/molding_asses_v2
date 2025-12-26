/**
 * @file surveyController.js
 * @description Controller for survey-related API requests.
 */

const formbricksService = require('../services/formbricksService');

/**
 * Retrieves all surveys from Formbricks.
 * @param {object} req - Express request object.
 * @param {object} res - Express response object.
 * @param {function} next - Express next middleware function.
 */
const getAllSurveys = async (req, res, next) => {
  try {
    const surveys = await formbricksService.getSurveys();
    res.status(200).json(surveys);
  } catch (error) {
    next(error);
  }
};

module.exports = {
  getAllSurveys,
};
