"""add root migration

Revision ID: 953ac7fd2de2
Revises: 
Create Date: 2023-02-18 00:12:32.944541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Sequence, CreateSequence, DropSequence
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "953ac7fd2de2"
down_revision = None
branch_labels = None
depends_on = None


def create_sequence(name: str):
    field_seq = Sequence(name, schema="service_all")
    op.execute(CreateSequence(field_seq))
    return field_seq


sensor_types_enum = postgresql.ENUM(
    "temperature",
    "vibration",
    name="sensor_types",
)
sensor_statuses_enum = postgresql.ENUM(
    "ok",
    "warning",
    "alert",
    "no_data",
    name="sensor_statuses_enum",
)


def upgrade() -> None:
    op.execute("create schema service_all")
    op.execute("create schema catalogs")
    op.create_table(
        "refrigerant",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("refrigerant_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("water_temperature_after", sa.Numeric(6, 2)),
        sa.Column("water_temperature_before", sa.Numeric(6, 2)),
        sa.Column("oil_temperature_after", sa.Numeric(6, 2)),
        sa.Column("oil_temperature_before", sa.Numeric(6, 2)),
        schema="service_all",
        comment="refrigerant with water and oil data table",
    )
    op.create_table(
        "gas_manifold",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("gas_manifold_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("temperature_before", sa.Numeric(6, 2)),
        sa.Column("underpressure_before", sa.Numeric(6, 2)),
        schema="service_all",
        comment="Gas manifold table",
    )

    op.create_table(
        "valve_position",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("valve_position_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("gas_valve_closed", sa.Numeric(6, 2)),
        sa.Column("gas_valve_open", sa.Numeric(6, 2)),
        sa.Column("gas_valve_position", sa.Numeric(6, 2)),
        schema="service_all",
        comment="Valve position table",
    )
    op.create_table(
        "main_drive",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("main_drive_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("rotor_current", sa.Numeric(6, 2)),
        sa.Column("rotor_voltage", sa.Numeric(6, 2)),
        sa.Column("stator_current", sa.Numeric(6, 2)),
        sa.Column("stator_voltage", sa.Numeric(6, 2)),
        schema="service_all",
        comment="Main drive table",
    )
    op.create_table(
        "oil_system",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("oil_system_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("oil_level", sa.Numeric(6, 2)),
        sa.Column("oil_pressure", sa.Numeric(6, 2)),
        schema="service_all",
        comment="Oil pressure table",
    )
    op.create_table(
        "exsgauter_metadata",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("exsgauter_metadata_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("exhauster_name", sa.String(50), nullable=False),
        sa.Column("rotor_instalation", sa.Date, nullable=False),
        sa.Column("rotor_number", sa.Integer, nullable=False),
        sa.Column("sinter_machine_name", sa.String(20), nullable=False),
        schema="catalogs",
        comment="Oil pressure table",
    )
    op.create_table(
        "sensor",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("sensor_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column("value", sa.Numeric(6, 2)),
        sa.Column("alarm_max", sa.Numeric(6, 2)),
        sa.Column("alarm_min", sa.Numeric(6, 2)),
        sa.Column("warning_max", sa.Numeric(6, 2)),
        sa.Column("warning_min", sa.Numeric(6, 2)),
        sa.Column("type", sensor_types_enum, nullable=False),
        schema="service_all",
        comment="Sensors with temperature or vibration table",
    )
    op.create_table(
        "bearing_with_vibration_sensor",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence(
                "bearing_with_vibration_sensor_id_seq"
            ).next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column(
            "temperature_id",
            sa.Integer,
            sa.ForeignKey("service_all.sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "axial_vibration_id",
            sa.Integer,
            sa.ForeignKey("service_all.sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "horizontal_vibration_id",
            sa.Integer,
            sa.ForeignKey("service_all.sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "vertical_vibration_id",
            sa.Integer,
            sa.ForeignKey("service_all.sensor.id"),
            nullable=False,
        ),
        sa.Column("number", sa.SmallInteger, nullable=False),
        sa.Column("temperature_status", sensor_statuses_enum, nullable=False),
        sa.Column("vibration_status", sensor_statuses_enum, nullable=False),
        schema="service_all",
        comment="Bearing with vibration sensor table",
    )
    op.create_table(
        "bearing_without_vibration_sensor",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence(
                "bearing_without_vibration_sensor_id_seq"
            ).next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column(
            "temperature_id",
            sa.Integer,
            sa.ForeignKey("service_all.sensor.id"),
            nullable=False,
        ),
        sa.Column("number", sa.SmallInteger, nullable=False),
        sa.Column("temperature_status", sensor_statuses_enum, nullable=False),
        schema="service_all",
        comment="Bearing without vibration sensor table",
    )
    op.create_table(
        "exhauster",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            server_default=create_sequence("exhauster_id_seq").next_value(),
            nullable=False,
            comment="Суррогатный первичный ключ",
        ),
        sa.Column(
            "meta_id",
            sa.Integer,
            sa.ForeignKey("catalogs.exsgauter_metadata.id"),
            nullable=False,
        ),
        sa.Column(
            "refrigerant_id",
            sa.Integer,
            sa.ForeignKey("service_all.refrigerant.id"),
            nullable=False,
        ),
        sa.Column(
            "gas_manifold_id",
            sa.Integer,
            sa.ForeignKey("service_all.gas_manifold.id"),
            nullable=False,
        ),
        sa.Column(
            "valve_position_id",
            sa.Integer,
            sa.ForeignKey("service_all.valve_position.id"),
            nullable=False,
        ),
        sa.Column(
            "main_drive_id",
            sa.Integer,
            sa.ForeignKey("service_all.main_drive.id"),
            nullable=False,
        ),
        sa.Column(
            "oil_system_id",
            sa.Integer,
            sa.ForeignKey("service_all.oil_system.id"),
            nullable=False,
        ),
        sa.Column(
            "bearing_with_vibration_sensor_1_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_with_vibration_sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "bearing_with_vibration_sensor_2_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_with_vibration_sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "bearing_with_vibration_sensor_7_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_with_vibration_sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "bearing_with_vibration_sensor_8_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_with_vibration_sensor.id"),
            nullable=False,
        ),
        sa.Column(
            "bearing_without_vibration_sensor_3_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_without_vibration_sensor.id"),
            nullable=True,
        ),
        sa.Column(
            "bearing_without_vibration_sensor_4_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_without_vibration_sensor.id"),
            nullable=True,
        ),
        sa.Column(
            "bearing_without_vibration_sensor_5_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_without_vibration_sensor.id"),
            nullable=True,
        ),
        sa.Column(
            "bearing_without_vibration_sensor_6_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_without_vibration_sensor.id"),
            nullable=True,
        ),
        sa.Column(
            "bearing_without_vibration_sensor_9_id",
            sa.Integer,
            sa.ForeignKey("service_all.bearing_without_vibration_sensor.id"),
            nullable=True,
        ),
        sa.Column("loaded_from_kafka_at", sa.TIMESTAMP, nullable=False),
        sa.Column("is_active", sa.SmallInteger, nullable=False),
        schema="service_all",
        comment="Root exhauster table",
    )


def downgrade() -> None:
    op.drop_table("exsgauter_metadata", "catalogs")
    op.drop_table("oil_system", "service_all")
    op.drop_table("main_drive", "service_all")
    op.drop_table("gas_manifold", "service_all")
    op.drop_table("valve_position", "service_all")
    op.drop_table("refrigerant", "service_all")
    op.drop_table("sensor", "service_all")
    op.drop_table("bearing_without_vibration_sensor", "service_all")
    op.drop_table("bearing_with_vibration_sensor", "service_all")
    op.drop_table("exhauster", "service_all")
    sensor_types_enum.drop(op.get_bind())
    sensor_statuses_enum.drop(op.get_bind())
    op.execute(DropSequence(Sequence("exsgauter_metadata_id_seq", schema="catalogs")))
    op.execute(DropSequence(Sequence("oil_system_id_seq", schema="service_all")))
    op.execute(DropSequence(Sequence("main_drive_id_seq", schema="service_all")))
    op.execute(DropSequence(Sequence("gas_manifold_id_seq", schema="service_all")))
    op.execute(DropSequence(Sequence("valve_position_id_seq", schema="service_all")))
    op.execute(DropSequence(Sequence("refrigerant_id_seq", schema="service_all")))
    op.execute(DropSequence(Sequence("sensor_id_seq", schema="service_all")))
    op.execute(
        DropSequence(
            Sequence("bearing_without_vibration_sensor_id_seq", schema="service_all")
        )
    )
    op.execute(
        DropSequence(
            Sequence("bearing_with_vibration_sensor_id_seq", schema="service_all")
        )
    )
    op.execute(DropSequence(Sequence("exhauster_id_seq", schema="service_all")))
    op.execute("drop schema service_all")
    op.execute("drop schema catalogs")
