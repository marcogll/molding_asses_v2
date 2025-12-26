/**
 * @file databaseService.js
 * @description Service for database initialization and management.
 */

const db = require('../config/database');

/**
 * Initializes the database schema.
 */
const initializeDatabase = () => {
  db.serialize(() => {
    // Participants Table
    db.run(`CREATE TABLE IF NOT EXISTS Participants (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      employee_id TEXT UNIQUE,
      department TEXT,
      role TEXT,
      experience_years INTEGER,
      self_evaluation INTEGER
    )`);

    // Assessments Table
    db.run(`CREATE TABLE IF NOT EXISTS Assessments (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      language TEXT NOT NULL,
      json_ref TEXT NOT NULL,
      participant_id INTEGER,
      FOREIGN KEY (participant_id) REFERENCES Participants (id)
    )`);

    // Results Table
    db.run(`CREATE TABLE IF NOT EXISTS Results (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      participant_id INTEGER,
      assessment_id INTEGER,
      score REAL,
      breakdown TEXT,
      FOREIGN KEY (participant_id) REFERENCES Participants (id),
      FOREIGN KEY (assessment_id) REFERENCES Assessments (id)
    )`);

    console.log('Database tables initialized or already exist.');
  });
};

module.exports = {
  initializeDatabase,
};
