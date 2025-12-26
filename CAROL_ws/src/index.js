// Import necessary modules
const express = require('express');
const dotenv = require('dotenv');

// Load environment variables from the root .env file
dotenv.config();

// Initialize the Express application
const app = express();

// Define the port and host from environment variables, with defaults
const PORT = process.env.PORT || 8000;
const HOST = process.env.HOST || '0.0.0.0';

// Middleware to parse JSON bodies
app.use(express.json());

// Health check endpoint to verify server status
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Server is running' });
});

// Import and use survey routes
const surveyRoutes = require('./routes/surveyRoutes');
app.use('/api/surveys', surveyRoutes);

// Start the server and listen for incoming connections
app.listen(PORT, HOST, () => {
  console.log(`CAROL-ws server is running on http://${HOST}:${PORT}`);
});

module.exports = app; // Export for potential testing
