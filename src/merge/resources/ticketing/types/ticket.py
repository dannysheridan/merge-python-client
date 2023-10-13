# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .remote_field import RemoteField
from .ticket_account import TicketAccount
from .ticket_assignees_item import TicketAssigneesItem
from .ticket_collections_item import TicketCollectionsItem
from .ticket_contact import TicketContact
from .ticket_creator import TicketCreator
from .ticket_priority import TicketPriority
from .ticket_status import TicketStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Ticket(pydantic.BaseModel):
    """
    # The Ticket Object
    ### Description
    The `Ticket` object is used to represent a ticket or a task within a system.

    ### Usage Example
    TODO
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The ticket's name.")
    assignees: typing.Optional[typing.List[typing.Optional[TicketAssigneesItem]]]
    creator: typing.Optional[TicketCreator] = pydantic.Field(description="The user who created this ticket.")
    due_date: typing.Optional[dt.datetime] = pydantic.Field(description="The ticket's due date.")
    status: typing.Optional[TicketStatus] = pydantic.Field(
        description=(
            "The current status of the ticket.\n"
            "\n"
            "* `OPEN` - OPEN\n"
            "* `CLOSED` - CLOSED\n"
            "* `IN_PROGRESS` - IN_PROGRESS\n"
            "* `ON_HOLD` - ON_HOLD\n"
        )
    )
    description: typing.Optional[str] = pydantic.Field(
        description="The ticket’s description. HTML version of description is mapped if supported by the third-party platform."
    )
    collections: typing.Optional[typing.List[typing.Optional[TicketCollectionsItem]]]
    ticket_type: typing.Optional[str] = pydantic.Field(description="The ticket's type.")
    account: typing.Optional[TicketAccount] = pydantic.Field(description="The account associated with the ticket.")
    contact: typing.Optional[TicketContact] = pydantic.Field(description="The contact associated with the ticket.")
    parent_ticket: typing.Optional[TicketParentTicket] = pydantic.Field(description="The ticket's parent ticket.")
    attachments: typing.Optional[typing.List[typing.Optional[TicketAttachmentsItem]]]
    tags: typing.Optional[typing.List[typing.Optional[str]]]
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's ticket was created."
    )
    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's ticket was updated."
    )
    completed_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the ticket was completed.")
    remote_was_deleted: typing.Optional[bool]
    ticket_url: typing.Optional[str] = pydantic.Field(description="The 3rd party url of the Ticket.")
    priority: typing.Optional[TicketPriority] = pydantic.Field(
        description=(
            "The priority or urgency of the Ticket.\n"
            "\n"
            "* `URGENT` - URGENT\n"
            "* `HIGH` - HIGH\n"
            "* `NORMAL` - NORMAL\n"
            "* `LOW` - LOW\n"
        )
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

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


from .ticket_attachments_item import TicketAttachmentsItem  # noqa: E402
from .ticket_parent_ticket import TicketParentTicket  # noqa: E402

Ticket.update_forward_refs()
