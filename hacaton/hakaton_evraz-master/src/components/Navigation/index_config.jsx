import React from 'react';
import { Link } from 'react-router-dom';


export const navigationConfig = [
  {
    label: <Link to={{ pathname: '/exhauster', search: '' }}>Exhauster</Link>,
    key: 'exhauster',
    title: 'Exhauster',
    // icon: ,
  },
  {
    label: <Link to={{ pathname: '/exhausters_all', search: '' }}>Exhausters all</Link>,
    key: 'exhausters_all',
    title: 'Exhausters all',
    // icon: ,
  },
  {
    label: 'Smth',
    key: 'Smt',
    title: 'Smth',
    // icon: ,
    children: nested_exhausters.map(({ itemKey, toPath, query, displayName }) => ({
      label: <Link to={{ pathname: toPath, search: query }}>{displayName}</Link>,
      key: itemKey,
      title: displayName,
    })),
  }
];
