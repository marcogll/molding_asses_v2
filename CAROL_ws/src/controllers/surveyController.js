// Import the Formbricks service to fetch surveys
const formbricksService = require('../services/formbricksService');

/**
 * Controller to handle the request for fetching all surveys.
 * It calls the Formbricks service and sends the surveys as a JSON response.
 * @param {object} req - The Express request object.
 * @param {object} res - The Express response object.
 */
const getAllSurveys = async (req, res) => {
  try {
    // Fetch surveys using the service
    const surveys = await formbricksService.getSurveys();

    // Send a successful response with the survey data
    res.status(200).json(surveys);
  } catch (error) {
    // If an error occurs, send an error response
    res.status(500).json({
      message: 'An error occurred while fetching surveys.',
      error: error.message,
    });
  }
};

// Export the controller function
module.exports = {
  getAllSurveys,
};
