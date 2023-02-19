from datetime import datetime, timedelta
from typing import Optional, List
from sqlalchemy.orm import joinedload
from pydantic import ValidationError

from app.schema.exhauster.exhauster import Exhauster
from app.schema.exhauster.exhauster_with_bearings import ExhausterWithBearings
from app.schema.exhauster.exsgauter_metadata import ExsgauterMetadata
from app.models.exhauster import (
    ExhausterModel,
    BearingWithoutVibrationSensorModel,
    BearingWithVibrationSensorModel,
    ExhausterMetadataModel,
    SensorModel
)
from app.controllers.base_repository import BaseRepository
from app.views.helpers.base_exceptions import RecordsNotLoadedError


MODEL = ExhausterModel
DOMAIN = Exhauster


class ExhausterRepository(BaseRepository[MODEL, DOMAIN]):
    def __init__(self):
        super().__init__(MODEL, DOMAIN)

    def get_graph_data(self, rotor_number, lines):
        points = {}
        for line in lines:
            bearing, sensor = line.split("__")
            temperature_data = (
                self._session.query(
                    ExhausterModel.loaded_from_kafka_at,
                    BearingWithVibrationSensorModel.temperature_id,
                    SensorModel.value,
                    ExsgauterMetadataModel.rotor_number
                )
                .filter(
                    getattr(ExhausterModel, f"{bearing}_id")
                    == BearingWithVibrationSensorModel.id
                )
                .filter(
                    getattr(BearingWithVibrationSensorModel, f"{sensor}_id")
                    == SensorModel.id
                )
                .filter(
                    ExhausterModel.loaded_from_kafka_at
                    >= datetime.now() - timedelta(days=21)
                )
			.filter(ExhausterModel.meta_id == ExhausterMetadataModel.id)\
            .filter(ExhausterMetadataModel.rotor_number == rotor_number)\
                .distinct(ExhausterModel.loaded_from_kafka_at)
                .all()
            )
            points[f"{bearing}__{sensor}"] = [
                [datetime.timestamp(i[0]), i[2]] for i in temperature_data
            ]
        # line: [(x: datetime, y: value), ...]

        return points

    def _to_domain(self, model: MODEL) -> Optional[MODEL]:
        if model:
            return self._domain.from_orm(model)

    def _to_domain_exhauster_with_bearings(
        self, model: ExhausterWithBearings
    ) -> Optional[ExhausterWithBearings]:
        if model:
            return ExhausterWithBearings.from_orm(model)

    def get_all(self) -> List[ExhausterWithBearings]:
        last_records_datetime = self.__get_last_records_datetime()
        if last_records_datetime is None:
            raise RecordsNotLoadedError
        models = (
            self._session.query(self._model)
            .options(*self.__get_joinedload_bearings_only())
            .options(
                joinedload(self._model.meta),
            )
            .filter(self._model.loaded_from_kafka_at == last_records_datetime)
            .all()
        )
        schemas = [self._to_domain_exhauster_with_bearings(model) for model in models]
        return schemas

    def get_by_rotor_number(self, rotor_number: int) -> MODEL:
        last_records_datetime = self.__get_last_records_datetime()
        model = (
            self._session.query(self._model)
            .join(
                ExhausterMetadataModel, ExhausterMetadataModel.id == self._model.meta_id
            )
            .options(*self.__get_joinedload_bearings_only())
            .options(
                joinedload(self._model.gas_manifold),
                joinedload(self._model.main_drive),
                joinedload(self._model.oil_system),
                joinedload(self._model.refrigerant),
                joinedload(self._model.valve_position),
                joinedload(self._model.meta),
            )
            .filter(self._model.loaded_from_kafka_at == last_records_datetime)
            .filter(ExhausterMetadataModel.rotor_number == rotor_number)
            .first()
        )
        # model_dict = model.__dict__
        schema = self._to_domain(model)
        return schema

    def __get_last_records_datetime(self):
        return (
            self._session.query(self._model.loaded_from_kafka_at)
            .order_by(self._model.loaded_from_kafka_at.desc())
            .first()[0]
        )

    def __get_joinedload_bearings_only(self):
        return (
            joinedload(self._model.bearing_with_vibration_sensor_1),
            joinedload(self._model.bearing_with_vibration_sensor_2),
            joinedload(self._model.bearing_with_vibration_sensor_7),
            joinedload(self._model.bearing_with_vibration_sensor_8),
            joinedload(self._model.bearing_without_vibration_sensor_3),
            joinedload(self._model.bearing_without_vibration_sensor_4),
            joinedload(self._model.bearing_without_vibration_sensor_5),
            joinedload(self._model.bearing_without_vibration_sensor_6),
            joinedload(self._model.bearing_without_vibration_sensor_9),
        )

    # def __get_multiple_nested_joined_load_bearings(self):
    #     for

    # def create(self, data: dict) -> DOMAIN:
    #     if data.get(self._domain_referred_attr):
    #         self._referred_model_repository._check_unique_wagon_groups(
    #             data[self._domain_referred_attr]
    #         )
    #     return super().create(data)

    # def update(self, model_id: int, data: dict) -> DOMAIN:
    #     model = self._model.query.get(model_id)
    #     if model is None:
    #         raise ObjectNotFoundError
    #     new_parameters_ids = data.get(self._domain_referred_attr, [])
    #     if new_parameters_ids:
    #         self._referred_model_repository._check_unique_wagon_groups(
    #             data[self._domain_referred_attr]
    #         )
    #         old_parameters = model.parameters or []
    #         unbound_parameters_ids = [
    #             parameter.id
    #             for parameter in old_parameters
    #             if parameter.id not in new_parameters_ids
    #         ]
    #     else:
    #         unbound_parameters_ids = []
    #     domain = super().update(model_id, data)
    #     if unbound_parameters_ids:
    #         self._referred_model_repository._delete_unbound_parameters(
    #             unbound_parameters_ids
    #         )
    #     self._session.close()
    #     return domain

    # def copy_category(self, category_id: int, data: dict):
    #     copied_model = self.get_by_id(category_id)
    #     copied_model_dict = copied_model.to_dict()
    #     for attr, value in data.items():
    #         copied_model_dict[attr] = value
    #     parameters = self._referred_model_repository.filter(
    #         category_id=category_id
    #     ).all()
    #     new_parameters_ids = []
    #     for parameter in parameters:
    #         self._referred_model_repository._copy_parameter(parameter)
    #         new_parameters_ids.append(parameter.id)
    #     copied_model_dict["parameters_ids"] = new_parameters_ids
    #     del copied_model_dict["id"]
    #     return super().create(copied_model_dict)
