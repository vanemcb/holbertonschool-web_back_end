export default function getResponseFromAPI() {
  const myPromise = new Promise((resolve, reject) => {
    if (true) {
      resolve('True');
    } else {
      reject(new Error('Error'));
    }
  });
  return myPromise;
}
