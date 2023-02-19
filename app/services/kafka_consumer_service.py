import kafka
from kafka import TopicPartition
from orjson import loads

from app.entrypoint.database import SessionLocal
from app.models.exhauster import (
    ExhausterModel,
    OilSystemModel,
    MainDriveModel,
    RefrigerantModel,
    # ExhausterMetadataModel,
    ValvePositionModel,
    GasManifoldModel,
    SensorModel,
    # BearingWithoutVibrationSensorModel,
    BearingWithVibrationSensorModel, BearingWithoutVibrationSensorModel,
)
from app.models.exhauster.sensor import SensorTypesEnum


class KafkaConsumerService:
    active_flag: bool = True
    __model = ExhausterModel

    @classmethod
    def parse_data(cls):
        consumer = kafka.KafkaConsumer(
            bootstrap_servers=["rc1a-2ar1hqnl386tvq7k.mdb.yandexcloud.net:9091"],
            sasl_mechanism="SCRAM-SHA-512",
            security_protocol="SASL_SSL",
            sasl_plain_username="9433_reader",
            sasl_plain_password="eUIpgWu0PWTJaTrjhjQD3.hoyhntiK",
            ssl_cafile="CA.pem",
        )
        partition = TopicPartition("zsmk-9433-dev-01", 0)
        assigned_topic = [partition]
        consumer.assign(assigned_topic)
        #consumer.seek_to_beginning()
        for i in consumer:
            with SessionLocal.begin() as session:
                data = i.value
                data = loads(data)
                loaded_from_kafka_at = data["moment"]
                parsed_data = cls.__parse_kafka_data(data)
                exhausters = []
                for idx_exhauster, i in enumerate([
                    "exhauster_1",
                    "exhauster_2",
                    "exhauster_3",
                    "exhauster_4",
                    "exhauster_5",
                    "exhauster_6",
                ]):
                    exhauster_kafka_data = parsed_data[i]
                    bearings = []
                    for idx, bearing_kafka_data in enumerate(
                        exhauster_kafka_data["bearings"]
                    ):
                        if "vibration_status" in bearing_kafka_data:
                            bearing_model = BearingWithVibrationSensorModel(
                                number=idx,
                                temperature_status=bearing_kafka_data["temperature_status"],
                                vibration_status=bearing_kafka_data["vibration_status"],
                                temperature=SensorModel(**bearing_kafka_data["temperature"], type="temperature"),
                                axial_vibration=SensorModel(
                                    **bearing_kafka_data["vibration_axial"], type="vibration"
                                ),
                                horizontal_vibration=SensorModel(
                                    **bearing_kafka_data["vibration_horizontal"], type="vibration"
                                ),
                                vertical_vibration=SensorModel(
                                    **bearing_kafka_data["vibration_vertical"], type="vibration"
                                ),
                            )
                        else:
                            bearing_model = BearingWithoutVibrationSensorModel(
                                number=idx,
                                temperature=SensorModel(**bearing_kafka_data["temperature"], type="temperature"),
                                temperature_status=bearing_kafka_data["temperature_status"]
                            )
                        bearings.append(bearing_model)

                    exhauster = ExhausterModel(
                        meta_id=idx_exhauster+1,
                        refrigerant=RefrigerantModel(
                            **exhauster_kafka_data["exhauster"]["refrigerant"]
                        ),
                        gas_manifold=GasManifoldModel(
                            **exhauster_kafka_data["exhauster"]["gas_manifold"]
                        ),
                        valve_position=ValvePositionModel(
                            **exhauster_kafka_data["exhauster"]["valve_position"]
                        ),
                        main_drive=MainDriveModel(
                            **exhauster_kafka_data["exhauster"]["main_drive"]
                        ),
                        oil_system=OilSystemModel(
                            **exhauster_kafka_data["exhauster"]["oil_system"]
                        ),
                        bearing_with_vibration_sensor_1=bearings[0],
                        bearing_with_vibration_sensor_2=bearings[1],
                        bearing_without_vibration_sensor_3 = bearings[2],
                        bearing_without_vibration_sensor_4=bearings[3],
                        bearing_without_vibration_sensor_5=bearings[4],
                        bearing_without_vibration_sensor_6=bearings[5],
                        bearing_with_vibration_sensor_7=bearings[6],
                        bearing_with_vibration_sensor_8=bearings[7],
                        bearing_without_vibration_sensor_9=bearings[8],
                        is_active=exhauster_kafka_data["exhauster"]["is_active"],
                        loaded_from_kafka_at=loaded_from_kafka_at,
                    )
                    exhausters.append(exhauster)
                SessionLocal.add_all(exhausters)
                SessionLocal.commit()

    @classmethod
    def __parse_kafka_data(cls, data):
        parsed_data = dict()
        exhauster_machine_mapping = {
            0: (0, 1, 0),
            1: (0, 1, 1),
            2: (2, 4, 0),
            3: (2, 4, 1),
            4: (3, 5, 0),
            5: (3, 5, 1),
        }
        for k, v in data.items():
            for idx, i in enumerate(
                [
                    "exhauster_1",
                    "exhauster_2",
                    "exhauster_3",
                    "exhauster_4",
                    "exhauster_5",
                    "exhauster_6",
                ]
            ):
                temperature_order, drive_order, number = exhauster_machine_mapping[idx]
                parsed_data[i] = {
                    "bearings": cls.__parse_vibro_bearing_list(data, idx),
                    "exhauster": cls.__parse_exgauster_data(
                        data, temperature_order, drive_order, number
                    ),
                }
        return parsed_data

    @classmethod
    def __parse_vibro_bearing(
        cls, data: dict, order: int, offset: int, number: int, vibro_number: int
    ) -> dict:
        key = "SM_Exgauster\[{}:{}]"

        data = {
            "vibration_horizontal": {
                "value": data.get(
                    key.format(order, offset * 3 * 4 + vibro_number * 3 + 0), None
                ),
                "alarm_max": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 135), None
                ),
                "alarm_min": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 147), None
                ),
                "warning_max": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 159), None
                ),
                "warning_min": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 172), None
                ),
            },
            "vibration_vertical": {
                "value": data.get(
                    key.format(order, offset * 3 * 4 + vibro_number * 3 + 1), None
                ),
                "alarm_max": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 136), None
                ),
                "alarm_min": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 148), None
                ),
                "warning_max": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 159), None
                ),
                "warning_min": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 171), None
                ),
            },
            "vibration_axial": {
                "value": data.get(
                    key.format(order, offset * 3 * 4 + vibro_number * 3 + 2), None
                ),
                "alarm_max": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 137), None
                ),
                "alarm_min": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 149), None
                ),
                "warning_max": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 159), None
                ),
                "warning_min": data.get(
                    key.format(order, offset * 4 * 9 + vibro_number * 3 + 173), None
                ),
            },
            "temperature": {
                "value": data.get(key.format(order, offset * 16 + number + 27), None),
                "alarm_max": data.get(
                    key.format(order, offset * 4 * 9 + number + 63), None
                ),
                "alarm_min": data.get(
                    key.format(order, offset * 4 * 9 + number + 72), None
                ),
                "warning_max": data.get(
                    key.format(order, offset * 4 * 9 + number + 81), None
                ),
                "warning_min": data.get(
                    key.format(order, offset * 4 * 9 + number + 90), None
                ),
            },
        }

        if (
            data["vibration_horizontal"]["value"]
            >= data["vibration_horizontal"]["alarm_max"]
            or data["vibration_horizontal"]["value"]
            <= data["vibration_horizontal"]["alarm_min"]
            or data["vibration_vertical"]["value"]
            >= data["vibration_vertical"]["alarm_max"]
            or data["vibration_vertical"]["value"]
            <= data["vibration_vertical"]["alarm_min"]
            or data["vibration_axial"]["value"] >= data["vibration_axial"]["alarm_max"]
            or data["vibration_axial"]["value"] <= data["vibration_axial"]["alarm_min"]
        ):
            data["vibration_status"] = "alert"
        elif (
            data["vibration_horizontal"]["value"]
            >= data["vibration_horizontal"]["warning_max"]
            or data["vibration_horizontal"]["value"]
            <= data["vibration_horizontal"]["warning_min"]
            or data["vibration_vertical"]["value"]
            >= data["vibration_horizontal"]["warning_max"]
            or data["vibration_vertical"]["value"]
            <= data["vibration_horizontal"]["warning_min"]
            or data["vibration_axial"]["value"]
            >= data["vibration_axial"]["warning_max"]
            or data["vibration_axial"]["value"]
            <= data["vibration_axial"]["warning_min"]
        ):
            data["vibration_status"] = "warning"
        else:
            data["vibration_status"] = "ok"

        if (
            data["temperature"]["value"] >= data["temperature"]["alarm_max"]
            or data["temperature"]["value"] <= data["temperature"]["alarm_min"]
        ):
            data["temperature_status"] = "alert"
        elif (
            data["temperature"]["value"] >= data["temperature"]["warning_max"]
            or data["temperature"]["value"] <= data["temperature"]["warning_min"]
        ):
            data["temperature_status"] = "warning"
        else:
            data["temperature_status"] = "ok"

        for kk, vv in data.items():
            if kk in ["vibration_horizontal", "vibration_axial", "vibration_vertical", "temperature"]:
                for k, v in vv.items():
                    if v is not None:
                        data[kk][k] = round(v, 1)
        return data

    @classmethod
    def __parse_bearing(cls, data:dict, order, offset, number ):
        key = "SM_Exgauster\[{}:{}]"
        data = {
                   "temperature": {
            "value": data.get(key.format(order, offset * 16 + number + 27), None),
            "alarm_max": data.get(
                key.format(order, offset * 4 * 9 + number + 63), None
            ),
            "alarm_min": data.get(
                key.format(order, offset * 4 * 9 + number + 72), None
            ),
            "warning_max": data.get(
                key.format(order, offset * 4 * 9 + number + 81), None
            ),
            "warning_min": data.get(
                key.format(order, offset * 4 * 9 + number + 90), None
            ),
        }
        }

        if (
                data["temperature"]["value"] >= data["temperature"]["alarm_max"]
                or data["temperature"]["value"] <= data["temperature"]["alarm_min"]
        ):
            data["temperature_status"] = "alert"
        elif (
                data["temperature"]["value"] >= data["temperature"]["warning_max"]
                or data["temperature"]["value"] <= data["temperature"]["warning_min"]
        ):
            data["temperature_status"] = "warning"
        else:
            data["temperature_status"] = "ok"
        return data

    @classmethod
    def __parse_vibro_bearing_list(cls, data: dict, order: int) -> list[dict]:
        bearing_list: list[dict] = []
        exhauster_machine_mapping = {
            0: (0, 0),
            1: (0, 1),
            2: (2, 0),
            3: (2, 1),
            4: (3, 0),
            5: (3, 1),
        }
        vibro_bearings = {
            0: 0,
            1: 1,
            6: 2,
            7: 3
        }
        machine_num, exhauster_num = exhauster_machine_mapping[order]
        for bearing_num in range(9):
            if bearing_num in vibro_bearings:
                bearing_list.append(
                    cls.__parse_vibro_bearing(data, machine_num, exhauster_num, bearing_num, vibro_bearings[bearing_num])
                )
            else:
                bearing_list.append(
                    cls.__parse_bearing(data, machine_num, exhauster_num, bearing_num)
                )
        return bearing_list

    @classmethod
    def __parse_exgauster_data(
        cls, data, temperature_order: int, drive_order: int, number: int
    ):
        key = "SM_Exgauster\[{}{}{}]"

        data = {
            "is_active": data.get(key.format(temperature_order, ".", number), None),
            "refrigerant": {
                "water_temperature_before": data.get(
                    key.format(temperature_order, ":", 36 + number * 17 + number), None
                ),
                "water_temperature_after": data.get(
                    key.format(temperature_order, ":", 37 + number * 17 + number), None
                ),
                "oil_temperature_before": data.get(
                    key.format(temperature_order, ":", 41 + number * 17 + number), None
                ),
                "oil_temperature_after": data.get(
                    key.format(temperature_order, ":", 42 + number * 17 + number), None
                ),
            },
            "gas_manifold": {
                "temperature_before": data.get(
                    key.format(temperature_order, ":", 24 + number), None
                ),
                "underpressure_before": data.get(
                    key.format(temperature_order, ":", 61 + number), None
                ),
            },
            "oil_system": {
                "oil_level": data.get(
                    key.format(drive_order, ":", number * 7 + number), None
                ),
                "oil_pressure": data.get(
                    key.format(drive_order, ":", number * 7 + number + 1), None
                ),
            },
            "valve_position": {
                "gas_valve_closed": data.get(
                    key.format(drive_order, ".", number * 5 + number + 1), None
                ),
                "gas_valve_open": data.get(
                    key.format(drive_order, ".", number * 5 + number + 2), None
                ),
                "gas_valve_position": data.get(
                    key.format(drive_order, ":", number * 5 + number + 6), None
                ),
            },
            "main_drive": {
                "rotor_current": data.get(
                    key.format(drive_order, ":", number * 7 + number + 2), None
                ),
                "stator_current": data.get(
                    key.format(drive_order, ":", number * 7 + number + 3), None
                ),
                "rotor_voltage": data.get(
                    key.format(drive_order, ":", number * 7 + number + 4), None
                ),
                "stator_voltage": data.get(
                    key.format(drive_order, ":", number * 7 + number + 5), None
                ),
            },
        }

        for kk, vv in data.items():
            if kk in ["main_drive", "valve_position", "oil_system", "gas_manifold", "refrigerant"]:
                for k, v in vv.items():
                    if v is not None:
                        data[kk][k] = round(v, 1)
        data["main_drive"]["rotor_voltage"] = data["main_drive"]["rotor_voltage"]/10 if data["main_drive"]["rotor_voltage"] else None
        data["main_drive"]["stator_voltage"] = data["main_drive"]["stator_voltage"]/10 if data["main_drive"]["rotor_voltage"] else None

        return data
