import React from "react";
import { Card, Tag } from "antd";
import Spiner from "../../components/Spiner";

import { columns } from "./services/exhauster_columns";
import { useExhauster } from "./hooks/useExhauster";

import "./index.css";
// const { Title } = Typography;

const STATUS_STYLES_DICT = {
  alert: "#8b0000",
  warning: "#d2691e",
  ok: "#2f484f",
  no_data: "#2f484f",
};

const Exhauster = () => {
  const [exhauster, loading] = useExhauster();
  console.log(exhauster);

  const generate_bearing_with_card = (field, bearing_number, card_style) => (
    <div className="exhauter_card">
      <Card
        className={"exhauter_card_ok"}
        style={card_style}
        headStyle={{ color: "white" }}
        title={bearing_number + " " + "ПС"}
      >
        <p>
          <Tag color={STATUS_STYLES_DICT[String(field.temperature_status)]}>
            T, &#176;C {field.temperature.value}{" "}
          </Tag>
        </p>
        <p>
          {" "}
          <Tag color={STATUS_STYLES_DICT[String(field.vibration_status)]}>
            В, мм/c {field.vertical_vibration.value}{" "}
          </Tag>
        </p>
        <p>
          {" "}
          <Tag color={STATUS_STYLES_DICT[String(field.vibration_status)]}>
            Г, мм/c {field.horizontal_vibration.value}{" "}
          </Tag>
        </p>
        <p>
          {" "}
          <Tag color={STATUS_STYLES_DICT[String(field.vibration_status)]}>
            О, мм/c {field.axial_vibration.value}{" "}
          </Tag>
        </p>
      </Card>
    </div>
  );
  const generate_bearing_without_card = (field, bearing_number, card_style) => (
    <div className="exhauter_card">
      <Card
        className={"exhauter_card_ok"}
        style={card_style}
        headStyle={{ color: "white" }}
        title={bearing_number + " " + "ПС"}
      >
        <p>
          <Tag color={STATUS_STYLES_DICT[String(field.temperature_status)]}>
            T, &#176;C {field.temperature.value}{" "}
          </Tag>{" "}
        </p>
      </Card>
    </div>
  );

  if (loading) return <Spiner isFullScreen size="large" />;
  return (
    <div className="background">
    <div className="background_exhauter_picture first">
      {generate_bearing_with_card(
        exhauster.bearing_with_vibration_sensor_1,
        1,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture second">
      {generate_bearing_with_card(
        exhauster.bearing_with_vibration_sensor_2,
        2,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture seventh">
      {generate_bearing_with_card(
        exhauster.bearing_with_vibration_sensor_7,
        7,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture eighth">
      {generate_bearing_with_card(
        exhauster.bearing_with_vibration_sensor_8,
        8,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture third">
      {generate_bearing_without_card(
        exhauster.bearing_without_vibration_sensor_3,
        3,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture forth">
      {generate_bearing_without_card(
        exhauster.bearing_without_vibration_sensor_4,
        4,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture fifth">
      {generate_bearing_without_card(
        exhauster.bearing_without_vibration_sensor_5,
        5,
        { borderColor: "#2f484f" }
      )}
    </div>
    <div className="background_exhauter_picture sixth">
      {generate_bearing_without_card(
        exhauster.bearing_without_vibration_sensor_6,
        6,
        { borderColor: "#2f484f"}
      )}
    </div>
    <div className="background_exhauter_picture ninth" style={{top:"558px"}}>
      {generate_bearing_without_card(
        exhauster.bearing_without_vibration_sensor_9,
        9,
        { borderColor: "#2f484f" }
      )}
    </div>
      <div className="exhauter_card main_engine" style={{width:"300px"}}>
        <Card
          className={"exhauter_card_ok"}
          style={{ borderColor: "#2f484f" }}
          headStyle={{ color: "white" }}
          title={"Главный привод"}
        >
          <p>Ток, А{exhauster.main_drive.rotor_current}</p>
          <p>Ток двигателя, А{exhauster.main_drive.rotor_voltage}</p>
          <p>Напряжения ротора, кВт{exhauster.main_drive.stator_current} </p>
          <p>Напряжение статера, кВт{exhauster.main_drive.stator_voltage} </p>
        </Card>
      </div>
        <div className="oil_level">Уровень масла {exhauster.oil_system.oil_level}</div>
        <div className="oil_pressure">Давление масла 4.8{exhauster.oil_system.oil_pressure}</div>
    
</div>
  );
};

export default Exhauster;
