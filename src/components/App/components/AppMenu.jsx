import React, { useState, useEffect } from 'react';
import { Layout } from 'antd';

import Navigation from '../../Navigation';


const { Sider } = Layout;

const AppMenu = () => {
  const [isSideMenuCollapsed, setIsSideMenuCollapsed] = useState();
  const onSideMenuCollapse = () => setIsSideMenuCollapsed(!isSideMenuCollapsed);

  useEffect(() => localStorage.setItem('batSideMenuState', isSideMenuCollapsed ? 'yes' : ''), [isSideMenuCollapsed]);

  return (
    <Sider
      width={175}
      collapsedWidth={70}
      theme="light"
      collapsible
      collapsed={isSideMenuCollapsed}
      onCollapse={onSideMenuCollapse}
    >
      <Navigation isNavigationVisible={!isSideMenuCollapsed} />
    </Sider>
  );
};

export default AppMenu;
