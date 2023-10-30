# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExpensesListRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNT_ACCOUNTING_PERIOD = "account,accounting_period"
    ACCOUNT_COMPANY = "account,company"
    ACCOUNT_COMPANY_ACCOUNTING_PERIOD = "account,company,accounting_period"
    ACCOUNT_CONTACT = "account,contact"
    ACCOUNT_CONTACT_ACCOUNTING_PERIOD = "account,contact,accounting_period"
    ACCOUNT_CONTACT_COMPANY = "account,contact,company"
    ACCOUNT_CONTACT_COMPANY_ACCOUNTING_PERIOD = "account,contact,company,accounting_period"
    ACCOUNTING_PERIOD = "accounting_period"
    COMPANY = "company"
    COMPANY_ACCOUNTING_PERIOD = "company,accounting_period"
    CONTACT = "contact"
    CONTACT_ACCOUNTING_PERIOD = "contact,accounting_period"
    CONTACT_COMPANY = "contact,company"
    CONTACT_COMPANY_ACCOUNTING_PERIOD = "contact,company,accounting_period"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNT = "tracking_categories,account"
    TRACKING_CATEGORIES_ACCOUNT_ACCOUNTING_PERIOD = "tracking_categories,account,accounting_period"
    TRACKING_CATEGORIES_ACCOUNT_COMPANY = "tracking_categories,account,company"
    TRACKING_CATEGORIES_ACCOUNT_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,account,company,accounting_period"
    TRACKING_CATEGORIES_ACCOUNT_CONTACT = "tracking_categories,account,contact"
    TRACKING_CATEGORIES_ACCOUNT_CONTACT_ACCOUNTING_PERIOD = "tracking_categories,account,contact,accounting_period"
    TRACKING_CATEGORIES_ACCOUNT_CONTACT_COMPANY = "tracking_categories,account,contact,company"
    TRACKING_CATEGORIES_ACCOUNT_CONTACT_COMPANY_ACCOUNTING_PERIOD = (
        "tracking_categories,account,contact,company,accounting_period"
    )
    TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "tracking_categories,accounting_period"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,company,accounting_period"
    TRACKING_CATEGORIES_CONTACT = "tracking_categories,contact"
    TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = "tracking_categories,contact,accounting_period"
    TRACKING_CATEGORIES_CONTACT_COMPANY = "tracking_categories,contact,company"
    TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,contact,company,accounting_period"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        account_accounting_period: typing.Callable[[], T_Result],
        account_company: typing.Callable[[], T_Result],
        account_company_accounting_period: typing.Callable[[], T_Result],
        account_contact: typing.Callable[[], T_Result],
        account_contact_accounting_period: typing.Callable[[], T_Result],
        account_contact_company: typing.Callable[[], T_Result],
        account_contact_company_accounting_period: typing.Callable[[], T_Result],
        accounting_period: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        company_accounting_period: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_accounting_period: typing.Callable[[], T_Result],
        contact_company: typing.Callable[[], T_Result],
        contact_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_account: typing.Callable[[], T_Result],
        tracking_categories_account_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_account_company: typing.Callable[[], T_Result],
        tracking_categories_account_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_account_contact: typing.Callable[[], T_Result],
        tracking_categories_account_contact_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_account_contact_company: typing.Callable[[], T_Result],
        tracking_categories_account_contact_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_contact: typing.Callable[[], T_Result],
        tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_contact_company: typing.Callable[[], T_Result],
        tracking_categories_contact_company_accounting_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpensesListRequestExpand.ACCOUNT:
            return account()
        if self is ExpensesListRequestExpand.ACCOUNT_ACCOUNTING_PERIOD:
            return account_accounting_period()
        if self is ExpensesListRequestExpand.ACCOUNT_COMPANY:
            return account_company()
        if self is ExpensesListRequestExpand.ACCOUNT_COMPANY_ACCOUNTING_PERIOD:
            return account_company_accounting_period()
        if self is ExpensesListRequestExpand.ACCOUNT_CONTACT:
            return account_contact()
        if self is ExpensesListRequestExpand.ACCOUNT_CONTACT_ACCOUNTING_PERIOD:
            return account_contact_accounting_period()
        if self is ExpensesListRequestExpand.ACCOUNT_CONTACT_COMPANY:
            return account_contact_company()
        if self is ExpensesListRequestExpand.ACCOUNT_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return account_contact_company_accounting_period()
        if self is ExpensesListRequestExpand.ACCOUNTING_PERIOD:
            return accounting_period()
        if self is ExpensesListRequestExpand.COMPANY:
            return company()
        if self is ExpensesListRequestExpand.COMPANY_ACCOUNTING_PERIOD:
            return company_accounting_period()
        if self is ExpensesListRequestExpand.CONTACT:
            return contact()
        if self is ExpensesListRequestExpand.CONTACT_ACCOUNTING_PERIOD:
            return contact_accounting_period()
        if self is ExpensesListRequestExpand.CONTACT_COMPANY:
            return contact_company()
        if self is ExpensesListRequestExpand.CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return contact_company_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT:
            return tracking_categories_account()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_ACCOUNTING_PERIOD:
            return tracking_categories_account_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_COMPANY:
            return tracking_categories_account_company()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_account_company_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_CONTACT:
            return tracking_categories_account_contact()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_CONTACT_ACCOUNTING_PERIOD:
            return tracking_categories_account_contact_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_CONTACT_COMPANY:
            return tracking_categories_account_contact_company()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_account_contact_company_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return tracking_categories_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_company_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_CONTACT:
            return tracking_categories_contact()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return tracking_categories_contact_accounting_period()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_CONTACT_COMPANY:
            return tracking_categories_contact_company()
        if self is ExpensesListRequestExpand.TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_contact_company_accounting_period()
