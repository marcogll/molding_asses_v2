/**
 * @file employeeService.js
 * @description Service for employee data validation.
 */

const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const CSV_PATH = path.join(__dirname, '../../data/employees.csv');

/**
 * Validates an employee by their ID against CSV data.
 * @param {string} employeeId - The ID of the employee to validate.
 * @returns {Promise<object|null>} The employee object or null.
 */
const validateEmployee = (employeeId) => {
  return new Promise((resolve, reject) => {
    if (!fs.existsSync(CSV_PATH)) {
      const error = new Error(`Employee CSV file not found at path: ${CSV_PATH}`);
      console.error(error.message);
      return reject(error);
    }

    const employees = [];
    fs.createReadStream(CSV_PATH)
      .pipe(csv())
      .on('data', (row) => employees.push(row))
      .on('end', () => {
        const employee = employees.find(emp => emp.employee_id === employeeId);
        if (employee && employee.active === 'true') {
          resolve(employee);
        } else {
          resolve(null);
        }
      })
      .on('error', (error) => {
        console.error('An error occurred while parsing the employee CSV file:', error);
        reject(error);
      });
  });
};

module.exports = {
  validateEmployee,
};
