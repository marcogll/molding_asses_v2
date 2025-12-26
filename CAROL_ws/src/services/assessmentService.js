/**
 * @file assessmentService.js
 * @description Service for managing assessments in the database.
 */

const db = require('../config/database');

/**
 * Creates a new assessment.
 * @param {object} assessmentData - The data for the new assessment.
 * @returns {Promise<number>} The ID of the newly created assessment.
 */
const createAssessment = (assessmentData) => {
  return new Promise((resolve, reject) => {
    const { language, json_ref, participant_id } = assessmentData;
    const sql = `INSERT INTO Assessments (language, json_ref, participant_id)
                 VALUES (?, ?, ?)`;
    db.run(sql, [language, json_ref, participant_id], function (err) {
      if (err) {
        reject(err);
      } else {
        resolve(this.lastID);
      }
    });
  });
};

/**
 * Gets an assessment by its ID.
 * @param {number} id - The ID of the assessment.
 * @returns {Promise<object|null>} The assessment object or null if not found.
 */
const getAssessmentById = (id) => {
  return new Promise((resolve, reject) => {
    const sql = `SELECT * FROM Assessments WHERE id = ?`;
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
  createAssessment,
  getAssessmentById,
};
