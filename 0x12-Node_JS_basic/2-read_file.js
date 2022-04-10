const fs = require('fs')

const countStudents = (path) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      throw Error('Cannot load the database');
    }
    const arrayLines = data.split('\n');
    arrayLines.shift();
    const arrayData = arrayLines.map(row => row.split(","));
    const dictField = {};
    const listName = [];
    for (let field of arrayData) {
      for (let i = 0; i < field.length; i++) {
        dictField[field[3]] = listName.push('hola')
      }
    }

    console.log(arrayData)
    console.log(dictField)
    console.log(`Number of students: ${arrayLines.length}`)
  })
}

module.exports = countStudents;