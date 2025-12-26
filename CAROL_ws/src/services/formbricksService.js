/**
 * @file formbricksService.js
 * @description Service for interacting with the Formbricks API.
 */

const axios = require('axios');

const { FORMBRICKS_URL, FORMBRICKS_API_KEY, FORMBRICKS_ENVIRONMENT_ID } = process.env;

if (!FORMBRICKS_URL || !FORMBRICKS_API_KEY || !FORMBRICKS_ENVIRONMENT_ID) {
  throw new Error('Formbricks environment variables are not defined.');
}

/**
 * Fetches all surveys from the Formbricks management API.
 * @returns {Promise<Array>} A promise that resolves with an array of survey objects.
 */
const getSurveys = async () => {
  try {
    const endpoint = `${FORMBRICKS_URL}/api/v1/management/surveys`;
    const response = await axios.get(endpoint, {
      headers: { 'x-api-key': FORMBRICKS_API_KEY },
      params: { environmentId: FORMBRICKS_ENVIRONMENT_ID },
    });
    return response.data.data;
  } catch (error) {
    const errorMessage = error.response
      ? `API Error: ${error.response.status} ${JSON.stringify(error.response.data)}`
      : `Request Error: ${error.message}`;
    console.error('Error fetching surveys from Formbricks API:', errorMessage);
    throw new Error('Could not fetch surveys from Formbricks.');
  }
};

module.exports = {
  getSurveys,
};
