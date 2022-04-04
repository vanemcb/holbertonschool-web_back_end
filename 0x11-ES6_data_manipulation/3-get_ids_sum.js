export default function getStudentIdsSum(listEstudents) {
  return listEstudents.reduce((prev, current) => prev.id + current.id, 0);
}
