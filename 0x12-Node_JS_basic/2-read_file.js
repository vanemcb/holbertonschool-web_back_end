const fs = require('fs');

const countStudents = (path) => {
  try {
    const arrayLines = fs.readFileSync(path, { encoding: 'utf8' }).split('\n');
    arrayLines.shift();
    const arrayData = arrayLines.map((row) => row.split(','));
    const dictField = {};

    for (const field of arrayData) {
      const keys = Object.keys(dictField);
      if (keys.includes(field[3])) {
        dictField[field[3]].push(field[0]);
      } else {
        dictField[field[3]] = [field[0]];
      }
    }

    console.log(`Number of students: ${arrayLines.length}`);
    const keysStr = Object.keys(dictField);
    keysStr.forEach((item) => {
      console.log(`Number of students in ${item}: ${dictField[item].length}. List: ${dictField[item].join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
module.exports = countStudents;
