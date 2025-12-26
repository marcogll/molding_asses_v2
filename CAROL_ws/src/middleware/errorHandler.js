/**
 * @file errorHandler.js
 * @description Centralized error handling middleware.
 */

const errorHandler = (err, req, res, next) => {
  console.error(err.stack);

  const statusCode = res.statusCode === 200 ? 500 : res.statusCode;

  res.status(statusCode).json({
    message: err.message || 'An unexpected error occurred.',
    stack: process.env.APP_ENV === 'development' ? err.stack : undefined,
  });
};

module.exports = errorHandler;
