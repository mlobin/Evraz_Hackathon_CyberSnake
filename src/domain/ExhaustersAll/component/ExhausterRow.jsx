import React from "react";
import Moment from "moment";
import { useNavigate } from "react-router-dom";
import { Card, Row, Col } from "antd";

import Bearing from "./Bearing";
import "../index.css"

const ExhausterRow = ({ exhauster }) => {

  const check_rotor_status = (exhauster) => {
    let temperature_status = "ok"
    let vibration_status = "ok"
    for (const key in exhauster){
      if (exhauster[key] && key.startsWith("bearing")){
        if(exhauster[key].temperature_status == "warning" || exhauster[key].temperature_status == "alert"){
          temperature_status = exhauster[key].temperature_status
          break;
        }
        if(exhauster[key].vibration_status == "warning" || exhauster[key].vibration_status == "alert"){
          vibration_status = exhauster[key].vibration_status
          break;
        }
      }
    }
    return [temperature_status, vibration_status]
  }

  const navigate = useNavigate();
  const jumpToExhauster = () => {
    let path = "exhauster/"+String(exhauster?.meta.rotor_number);
    navigate(path);
  };
  const work_status = exhauster.is_active == 1 ? "Работает" : "Выключен"
  
  const [temperature_status, vibration_status] = check_rotor_status(exhauster)
  let card_color = "exhauter_card_ok"
  if (temperature_status == "warning" || vibration_status=="warning"){
    card_color = "exhauter_card_warning"
  }
  if (temperature_status == "alert" || vibration_status=="alert"){
    card_color = "exhauter_card_alert"
  }
  return (
    <div>
      <Row gutter={[8, 48]} className="exhauter_row_all" align="middle">
        <Col span={5} onClick={jumpToExhauster}>
          <Card className={card_color} style={{borderColor:"#2f484f"}} title={exhauster.meta.exhauster_name + " " + work_status} hoverable={true} size="small" headStyle={{color:"white"}}>
            <p><b>Время загруки</b> {Moment(exhauster.loaded_from_kafka_at).format("hh:mm:ss")}</p>
          </Card>
        </Col>
        {Object.entries(exhauster).map(([key, value]) => {
          if (key.startsWith("bearing")) {
            return (
              <Col span={2}>
                <Bearing bearing_name={key} bearing_data={value} />
              </Col>
            );
          }
        })}
      </Row>
    </div>
  );
};

export default ExhausterRow;
