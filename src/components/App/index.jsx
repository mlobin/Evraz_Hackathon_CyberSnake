import React, { useState, useEffect, Suspense } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { connect } from "react-redux";
import { Layout } from "antd";

import AppHeader from "./components/AppHeader.jsx";
import AppRoutes from "./components/AppRoutes.jsx";
import Spiner from '../Spiner';

import "./index.css";

const { Content } = Layout;

const App = () => {
  // const [loading, setLoading] = useState(true);
  // if (loading) return <Spiner isFullScreen size="large" />;
  return (
    <>
      <Router>
        <AppHeader />
        <Layout>
          <Suspense fallback={<Spiner isFullScreen size="large" />}>
            <Content>
              <AppRoutes />
            </Content>
          </Suspense>
        </Layout>
      </Router>
    </>
  );
};

export default connect(null, {})(App);
