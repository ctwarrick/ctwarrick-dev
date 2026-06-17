// infra/main.bicepparam — deploy-time parameter values for main.bicep.
//
// resourceGroupName/location are the deploy-time choices for the new resource
// group (research.md §7, contracts/static-hosting.md). westus2 is a real Azure
// region that supports Static Web Apps Free SKU; adjust if a closer region is
// preferred. dnsZoneName is the apex domain: after deploy, delegate GoDaddy's
// nameservers to the zone's `nameServers` output, then bind the apex + `www`
// custom domains on the SWA via the portal's "Custom Domain on Azure DNS" flow.

using 'main.bicep'

param resourceGroupName = 'rg-ctwarrick-web'
param location = 'westus2'
param staticWebAppName = 'ctwarrick-dev'
param dnsZoneName = 'ctwarrick.dev'
