export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const item of array) {
    array[idx] = appendString + item;// eslint-disable-line no-param-reassign
    idx += 1;
  }

  return array;
}
