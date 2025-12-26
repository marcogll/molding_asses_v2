/**
 * @file resultService.js
 * @description Service for managing results in the database.
 */

const db = require('../config/database');

/**
 * Creates a new result.
 * @param {object} resultData - The data for the new result.
 * @returns {Promise<number>} The ID of the newly created result.
 */
const createResult = (resultData) => {
  return new Promise((resolve, reject) => {
    const { participant_id, assessment_id, score, breakdown } = resultData;
    const sql = `INSERT INTO Results (participant_id, assessment_id, score, breakdown)
                 VALUES (?, ?, ?, ?)`;
    db.run(sql, [participant_id, assessment_id, score, breakdown], function (err) {
      if (err) {
        reject(err);
      } else {
        resolve(this.lastID);
      }
    });
  });
};

/**
 * Gets a result by its ID.
 * @param {number} id - The ID of the result.
 * @returns {Promise<object|null>} The result object or null if not found.
 */
const getResultById = (id) => {
  return new Promise((resolve, reject) => {
    const sql = `SELECT * FROM Results WHERE id = ?`;
    db.get(sql, [id], (err, row) => {
      if (err) {
        reject(err);
      } else {
        resolve(row);
      }
    });
  });
};

module.exports = {
  createResult,
  getResultById,
};
