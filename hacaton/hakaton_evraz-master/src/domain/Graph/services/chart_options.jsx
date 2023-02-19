export const options1 = (data) => ({
  chart: {
    id: "chart2",
    type: "line",
    height: 330,
    foreColor: "#2f484f",
    toolbar: {
      autoSelected: "pan",
      show: false,
    },
  },
  colors: ["#00BAEC"],
  stroke: {
    width: 3,
  },
  grid: {
    borderColor: "#555",
    clipMarkers: false,
    yaxis: {
      lines: {
        show: false,
      },
    },
  },
  dataLabels: {
    enabled: false,
  },
  fill: {
    gradient: {
      enabled: true,
      opacityFrom: 0.55,
      opacityTo: 0,
    },
  },
  markers: {
    size: 5,
    colors: ["#000524"],
    strokeColor: "#00BAEC",
    strokeWidth: 3,
  },
  series: [
    {
      data: data,
    },
  ],
  tooltip: {
    theme: "dark",
  },
  xaxis: {
    type: "datetime",
  },
  yaxis: {
    min: 0,
    tickAmount: 4,
  },
});

export const options2 = (data) => ({
  chart: {
    id: "chart1",
    height: 230,
    type: "bar",
    foreColor: "#ccc",
    zoom: {
        autoScaleYaxis: true
      },
    brush: {
      target: "chart2",
      enabled: true,
    },
    selection: {
      enabled: true,
      fill: {
        color: "#fff",
        opacity: 0.4,
      },
      xaxis: {
        min: new Date("10 Feb 2023 10:00:00").getTime(),
        max: new Date("20 Feb 2023 10:00:00").getTime(),
      },
    },
  },
  colors: ["#FF0080"],
  series: [
    {
      data: data,
    },
  ],
  stroke: {
    width: 2,
  },
  grid: {
    borderColor: "#444",
  },
  markers: {
    size: 0,
  },
  xaxis: {
    type: "datetime",
    tooltip: {
      enabled: false,
    },
  },
  yaxis: {
    tickAmount: 2,
  },
});

export const options3 = {
chart: {
    id: "chart2",
    type: "line",
    height: 330,
    foreColor: "#2f484f",
    // zoom: {
    //     autoScaleYaxis: true
    //   },
    toolbar: {
        autoSelected: "pan",
        show: false,
    },
    },
  stroke: {
    curve: "stepline",
  },
  dataLabels: {
    enabled: false,
  },
  title: {
    text: "Stepline Chart",
    align: "left",
  },
  markers: {
    hover: {
      sizeOffset: 4,
    },
  },
  selection: {
    enabled: true,
    fill: {
      color: "#fff",
      opacity: 0.4,
    },
    xaxis: {
        type: "timestamp",
        min: new Date('10 Feb 2023 10:00:00').getTime(),
        tickAmount: 6,
    //   min: new Date("10 Feb 2023 10:00:00").getTime(),
    //   max: new Date("20 Feb 2023 10:00:00").getTime(),
    },
  },
  tooltip: {
    x: {
      format: 'dd MMM yyyy'
    },
  },
};

export const options4 = (data) => ({
  chart: {
    id: "chart2",
    type: "area",
    height: 230,
    foreColor: "#ccc",
    toolbar: {
      autoSelected: "pan",
      show: false,
    },
  },
  colors: ["#00BAEC"],
  stroke: {
    width: 3,
  },
  grid: {
    borderColor: "#555",
    clipMarkers: false,
    yaxis: {
      lines: {
        show: false,
      },
    },
  },
  dataLabels: {
    enabled: false,
  },
  fill: {
    gradient: {
      enabled: true,
      opacityFrom: 0.55,
      opacityTo: 0,
    },
  },
  markers: {
    size: 5,
    colors: ["#000524"],
    strokeColor: "#00BAEC",
    strokeWidth: 3,
  },
  series: [
    {
      data: data,
    },
  ],
  tooltip: {
    theme: "dark",
  },
  xaxis: {
    type: "datetime",
  },
  yaxis: {
    min: 0,
    tickAmount: 4,
  },
});

export const options5 = (data) => ({
  chart: {
    id: "chart1",
    height: 130,
    type: "bar",
    foreColor: "#ccc",
    brush: {
      target: "chart2",
      enabled: true,
    },
    selection: {
      enabled: true,
      fill: {
        color: "#fff",
        opacity: 0.4,
      },
      xaxis: {
        min: new Date("27 Jul 2017 10:00:00").getTime(),
        max: new Date("14 Aug 2017 10:00:00").getTime(),
      },
    },
  },
  colors: ["#FF0080"],
  series: [
    {
      data: data,
    },
  ],
  stroke: {
    width: 2,
  },
  grid: {
    borderColor: "#444",
  },
  markers: {
    size: 0,
  },
  xaxis: {
    type: "datetime",
    tooltip: {
      enabled: false,
    },
  },
  yaxis: {
    tickAmount: 2,
  },
});
