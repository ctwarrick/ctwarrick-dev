// infra/main.bicep — provisions the ctwarrick.dev hosting in a new resource
// group within the existing subscription.
//
// Why: per the constitution's attack-surface rule and FR-012/FR-013, production
// is a single Azure Static Web App (Free SKU) serving pre-rendered static
// files — no app server, no database. This template creates a new resource
// group, the Static Web App, and the Azure DNS zone for the apex domain.
//
// Scope: subscription (so the resource group itself is created here).
// Deploy with:
//   az deployment sub create \
//     --location <region> \
//     --template-file infra/main.bicep \
//     --parameters infra/main.bicepparam
//
// Custom-domain binding is NOT modeled here. The apex (`ctwarrick.dev`,
// canonical) and the `www` redirect are bound on the Static Web App via the
// portal's "Custom Domain on Azure DNS" flow after DNS is delegated from
// GoDaddy to the `nameServers` output below — the apex `dns-txt-token`
// validation token is not exposed as a Bicep output, so a declarative bind
// deadlocks (Azure/static-web-apps#1652; research.md §7).

targetScope = 'subscription'

@description('Name of the new resource group to create for the site.')
param resourceGroupName string

@description('Azure region for the resource group and Static Web App.')
param location string

@description('Name of the Azure Static Web App resource.')
param staticWebAppName string

@description('DNS zone (apex domain) name, e.g. ctwarrick.dev.')
param dnsZoneName string

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
  }
}

module dns 'dns.bicep' = {
  name: 'dns'
  scope: rg
  params: {
    dnsZoneName: dnsZoneName
  }
}

@description('The default *.azurestaticapps.net hostname of the Static Web App.')
output defaultHostname string = staticWebApp.outputs.defaultHostname

@description('Azure nameservers for the DNS zone — set these at GoDaddy to delegate DNS.')
output nameServers array = dns.outputs.nameServers
