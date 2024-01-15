export const Converter = (isoTime) => {

    // convert iso date to ddmmyyy

  const date = new Date(isoTime);
  const day = date.getDate();
  const month = date.getMonth();
  const year = date.getFullYear();

  const results = day + "/" + `${month + 1}` + "/" + year;
  return results;
};