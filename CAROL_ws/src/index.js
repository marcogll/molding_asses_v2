/**
 * CAROL-ws - Assessment Gateway Web Server
 */

// --- DEPENDENCIES ---
const express = require('express');
const dotenv = require('dotenv');
const path = require('path');

// --- INITIALIZATION ---
dotenv.config();
const app = express();

// --- CONFIGURATION ---
const PORT = process.env.PORT || 8000;
const HOST = process.env.HOST || '0.0.0.0';

// --- MIDDLEWARE ---
app.use(express.json());
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// --- ROUTES ---
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK', message: 'Server is running' });
});

const surveyRoutes = require('./routes/surveyRoutes');
app.use('/api/surveys', surveyRoutes);

const assessmentRoutes = require('./routes/assessmentRoutes');
app.use('/assessment', assessmentRoutes);

// --- ERROR HANDLING ---
const errorHandler = require('./middleware/errorHandler');
app.use(errorHandler);

// --- SERVER STARTUP ---
app.listen(PORT, HOST, () => {
  console.log(`CAROL-ws server is running on http://${HOST}:${PORT}`);
});

// --- EXPORTS ---
module.exports = app;
