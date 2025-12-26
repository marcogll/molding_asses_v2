// Import axios for making HTTP requests
const axios = require('axios');

// Retrieve Formbricks credentials from environment variables
const { FORMBRICKS_URL, FORMBRICKS_API_KEY, FORMBRICKS_ENVIRONMENT_ID } = process.env;

// Check if the necessary environment variables are set
if (!FORMBRICKS_URL || !FORMBRICKS_API_KEY || !FORMBRICKS_ENVIRONMENT_ID) {
  throw new Error('Formbricks URL, API Key, or Environment ID are not defined in .env');
}

/**
 * Fetches all surveys from the Formbricks management API.
 * @returns {Promise<Array>} A promise that resolves to an array of survey objects.
 * @throws {Error} Throws an error if the API request fails.
 */
const getSurveys = async () => {
  try {
    // Construct the API endpoint URL
    const endpoint = `${FORMBRICKS_URL}/api/v1/management/surveys`;

    // Make a GET request to the Formbricks API
    const response = await axios.get(endpoint, {
      headers: {
        'x-api-key': FORMBRICKS_API_KEY,
        'Content-Type': 'application/json',
      },
      params: {
        environmentId: FORMBRICKS_ENVIRONMENT_ID,
      },
    });

    // Return the survey data from the response
    return response.data.data;
  } catch (error) {
    // Log the error for debugging purposes
    console.error('Error fetching surveys from Formbricks API:', error.response ? error.response.data : error.message);

    // Throw a new error to be caught by the caller
    throw new Error('Failed to fetch surveys.');
  }
};

// Export the service function
module.exports = {
  getSurveys,
};
