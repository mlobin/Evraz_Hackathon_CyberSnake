import React from 'react';
import { Menu } from 'antd';

import { navigationConfig } from '../../configurations/navigation';

import './index.css';

const Navigation = ({ isNavigationVisible }) => (
  <Menu
    mode="inline"
    className="menu"
    items={navigationConfig}
    defaultOpenKeys={isNavigationVisible}
  />
);

export default Navigation;
