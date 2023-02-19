import React from "react";

import { Card, Tag } from "antd";

const Bearing = ({ bearing_name, bearing_data }) => {
  const get_colored_tag = (color, text) => <Tag color={color}>{text}</Tag>;
  
  let temperature_row = <p></p>;
  let vibration_row = <div></div>;
  if (bearing_data && bearing_data.temperature_status) {
    temperature_row =
      bearing_data.temperature_status == "alert"
        ? get_colored_tag("#8b0000", "Т")
        : bearing_data.temperature_status == "warning"
        ? get_colored_tag("#d2691e", "Т")
        : get_colored_tag("#2f484f", "Т");
  }
  if (bearing_data && bearing_data.vibration_status) {
    vibration_row =
      bearing_data.vibration_status == "alert"
        ? get_colored_tag("#8b0000", "В")
        : bearing_data.vibration_status == "warning"
        ? get_colored_tag("#d2691e", "В")
        : get_colored_tag("#2f484f", "В");
  }
  return (
    <Card
      style={{ borderColor: "#2f484f" }}
      title={"П-K:" + " " + bearing_name.slice(-1)}
      size="small"
    >
      {temperature_row}
      {vibration_row}
    </Card>
  );
};

export default Bearing;
