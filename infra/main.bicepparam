// infra/main.bicepparam — deploy-time parameter values for main.bicep.
//
// resourceGroupName/location are the deploy-time choices for the new resource
// group (research.md §7, contracts/static-hosting.md). westus2 is a real
// Azure region that supports Static Web Apps Free SKU; adjust if a closer
// region is preferred. customDomainName/wwwDomainName are left empty until
// the Azure DNS zone is delegated from GoDaddy — bind them in a follow-up
// deploy once DNS is ready.

using 'main.bicep'

param resourceGroupName = 'rg-ctwarrick-web'
param location = 'westus2'
param staticWebAppName = 'ctwarrick-dev'
param customDomainName = ''
param wwwDomainName = ''
