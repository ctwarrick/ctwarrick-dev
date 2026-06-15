// infra/static-web-app.bicep — the Azure Static Web App (Free SKU) and its
// optional custom-domain bindings, deployed into the resource group created
// by main.bicep.
//
// Apex (`customDomainName`) is canonical (FR-013); `www` (`wwwDomainName`),
// once bound and DNS-validated, redirects to it per
// contracts/static-hosting.md and staticwebapp.config.json. Both domain
// params default to empty so the SWA can be created before DNS is delegated
// to Azure DNS (research.md §7) — bindings are added in a follow-up deploy
// once the GoDaddy nameservers point at the Azure DNS zone.

@description('Name of the Azure Static Web App resource.')
param staticWebAppName string

@description('Azure region for the Static Web App.')
param location string

@description('Apex custom domain (canonical), e.g. ctwarrick.dev. Empty = not bound yet.')
param customDomainName string = ''

@description('www custom domain that redirects to the apex, e.g. www.ctwarrick.dev. Empty = not bound yet.')
param wwwDomainName string = ''

resource staticSite 'Microsoft.Web/staticSites@2024-04-01' = {
  name: staticWebAppName
  location: location
  sku: {
    name: 'Free'
    tier: 'Free'
  }
  properties: {
    // Source-less: content is deployed by CI (Azure/static-web-apps-deploy
    // with skip_app_build: true), not built from a linked repo.
    allowConfigFileUpdates: true
    stagingEnvironmentPolicy: 'Disabled'
  }
}

resource apexDomain 'Microsoft.Web/staticSites/customDomains@2024-04-01' = if (!empty(customDomainName)) {
  parent: staticSite
  name: customDomainName
}

resource wwwDomain 'Microsoft.Web/staticSites/customDomains@2024-04-01' = if (!empty(wwwDomainName)) {
  parent: staticSite
  name: wwwDomainName
  dependsOn: [
    apexDomain
  ]
}

@description('The default *.azurestaticapps.net hostname of the Static Web App.')
output defaultHostname string = staticSite.properties.defaultHostname
