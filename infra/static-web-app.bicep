// infra/static-web-app.bicep — the Azure Static Web App (Free SKU), deployed
// into the resource group created by main.bicep.
//
// Custom domains are intentionally NOT modeled here. Apex (`ctwarrick.dev`) is
// canonical (FR-013) and `www` 301-redirects to it via the SWA default-domain
// setting; both are bound on this app through the portal's "Custom Domain on
// Azure DNS" flow once DNS is delegated to the Azure DNS zone (research.md §7).
// A declarative apex bind is not possible in a single deployment because the
// apex `dns-txt-token` validation token is not exposed as a Bicep/ARM output,
// so the customDomains resource deadlocks in "Validating"
// (Azure/static-web-apps#1652).

@description('Name of the Azure Static Web App resource.')
param staticWebAppName string

@description('Azure region for the Static Web App.')
param location string

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

@description('The default *.azurestaticapps.net hostname of the Static Web App.')
output defaultHostname string = staticSite.properties.defaultHostname
