import React from "react";
import { Typography, Button, Tag } from "antd";
// import { Link } from 'react-router-dom';

// import CreatedAtUpdatedAt from '../../../components/TableCells/CreatedAtUpdatedAt';

// import { timeZone } from '../../../services/renderFormattedDate';
// import { Hashtag } from '../types';
// import CreatedByUpdatedByCell from '../components/CreatedByUpdatedByCell';

// const { Paragraph } = Typography;

export const dataSource = [
  {
    key: "1",
    name: "Mike",
    age: 32,
    address: "10 Downing Street",
  },
  {
    key: "2",
    name: "John",
    age: 42,
    address: "10 Downing Street",
  },
];

export const columns = [
  {
    title: "Текущее значение температуры подшипника 1",
    dataIndex: "bearing1__temperature__value",
    key: "bearing1__temperature__value",
  },
  {
    title: "Предупредительная ставка минимальной температуры подшипника 1",
    dataIndex: "bearing1__temperature__warning_min",
    key: "bearing1__temperature__warning_min",
  },
  {
    title: "Предупредительная ставка максимальной температуры подшипника 1",
    dataIndex: "bearing1__temperature__warning_max",
    key: "bearing1__temperature__warning_max",
  },
  {
    title: "Аварийная ставка минимальной температуры подшипника 1",
    dataIndex: "bearing1__temperature__alarm_min",
    key: "bearing1__temperature__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной температуры подшипника 1",
    dataIndex: "bearing1__temperature__alarm_max",
    key: "bearing1__temperature__alarm_max",
  },
  {
    title: "Текущее осевое значение подшипника 1",
    dataIndex: "bearing1__axial__value",
    key: "bearing1__axial__value",
  },
  {
    title:
      "Предупредительная ставка минимального осевого значения подшипника 1",
    dataIndex: "bearing1__axial__warning_min",
    key: "bearing1__axial__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимального осевого значения подшипника 1",
    dataIndex: "bearing1__axial__warning_max",
    key: "bearing1__axial__warning_max",
  },
  {
    title: "Аварийная ставка минимального осевого значения подшипника 1",
    dataIndex: "bearing1__axial__alarm_min",
    key: "bearing1__axial__alarm_min",
  },
  {
    title: "Аварийная ставка максимального осевого значения подшипника 1",
    dataIndex: "bearing1__axial__alarm_max",
    key: "bearing1__axial__alarm_max",
  },
  {
    title: "Текущее значение вертикальной вибрации подшипника 1",
    dataIndex: "bearing1__vertical__value",
    key: "bearing1__vertical__value",
  },
  {
    title:
      "Предупредительная ставка минимальной вертикальной вибрации подшипника 1",
    dataIndex: "bearing1__vertical__warning_min",
    key: "bearing1__vertical__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной вертикальной вибрации подшипника 1",
    dataIndex: "bearing1__vertical__warning_max",
    key: "bearing1__vertical__warning_max",
  },
  {
    title: "Аварийная ставка минимальной вертикальной вибрации подшипника 1",
    dataIndex: "bearing1__vertical__alarm_min",
    key: "bearing1__vertical__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной вертикальной вибрации подшипника 1",
    dataIndex: "bearing1__vertical__alarm_max",
    key: "bearing1__vertical__alarm_max",
  },
  {
    title: "Текущее значение горизонтальной вибрации подшипника 1",
    dataIndex: "bearing1__horizontal__value",
    key: "bearing1__horizontal__value",
  },
  {
    title:
      "Предупредительная ставка минимальной горизонтальной вибрации подшипника 1",
    dataIndex: "bearing1__horizontal__warning_min",
    key: "bearing1__horizontal__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной горизонтальной вибрации подшипника 1",
    dataIndex: "bearing1__horizontal__warning_max",
    key: "bearing1__horizontal__warning_max",
  },
  {
    title: "Аварийная ставка минимальной горизонтальной вибрации подшипника 1",
    dataIndex: "bearing1__horizontal__alarm_min",
    key: "bearing1__horizontal__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной горизонтальной вибрации подшипника 1",
    dataIndex: "bearing1__horizontal__alarm_max",
    key: "bearing1__horizontal__alarm_max",
  },
  {
    title: "Текущее значение температуры подшипника 2",
    dataIndex: "bearing2__temperature__value",
    key: "bearing2__temperature__value",
  },
  {
    title: "Предупредительная ставка минимальной температуры подшипника 2",
    dataIndex: "bearing2__temperature__warning_min",
    key: "bearing2__temperature__warning_min",
  },
  {
    title: "Предупредительная ставка максимальной температуры подшипника 2",
    dataIndex: "bearing2__temperature__warning_max",
    key: "bearing2__temperature__warning_max",
  },
  {
    title: "Аварийная ставка минимальной температуры подшипника 2",
    dataIndex: "bearing2__temperature__alarm_min",
    key: "bearing2__temperature__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной температуры подшипника 2",
    dataIndex: "bearing2__temperature__alarm_max",
    key: "bearing2__temperature__alarm_max",
  },
  {
    title: "Текущее осевое значение подшипника 2",
    dataIndex: "bearing2__axial__value",
    key: "bearing2__axial__value",
  },
  {
    title:
      "Предупредительная ставка минимального осевого значения подшипника 2",
    dataIndex: "bearing2__axial__warning_min",
    key: "bearing2__axial__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимального осевого значения подшипника 2",
    dataIndex: "bearing2__axial__warning_max",
    key: "bearing2__axial__warning_max",
  },
  {
    title: "Аварийная ставка минимального осевого значения подшипника 2",
    dataIndex: "bearing2__axial__alarm_min",
    key: "bearing2__axial__alarm_min",
  },
  {
    title: "Аварийная ставка максимального осевого значения подшипника 2",
    dataIndex: "bearing2__axial__alarm_max",
    key: "bearing2__axial__alarm_max",
  },
  {
    title: "Текущее значение вертикальной вибрации подшипника 2",
    dataIndex: "bearing2__vertical__value",
    key: "bearing2__vertical__value",
  },
  {
    title:
      "Предупредительная ставка минимальной вертикальной вибрации подшипника 2",
    dataIndex: "bearing2__vertical__warning_min",
    key: "bearing2__vertical__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной вертикальной вибрации подшипника 2",
    dataIndex: "bearing2__vertical__warning_max",
    key: "bearing2__vertical__warning_max",
  },
  {
    title: "Аварийная ставка минимальной вертикальной вибрации подшипника 2",
    dataIndex: "bearing2__vertical__alarm_min",
    key: "bearing2__vertical__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной вертикальной вибрации подшипника 2",
    dataIndex: "bearing2__vertical__alarm_max",
    key: "bearing2__vertical__alarm_max",
  },
  {
    title: "Текущее значение горизонтальной вибрации подшипника 2",
    dataIndex: "bearing2__horizontal__value",
    key: "bearing2__horizontal__value",
  },
  {
    title:
      "Предупредительная ставка минимальной горизонтальной вибрации подшипника 2",
    dataIndex: "bearing2__horizontal__warning_min",
    key: "bearing2__horizontal__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной горизонтальной вибрации подшипника 2",
    dataIndex: "bearing2__horizontal__warning_max",
    key: "bearing2__horizontal__warning_max",
  },
  {
    title: "Аварийная ставка минимальной горизонтальной вибрации подшипника 2",
    dataIndex: "bearing2__horizontal__alarm_min",
    key: "bearing2__horizontal__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной горизонтальной вибрации подшипника 2",
    dataIndex: "bearing2__horizontal__alarm_max",
    key: "bearing2__horizontal__alarm_max",
  },
  {
    title: "Текущее значение температуры подшипника 3",
    dataIndex: "bearing3__temperature__value",
    key: "bearing3__temperature__value",
  },
  {
    title: "Предупредительная ставка минимальной температуры подшипника 3",
    dataIndex: "bearing3__temperature__warning_min",
    key: "bearing3__temperature__warning_min",
  },
  {
    title: "Предупредительная ставка максимальной температуры подшипника 3",
    dataIndex: "bearing3__temperature__warning_max",
    key: "bearing3__temperature__warning_max",
  },
  {
    title: "Аварийная ставка минимальной температуры подшипника 3",
    dataIndex: "bearing3__temperature__alarm_min",
    key: "bearing3__temperature__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной температуры подшипника 3",
    dataIndex: "bearing3__temperature__alarm_max",
    key: "bearing3__temperature__alarm_max",
  },
  {
    title: "Текущее осевое значение подшипника 3",
    dataIndex: "bearing3__axial__value",
    key: "bearing3__axial__value",
  },
  {
    title:
      "Предупредительная ставка минимального осевого значения подшипника 3",
    dataIndex: "bearing3__axial__warning_min",
    key: "bearing3__axial__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимального осевого значения подшипника 3",
    dataIndex: "bearing3__axial__warning_max",
    key: "bearing3__axial__warning_max",
  },
  {
    title: "Аварийная ставка минимального осевого значения подшипника 3",
    dataIndex: "bearing3__axial__alarm_min",
    key: "bearing3__axial__alarm_min",
  },
  {
    title: "Аварийная ставка максимального осевого значения подшипника 3",
    dataIndex: "bearing3__axial__alarm_max",
    key: "bearing3__axial__alarm_max",
  },
  {
    title: "Текущее значение вертикальной вибрации подшипника 3",
    dataIndex: "bearing3__vertical__value",
    key: "bearing3__vertical__value",
  },
  {
    title:
      "Предупредительная ставка минимальной вертикальной вибрации подшипника 3",
    dataIndex: "bearing3__vertical__warning_min",
    key: "bearing3__vertical__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной вертикальной вибрации подшипника 3",
    dataIndex: "bearing3__vertical__warning_max",
    key: "bearing3__vertical__warning_max",
  },
  {
    title: "Аварийная ставка минимальной вертикальной вибрации подшипника 3",
    dataIndex: "bearing3__vertical__alarm_min",
    key: "bearing3__vertical__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной вертикальной вибрации подшипника 3",
    dataIndex: "bearing3__vertical__alarm_max",
    key: "bearing3__vertical__alarm_max",
  },
  {
    title: "Текущее значение горизонтальной вибрации подшипника 3",
    dataIndex: "bearing3__horizontal__value",
    key: "bearing3__horizontal__value",
  },
  {
    title:
      "Предупредительная ставка минимальной горизонтальной вибрации подшипника 3",
    dataIndex: "bearing3__horizontal__warning_min",
    key: "bearing3__horizontal__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной горизонтальной вибрации подшипника 3",
    dataIndex: "bearing3__horizontal__warning_max",
    key: "bearing3__horizontal__warning_max",
  },
  {
    title: "Аварийная ставка минимальной горизонтальной вибрации подшипника 3",
    dataIndex: "bearing3__horizontal__alarm_min",
    key: "bearing3__horizontal__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной горизонтальной вибрации подшипника 3",
    dataIndex: "bearing3__horizontal__alarm_max",
    key: "bearing3__horizontal__alarm_max",
  },
  {
    title: "Текущее значение температуры подшипника 4",
    dataIndex: "bearing4__temperature__value",
    key: "bearing4__temperature__value",
  },
  {
    title: "Предупредительная ставка минимальной температуры подшипника 4",
    dataIndex: "bearing4__temperature__warning_min",
    key: "bearing4__temperature__warning_min",
  },
  {
    title: "Предупредительная ставка максимальной температуры подшипника 4",
    dataIndex: "bearing4__temperature__warning_max",
    key: "bearing4__temperature__warning_max",
  },
  {
    title: "Аварийная ставка минимальной температуры подшипника 4",
    dataIndex: "bearing4__temperature__alarm_min",
    key: "bearing4__temperature__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной температуры подшипника 4",
    dataIndex: "bearing4__temperature__alarm_max",
    key: "bearing4__temperature__alarm_max",
  },
  {
    title: "Текущее осевое значение подшипника 4",
    dataIndex: "bearing4__axial__value",
    key: "bearing4__axial__value",
  },
  {
    title:
      "Предупредительная ставка минимального осевого значения подшипника 4",
    dataIndex: "bearing4__axial__warning_min",
    key: "bearing4__axial__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимального осевого значения подшипника 4",
    dataIndex: "bearing4__axial__warning_max",
    key: "bearing4__axial__warning_max",
  },
  {
    title: "Аварийная ставка минимального осевого значения подшипника 4",
    dataIndex: "bearing4__axial__alarm_min",
    key: "bearing4__axial__alarm_min",
  },
  {
    title: "Аварийная ставка максимального осевого значения подшипника 4",
    dataIndex: "bearing4__axial__alarm_max",
    key: "bearing4__axial__alarm_max",
  },
  {
    title: "Текущее значение вертикальной вибрации подшипника 4",
    dataIndex: "bearing4__vertical__value",
    key: "bearing4__vertical__value",
  },
  {
    title:
      "Предупредительная ставка минимальной вертикальной вибрации подшипника 4",
    dataIndex: "bearing4__vertical__warning_min",
    key: "bearing4__vertical__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной вертикальной вибрации подшипника 4",
    dataIndex: "bearing4__vertical__warning_max",
    key: "bearing4__vertical__warning_max",
  },
  {
    title: "Аварийная ставка минимальной вертикальной вибрации подшипника 4",
    dataIndex: "bearing4__vertical__alarm_min",
    key: "bearing4__vertical__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной вертикальной вибрацииподшипника 4",
    dataIndex: "bearing4__vertical__alarm_max",
    key: "bearing4__vertical__alarm_max",
  },
  {
    title: "Текущее значение горизонтальной вибрации подшипника 4",
    dataIndex: "bearing4__horizontal__value",
    key: "bearing4__horizontal__value",
  },
  {
    title:
      "Предупредительная ставка минимальной горизонтальной вибрации подшипника 4",
    dataIndex: "bearing4__horizontal__warning_min",
    key: "bearing4__horizontal__warning_min",
  },
  {
    title:
      "Предупредительная ставка максимальной горизонтальной вибрации подшипника 4",
    dataIndex: "bearing4__horizontal__warning_max",
    key: "bearing4__horizontal__warning_max",
  },
  {
    title: "Аварийная ставка минимальной горизонтальной вибрации подшипника 4",
    dataIndex: "bearing4__horizontal__alarm_min",
    key: "bearing4__horizontal__alarm_min",
  },
  {
    title: "Аварийная ставка максимальной горизонтальной вибрации подшипника 4",
    dataIndex: "bearing4__horizontal__alarm_max",
    key: "bearing4__horizontal__alarm_max",
  },
];
