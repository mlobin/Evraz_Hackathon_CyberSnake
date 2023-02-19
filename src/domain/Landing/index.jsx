import React from 'react';
import { Typography, Card, Space } from 'antd';

import './index.css';

const { Text } = Typography;

const StartingPage = () => {
  return (
    <div className="starting-page">
      <Card hoverable style={{ width: '50%', cursor: 'default' }}>
        <Space direction="horizontal" size={80}>
          <Text>
            Welcome
          </Text>
        </Space>
      </Card>
    </div>
  );
};

export default StartingPage;
