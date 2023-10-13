# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.async_passthrough.client import AsyncAsyncPassthroughClient
from .resources.async_passthrough.client import (
    AsyncPassthroughClient as resources_hris_resources_async_passthrough_client_AsyncPassthroughClient,
)
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.bank_info.client import AsyncBankInfoClient, BankInfoClient
from .resources.benefits.client import AsyncBenefitsClient, BenefitsClient
from .resources.companies.client import AsyncCompaniesClient, CompaniesClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.dependents.client import AsyncDependentsClient, DependentsClient
from .resources.employee_payroll_runs.client import AsyncEmployeePayrollRunsClient, EmployeePayrollRunsClient
from .resources.employees.client import AsyncEmployeesClient, EmployeesClient
from .resources.employer_benefits.client import AsyncEmployerBenefitsClient, EmployerBenefitsClient
from .resources.employments.client import AsyncEmploymentsClient, EmploymentsClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.groups.client import AsyncGroupsClient, GroupsClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.locations.client import AsyncLocationsClient, LocationsClient
from .resources.passthrough.client import (
    AsyncPassthroughClient as resources_hris_resources_passthrough_client_AsyncPassthroughClient,
)
from .resources.passthrough.client import PassthroughClient
from .resources.pay_groups.client import AsyncPayGroupsClient, PayGroupsClient
from .resources.payroll_runs.client import AsyncPayrollRunsClient, PayrollRunsClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.selective_sync.client import AsyncSelectiveSyncClient, SelectiveSyncClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.teams.client import AsyncTeamsClient, TeamsClient
from .resources.time_off.client import AsyncTimeOffClient, TimeOffClient
from .resources.time_off_balances.client import AsyncTimeOffBalancesClient, TimeOffBalancesClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class HrisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = resources_hris_resources_async_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.available_actions = AvailableActionsClient(client_wrapper=self._client_wrapper)
        self.bank_info = BankInfoClient(client_wrapper=self._client_wrapper)
        self.benefits = BenefitsClient(client_wrapper=self._client_wrapper)
        self.companies = CompaniesClient(client_wrapper=self._client_wrapper)
        self.delete_account = DeleteAccountClient(client_wrapper=self._client_wrapper)
        self.dependents = DependentsClient(client_wrapper=self._client_wrapper)
        self.employee_payroll_runs = EmployeePayrollRunsClient(client_wrapper=self._client_wrapper)
        self.employees = EmployeesClient(client_wrapper=self._client_wrapper)
        self.employer_benefits = EmployerBenefitsClient(client_wrapper=self._client_wrapper)
        self.employments = EmploymentsClient(client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(client_wrapper=self._client_wrapper)
        self.groups = GroupsClient(client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.locations = LocationsClient(client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(client_wrapper=self._client_wrapper)
        self.pay_groups = PayGroupsClient(client_wrapper=self._client_wrapper)
        self.payroll_runs = PayrollRunsClient(client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.selective_sync = SelectiveSyncClient(client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(client_wrapper=self._client_wrapper)
        self.teams = TeamsClient(client_wrapper=self._client_wrapper)
        self.time_off = TimeOffClient(client_wrapper=self._client_wrapper)
        self.time_off_balances = TimeOffBalancesClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(client_wrapper=self._client_wrapper)


class AsyncHrisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AsyncAccountTokenClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = AsyncAsyncPassthroughClient(client_wrapper=self._client_wrapper)
        self.available_actions = AsyncAvailableActionsClient(client_wrapper=self._client_wrapper)
        self.bank_info = AsyncBankInfoClient(client_wrapper=self._client_wrapper)
        self.benefits = AsyncBenefitsClient(client_wrapper=self._client_wrapper)
        self.companies = AsyncCompaniesClient(client_wrapper=self._client_wrapper)
        self.delete_account = AsyncDeleteAccountClient(client_wrapper=self._client_wrapper)
        self.dependents = AsyncDependentsClient(client_wrapper=self._client_wrapper)
        self.employee_payroll_runs = AsyncEmployeePayrollRunsClient(client_wrapper=self._client_wrapper)
        self.employees = AsyncEmployeesClient(client_wrapper=self._client_wrapper)
        self.employer_benefits = AsyncEmployerBenefitsClient(client_wrapper=self._client_wrapper)
        self.employments = AsyncEmploymentsClient(client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(client_wrapper=self._client_wrapper)
        self.groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.locations = AsyncLocationsClient(client_wrapper=self._client_wrapper)
        self.passthrough = resources_hris_resources_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.pay_groups = AsyncPayGroupsClient(client_wrapper=self._client_wrapper)
        self.payroll_runs = AsyncPayrollRunsClient(client_wrapper=self._client_wrapper)
        self.regenerate_key = AsyncRegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.selective_sync = AsyncSelectiveSyncClient(client_wrapper=self._client_wrapper)
        self.sync_status = AsyncSyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(client_wrapper=self._client_wrapper)
        self.teams = AsyncTeamsClient(client_wrapper=self._client_wrapper)
        self.time_off = AsyncTimeOffClient(client_wrapper=self._client_wrapper)
        self.time_off_balances = AsyncTimeOffBalancesClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(client_wrapper=self._client_wrapper)
