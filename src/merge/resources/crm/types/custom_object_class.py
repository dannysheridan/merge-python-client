# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_field_class_for_custom_object_class import RemoteFieldClassForCustomObjectClass

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CustomObjectClass(pydantic.BaseModel):
    """
    # The Custom Object Class Object
    ### Description
    The `Custom Object Class` object is used to represent a Custom Object Schema in the remote system.
    ### Usage Example
    TODO
    """

    name: typing.Optional[str]
    description: typing.Optional[str]
    labels: typing.Optional[typing.Dict[str, typing.Optional[str]]]
    fields: typing.Optional[typing.List[RemoteFieldClassForCustomObjectClass]]
    association_types: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    modified_at: typing.Optional[dt.datetime]

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
