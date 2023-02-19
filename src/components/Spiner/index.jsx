import React from 'react';
import { Spin } from 'antd';

import "./index.css"
// const Sizes = ['small', 'default', 'large'];
// const IsCentered = ['horizontally', 'vertically', 'both'];

const Spiner = ({
  size = 'default',
  isCentered = null,
  isFullScreen = false,
}) => {
  let style = { position: 'relative' };

  switch (isCentered) {
    case 'horizontally': {
      style.inset = '0 0 50% 50%';
      break;
    }
    case 'vertically': {
      style.inset = '50% 50% 0 0';
      break;
    }
    case 'both': {
      style.inset = '50%';
      break;
    }
    default: {
      style.inset = undefined;
      break;
    }
  }

  if (isFullScreen) {
    style = { position: 'absolute', inset: '50%'};
  }

  return <Spin style={style} size={size} />;
};

export default Spiner;
