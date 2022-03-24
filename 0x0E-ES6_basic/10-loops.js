export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const item of array) {
    array[idx] = appendString + item;
    idx++;
  }

  return array;
}
