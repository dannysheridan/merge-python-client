# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .bank_info_account_type import BankInfoAccountType
from .bank_info_employee import BankInfoEmployee
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BankInfo(pydantic.BaseModel):
    """
    # The BankInfo Object
    ### Description
    The `BankInfo` object is used to represent the Bank Account information for an Employee.

    ### Usage Example
    Fetch from the `LIST BankInfo` endpoint and filter by `ID` to show all bank information.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    employee: typing.Optional[BankInfoEmployee] = pydantic.Field(description="The employee with this bank account.")
    account_number: typing.Optional[str] = pydantic.Field(description="The account number.")
    routing_number: typing.Optional[str] = pydantic.Field(description="The routing number.")
    bank_name: typing.Optional[str] = pydantic.Field(description="The bank name.")
    account_type: typing.Optional[BankInfoAccountType] = pydantic.Field(
        description=("The bank account type\n" "\n" "* `SAVINGS` - SAVINGS\n" "* `CHECKING` - CHECKING\n")
    )
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the matching bank object was created in the third party system."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

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
