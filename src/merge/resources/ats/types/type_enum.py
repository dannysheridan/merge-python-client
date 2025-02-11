# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypeEnum(str, enum.Enum):
    """
    * `DATE` - DATE
    * `FILE` - FILE
    * `SINGLE_SELECT` - SINGLE_SELECT
    * `MULTI_SELECT` - MULTI_SELECT
    * `SINGLE_LINE_TEXT` - SINGLE_LINE_TEXT
    * `MULTI_LINE_TEXT` - MULTI_LINE_TEXT
    * `NUMERIC` - NUMERIC
    * `BOOLEAN` - BOOLEAN
    """

    DATE = "DATE"
    FILE = "FILE"
    SINGLE_SELECT = "SINGLE_SELECT"
    MULTI_SELECT = "MULTI_SELECT"
    SINGLE_LINE_TEXT = "SINGLE_LINE_TEXT"
    MULTI_LINE_TEXT = "MULTI_LINE_TEXT"
    NUMERIC = "NUMERIC"
    BOOLEAN = "BOOLEAN"

    def visit(
        self,
        date: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        single_select: typing.Callable[[], T_Result],
        multi_select: typing.Callable[[], T_Result],
        single_line_text: typing.Callable[[], T_Result],
        multi_line_text: typing.Callable[[], T_Result],
        numeric: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TypeEnum.DATE:
            return date()
        if self is TypeEnum.FILE:
            return file()
        if self is TypeEnum.SINGLE_SELECT:
            return single_select()
        if self is TypeEnum.MULTI_SELECT:
            return multi_select()
        if self is TypeEnum.SINGLE_LINE_TEXT:
            return single_line_text()
        if self is TypeEnum.MULTI_LINE_TEXT:
            return multi_line_text()
        if self is TypeEnum.NUMERIC:
            return numeric()
        if self is TypeEnum.BOOLEAN:
            return boolean()
