# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TimesheetEntryRequest(pydantic.BaseModel):
    """
    # The Timesheet Entry Object
    ### Description
    The `Timesheet Entry` object is used to track coverage for hours worked by an 'Employee'.


    ### Usage Example
    GET and POST Timesheet Entries
    """

    employee: typing.Optional[str] = pydantic.Field(description="The employee the timesheet entry is for.")
    hours_worked: typing.Optional[float] = pydantic.Field(description="The number of hours logged by the employee.")
    start_time: typing.Optional[dt.datetime] = pydantic.Field(
        description="The time at which the employee started work."
    )
    end_time: typing.Optional[dt.datetime] = pydantic.Field(description="The time at which the employee ended work.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
