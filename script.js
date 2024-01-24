const options = {
  key: "Cbbhfd803LdSO8G7uOcjCRQ63nZKazoP", // REPLACE WITH YOUR KEY !!!
  verbose: true,
  lat: 14.458002708309518,
  lon: 120.97128722057477,
  zoom: 10,
};

windyInit(options, (windyAPI) => {
  const { picker, utils, broadcast, store } = windyAPI;

  picker.on("pickerOpened", ({ lat, lon, values, overlay }) => {
    // -> 48.4, 14.3, [ U,V, ], 'wind'
    console.log("opened", lat, lon, values, overlay);

    const windObject = utils.wind2obj(values);
    console.log(windObject);
  });

  picker.on("pickerMoved", ({ lat, lon, values, overlay }) => {
    // picker was dragged by user to latLon coords
    console.log("moved", lat, lon, values, overlay);
  });

  picker.on("pickerClosed", () => {
    // picker was closed
  });

  store.on("pickerLocation", ({ lat, lon }) => {
    console.log(lat, lon);

    const { values, overlay } = picker.getParams();
    console.log("location changed", lat, lon, values, overlay);
  });

  // Wait since wather is rendered
  broadcast.once("redrawFinished", () => {
    // Opening of a picker (async)
    picker.open({ lat: 14.458002708309518, lon: 120.97128722057477 });
  });
});
