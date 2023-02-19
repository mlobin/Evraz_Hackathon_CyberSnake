import React from 'react';
import { Typography, Space, Result, Button } from 'antd';
import { useNavigate } from 'react-router';

const NotFoundPage = ({ message }) => {
  const navigate = useNavigate();

  return (
    <Result
      status="warning"
      title={
        <Space direction="vertical">
          <Typography.Text>Something went wrong.</Typography.Text>
          {message ? <Typography.Text type="danger" color='#d2691e'>{message}</Typography.Text> : null}
        </Space>
      }
      extra={
        <Button type="default" color='#2f484f' onClick={navigate(-1)}>
          Go Back
        </Button>
      }
    />
  );
};

export default NotFoundPage;
