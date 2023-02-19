import React from "react";
import { Link } from "react-router-dom";
import { Layout } from "antd";

const { Header } = Layout;

const AppHeader = () => {
  return (
    <>
      <Header className="header">
        <div className="appname">Прогнозная аналитика эксгаустеров</div>
        <div>
          <Link
            style={{
              float: "right",
              "background-color": "#d2691e",
              color: "white",
            }}
            to="graph"
            className="btn"
          >
            Графики сенсоров
          </Link>
        </div>
      </Header>
    </>
  );
};

export default AppHeader;
