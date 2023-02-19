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
    title: "Температура подшипника 1",
    dataIndex: "bearing1__temperature",
    key: "bearing1__temperature",
  },
  {
    title: "Осевая подшипника 1",
    dataIndex: "bearing1__axial",
    key: "bearing1__axial",
  },
  {
    title: "Вертикальная вибрация подшипника 1",
    dataIndex: "bearing1__vertical",
    key: "bearing1__vertical",
  },
  {
    title: "Горизонтальная вибрация подшипника 1",
    dataIndex: "bearing1__horizontal",
    key: "bearing1__horizontal",
  },
  {
    title: "Температура подшипника 2",
    dataIndex: "bearing2__temperature",
    key: "bearing2__temperature",
  },
  {
    title: "Осевая подшипника 2",
    dataIndex: "bearing2__axial",
    key: "bearing2__axial",
  },
  {
    title: "Вертикальная вибрация подшипника 2",
    dataIndex: "bearing2__vertical",
    key: "bearing2__vertical",
  },
  {
    title: "Горизонтальная вибрация подшипника 2",
    dataIndex: "bearing2__horizontal",
    key: "bearing2__horizontal",
  },
  {
    title: "Температура подшипника 3",
    dataIndex: "bearing3__temperature",
    key: "bearing3__temperature",
  },
  {
    title: "Осевая подшипника 3",
    dataIndex: "bearing3__axial",
    key: "bearing3__axial",
  },
  {
    title: "Вертикальная вибрация подшипника 3",
    dataIndex: "bearing3__vertical",
    key: "bearing3__vertical",
  },
  {
    title: "Горизонтальная вибрация подшипника 3",
    dataIndex: "bearing3__horizontal",
    key: "bearing3__horizontal",
  },
  {
    title: "Температура подшипника 4",
    dataIndex: "bearing4__temperature",
    key: "bearing4__temperature",
  },
  {
    title: "Осевая подшипника 4",
    dataIndex: "bearing4__axial",
    key: "bearing4__axial",
  },
  {
    title: "Вертикальная вибрация подшипника 4",
    dataIndex: "bearing4__vertical",
    key: "bearing4__vertical",
  },
  {
    title: "Горизонтальная вибрация подшипника 4",
    dataIndex: "bearing4__horizontal",
    key: "bearing4__horizontal",
  },
];

// export const hashtagsTableColumns = [
//   {
//     title: 'Label',
//     dataIndex: 'label',
//     key: 'label',
//     width: 300,
//     render: (label: string): JSX.Element => <Paragraph copyable>{'#' + label}</Paragraph>,
//   },
//   {
//     title: 'Usage',
//     dataIndex: 'deprecated',
//     key: 'deprecated',
//     width: 200,
//     render: (deprecated: boolean): JSX.Element => (
//       <Paragraph>{deprecated ? <Tag>DEPRECATED</Tag> : <Tag color="green">IN USE</Tag>}</Paragraph>
//     ),
//   },
//   {
//     title: 'Created / Updated by',
//     key: 'CreatedByUpdatedBy',
//     width: 280,
//     render: (_: any, allValues: Hashtag): JSX.Element => (
//       <CreatedByUpdatedByCell createdBy={allValues.createdBy} updatedBy={allValues.updatedBy} />
//     ),
//   },
//   {
//     title: `[${timeZone}] Created / Updated at`,
//     key: 'CreatedAtUpdatedAt',
//     fixed: 'right',
//     width: 280,
//     render: (_: any, allValues: Hashtag): JSX.Element => (
//       // @ts-ignore
//       <CreatedAtUpdatedAt createdAt={allValues?.createdAt} updatedAt={allValues?.updatedAt} />
//     ),
//   },
//   {
//     title: 'Actions',
//     key: 'actions',
//     dataIndex: 'id',
//     fixed: 'right',
//     width: 100,
//     render: (id: number): JSX.Element => (
//       <Button type="link">
//         <Link to={{ state: { hashtagId: id } }} replace>
//           Edit
//         </Link>
//       </Button>
//     ),
//   },
// ];
