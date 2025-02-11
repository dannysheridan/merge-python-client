# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .accounting_period_status import AccountingPeriodStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AccountingPeriod(pydantic.BaseModel):
    """
    # The AccountingPeriod Object
    ### Description
    The `AccountingPeriod` object is used to define a period of time in which events occurred.

    ### Usage Example
    Common models like `Invoice` and `Transaction` will have `AccountingPeriod` objects which will denote when they occurred.
    """

    start_date: typing.Optional[dt.datetime] = pydantic.Field(description="Beginning date of the period")
    end_date: typing.Optional[dt.datetime] = pydantic.Field(description="End date of the period")
    status: typing.Optional[AccountingPeriodStatus]
    name: typing.Optional[str] = pydantic.Field(description="Name of the accounting period.")
    id: typing.Optional[str]
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

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
