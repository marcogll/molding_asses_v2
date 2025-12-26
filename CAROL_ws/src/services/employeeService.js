// Import necessary modules
const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

// Define the path to the CSV file
const CSV_PATH = path.join(__dirname, '../../data/employees.csv');

/**
 * Validates an employee by their ID against the CSV data.
 * This function reads the CSV file, searches for the employee,
 * and checks if they are active.
 *
 * @param {string} employeeId - The ID of the employee to validate.
 * @returns {Promise<object|null>} A promise that resolves to the employee object if found and active, otherwise null.
 */
const validateEmployee = (employeeId) => {
  return new Promise((resolve, reject) => {
    // Check if the CSV file exists
    if (!fs.existsSync(CSV_PATH)) {
      console.error(`Error: Employee CSV file not found at ${CSV_PATH}`);
      return reject(new Error('Employee data is not available.'));
    }

    const results = [];
    fs.createReadStream(CSV_PATH)
      .pipe(csv())
      .on('data', (data) => results.push(data))
      .on('end', () => {
        // Find the employee by their ID
        const employee = results.find(row => row.employee_id === employeeId);

        // If employee is found and is active, resolve with their data
        if (employee && employee.active === 'true') {
          resolve(employee);
        } else {
          // If not found or not active, resolve with null
          resolve(null);
        }
      })
      .on('error', (error) => {
        // If there's an error reading the file, reject the promise
        console.error('Error reading or parsing employee CSV:', error);
        reject(error);
      });
  });
};

module.exports = {
  validateEmployee,
};
