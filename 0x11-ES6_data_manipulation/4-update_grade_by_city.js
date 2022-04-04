export default function updateStudentGradeByCity(listEstudents, city, newGrades) {
  const listTest = listEstudents.filter((student) => student.location === city)
  const listTest2 = listTest.map((item) => {
    const arr = newGrades.filter((grade) => item.id === grade.studentId);
    item['grade'] = grade.studentId
  })

  
  //console.log(listTest)
  return listTest2

}