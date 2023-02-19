from typing import List
from fastapi import Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.entrypoint.database import SessionLocal
from app.models.exhauster import (
    BearingWithVibrationSensorModel,
    BearingWithoutVibrationSensorModel,
    ExhausterModel,
    ExhausterMetadataModel,
    GasManifoldModel,
    MainDriveModel,
    OilSystemModel,
    RefrigerantModel,
    SensorModel,
    ValvePositionModel,
)
from app.schema.exhauster.exhauster_with_bearings import ExhausterWithBearings
from app.schema.exhauster.exhauster import Exhauster
from app.controllers.exhauster_repository import ExhausterRepository
from app.services.kafka_consumer_service import KafkaConsumerService

exhauster_router = InferringRouter()


@cbv(exhauster_router)
class ExhausterRouter:
    __repository: ExhausterRepository = Depends(ExhausterRepository)
    # __user: User = Depends(get_current_user)

    @exhauster_router.get("/")
    async def get_all(self) -> List:
        schemas = self.__repository.get_all()
        # new_schemas = []
        # for i in schemas:
        #     data_dict = {}
        #     for k, v in {"bearing_with_vibration_sensor_1": "bearing1", "bearing_with_vibration_sensor_2":"bearing2",
        #               "bearing_with_vibration_sensor_7":"bearing3", "bearing_with_vibration_sensor_8":"bearing4"}.items():
        #         data_dict[f"{v}__temperature"] = getattr(i, k).temperature.value
        #         data_dict[f"{v}__axial"] = getattr(i, k).axial_vibration.value
        #         data_dict[f"{v}__vertical"] = getattr(i, k).vertical_vibration.value
        #         data_dict[f"{v}__horizontal"] = getattr(i, k).horizontal_vibration.value
        #     new_schemas.append(data_dict)
        # print(new_schemas[0])
        return schemas

    @exhauster_router.get("/one/{rotor_number}")
    async def get(self, rotor_number: int) -> Exhauster:
        schema = self.__repository.get_by_rotor_number(rotor_number)
        # for k, v in {"bearing_with_vibration_sensor_1": "bearing1", "bearing_with_vibration_sensor_2": "bearing2",
        #              "bearing_with_vibration_sensor_7": "bearing3",
        #              "bearing_with_vibration_sensor_8": "bearing4"}.items():
        #     bearing_data = {}
        #     bearing = getattr(schema, k)
        #     for kk, vv in {"temperature": "temperature", "axial_vibration":"axial",
        #                    "vertical_vibration":"vertical", "horizontal_vibration":"horizontal"}.items():
        #         sensor = getattr(bearing, kk)
        #         for kkk in ["value", "warning_min", "warning_max", "alarm_min", "alarm_max"]:
        #             limit = getattr(sensor, kkk)
        #             bearing_data[f"{v}__{vv}__{kkk}"] = limit
        #     bearings.append(bearing_data)
        return schema

    @exhauster_router.post("/graph/{rotor_number}")
    async def get_graph(self, rotor_number: int, lines: list):
        return self.__repository.get_graph_data(rotor_number, lines)
