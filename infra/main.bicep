// infra/main.bicep — provisions the ctwarrick.dev hosting in a new resource
// group within the existing subscription.
//
// Why: per the constitution's attack-surface rule and FR-012/FR-013, production
// is a single Azure Static Web App (Free SKU) serving pre-rendered static
// files — no app server, no database. This template creates a new resource
// group and the Static Web App, and (optionally) binds the apex and `www`
// custom domains so `www.ctwarrick.dev` can redirect to the canonical apex
// `ctwarrick.dev` (contracts/static-hosting.md, research.md §7).
//
// Scope: subscription (so the resource group itself is created here).
// Deploy with:
//   az deployment sub create \
//     --location <region> \
//     --template-file infra/main.bicep \
//     --parameters infra/main.bicepparam
//
// Custom-domain binding requires DNS validation (Azure DNS zone delegated from
// GoDaddy, per research.md §7) and is provisioned after the SWA exists; the
// `customDomainName`/`wwwDomainName` parameters are optional and the
// `customDomains` resources are only created when they are non-empty, so the
// base SWA can be deployed first and domains added once DNS is delegated.

targetScope = 'subscription'

@description('Name of the new resource group to create for the site.')
param resourceGroupName string

@description('Azure region for the resource group and Static Web App.')
param location string

@description('Name of the Azure Static Web App resource.')
param staticWebAppName string

@description('Apex custom domain (canonical), e.g. ctwarrick.dev. Leave empty to skip binding until DNS is delegated.')
param customDomainName string = ''

@description('www custom domain that redirects to the apex, e.g. www.ctwarrick.dev. Leave empty to skip binding until DNS is delegated.')
param wwwDomainName string = ''

resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: resourceGroupName
  location: location
}

module staticWebApp 'static-web-app.bicep' = {
  name: 'static-web-app'
  scope: rg
  params: {
    staticWebAppName: staticWebAppName
    location: location
    customDomainName: customDomainName
    wwwDomainName: wwwDomainName
  }
}

@description('The default *.azurestaticapps.net hostname of the Static Web App.')
output defaultHostname string = staticWebApp.outputs.defaultHostname
