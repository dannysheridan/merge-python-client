# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .scorecard_application import ScorecardApplication
from .scorecard_interview import ScorecardInterview
from .scorecard_interviewer import ScorecardInterviewer
from .scorecard_overall_recommendation import ScorecardOverallRecommendation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Scorecard(pydantic.BaseModel):
    """
    # The Scorecard Object
    ### Description
    The `Scorecard` object is used to represent an interviewer's candidate recommendation based on a particular interview.
    ### Usage Example
    Fetch from the `LIST Scorecards` endpoint and filter by `application` to show all scorecard for an applicant.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    application: typing.Optional[ScorecardApplication] = pydantic.Field(description="The application being scored.")
    interview: typing.Optional[ScorecardInterview] = pydantic.Field(description="The interview being scored.")
    interviewer: typing.Optional[ScorecardInterviewer] = pydantic.Field(
        description="The interviewer doing the scoring."
    )
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's scorecard was created."
    )
    submitted_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the scorecard was submitted.")
    overall_recommendation: typing.Optional[ScorecardOverallRecommendation] = pydantic.Field(
        description=(
            "The inteviewer's recommendation.\n"
            "\n"
            "* `DEFINITELY_NO` - DEFINITELY_NO\n"
            "* `NO` - NO\n"
            "* `YES` - YES\n"
            "* `STRONG_YES` - STRONG_YES\n"
            "* `NO_DECISION` - NO_DECISION\n"
        )
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
