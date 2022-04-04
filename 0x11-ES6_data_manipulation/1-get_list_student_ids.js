export default function getListStudentIds(array) {
  if (typeof array !== 'object') return [];
  const listIds = array.map((item) => item.id);
  return listIds;
}
