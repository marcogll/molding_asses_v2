/**
 * @file participantService.js
 * @description Service for managing participants in the database.
 */

const db = require('../config/database');

/**
 * Creates a new participant.
 * @param {object} participantData - The data for the new participant.
 * @returns {Promise<number>} The ID of the newly created participant.
 */
const createParticipant = (participantData) => {
  return new Promise((resolve, reject) => {
    const { name, employee_id, department, role, experience_years, self_evaluation } = participantData;
    const sql = `INSERT INTO Participants (name, employee_id, department, role, experience_years, self_evaluation)
                 VALUES (?, ?, ?, ?, ?, ?)`;
    db.run(sql, [name, employee_id, department, role, experience_years, self_evaluation], function (err) {
      if (err) {
        reject(err);
      } else {
        resolve(this.lastID);
      }
    });
  });
};

/**
 * Gets a participant by their ID.
 * @param {number} id - The ID of the participant.
 * @returns {Promise<object|null>} The participant object or null if not found.
 */
const getParticipantById = (id) => {
  return new Promise((resolve, reject) => {
    const sql = `SELECT * FROM Participants WHERE id = ?`;
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
  createParticipant,
  getParticipantById,
};
